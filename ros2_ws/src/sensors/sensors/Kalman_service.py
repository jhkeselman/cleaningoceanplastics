import time
import math


import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, Bool, Float32MultiArray, Float64MultiArray
from sensor_msgs.msg import NavSatFix, Imu
from services.srv import KalmanState
#from tf_transformations import euler_from_quaternion
import transforms3d

import math
import numpy as np

W_RADIUS = 6371000 #radius of earth in m
CEP = 2.5 #Circular error probable from Ozzmaker website
AVERAGE = 10 #Number of values for gps before beginning
MASS = 23 #NEED VALUES
DRAG = 0.5 
INERTIA = 200  #GET FROM SOLIDWORKS
R = 0.31875 #radius from center of robot to motor
V_TO_N = 4.6025 #conversion from Volts to Newtons of thrust

class KalmanService(Node):

    def __init__(self):
        super().__init__('Kalman_service')
        self.srv = self.create_service(KalmanState, 'get_Kalman_state', self.return_state)
        self.pub = self.create_publisher(Float64MultiArray,'get_state',10)

        self.imu_sub = self.create_subscription(Imu,'IMU_data',self.imu_response_callback,10)
        self.gps_sub = self.create_subscription(NavSatFix,'get_GPS',self.gps_response_callback,10)
        self.duty_sub = self.create_subscription(Float32MultiArray,'set_duty_cycle',self.duty_cycle_callback,10)
        self.motor_sub = self.create_subscription(Float32MultiArray,'set_motor_speeds',self.motor_speed_callback,10)

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )
        
        self.avg_pos = np.zeros((AVERAGE,2))
        self.avg_i = 0
        self.gps_ready = False
        self.state = np.zeros((5,1),np.float64) #x,y,v,theta,omega
        self.covariance = np.diag([2.5,2.5,0.25,0.1,0.1])
        
        self.dt = 0.1
        self.timer = self.create_timer(self.dt,self.calc_state)

        self.R = 0.1 * np.ones((5,5),np.float64) #model noise
        self.Q = 0.1 * np.ones((5,5),np.float64) #sensor noise
        self.sensor_data = np.zeros((5,1),np.float64)
        self.Tl = 0 #thrust left
        self.Tr = 0 
    
    def calc_state(self):
        #NON-LINEAR STATE PREDICTION
        state_pred = np.zeros((5,1))
        state_pred[0,0] = self.state[0,0] + self.state[2,0]*math.cos(self.state[3,0])*self.dt + (self.Tl + self.Tr - (DRAG*self.state[2,0]**2)*math.cos(self.state[3,0])*self.dt**2)/(2*MASS)
        state_pred[1,0] = self.state[1,0] + self.state[2,0]*math.sin(self.state[3,0])*self.dt + (self.Tl + self.Tr - (DRAG*self.state[2,0]**2)*math.sin(self.state[3,0])*self.dt**2)/(2*MASS)
        state_pred[2,0] = (self.Tl + self.Tr - (DRAG*self.state[2,0]**2)*self.dt)/MASS + self.state[2,0]
        state_pred[3,0] = self.state[4]*self.dt + self.state[3,0]
        state_pred[4,0] = (self.Tl + self.Tr - (1.25*DRAG*self.state[2,0]**2)*self.dt)/INERTIA + self.state[4,0] #drag increased by 25% for rotation

        G = np.array([[1,0,(math.cos(self.state[3,0])*self.dt - (self.dt**2)*DRAG*self.state[2,0]*math.cos(self.state[3,0])/MASS),(-self.state[2,0]*math.sin(self.state[3,0])*self.dt - (self.Tl + self.Tr - (DRAG*self.state[2,0]**2)*math.sin(self.state[3,0])*self.dt**2)/(2*MASS)),0],
                      [0,1,(math.sin(self.state[3,0])*self.dt - (self.dt**2)*DRAG*self.state[2,0]*math.sin(self.state[3,0])/MASS),(self.state[2,0]*math.cos(self.state[3,0])*self.dt + (self.Tl + self.Tr - (DRAG*self.state[2,0]**2)*math.cos(self.state[3,0])*self.dt**2)/(2*MASS)),0],
                      [0,0,(-2*self.dt*DRAG*self.state[2,0]/MASS + 1),0,0],
                      [0,0,0,1,self.dt],
                      [0,0,0,0,(-2*self.dt*1.25*DRAG*self.state[4,0]/INERTIA + 1)]],np.float64)

        covariance_pred = np.matmul(G,np.matmul(self.covariance,G.T)) + self.R

        #CORRECTION
        H = np.array([[1,0,0,0,0],
                      [0,1,0,0,0],
                      [0,0,(-2*DRAG*self.state[2,0])/MASS,0,0],
                      [0,0,0,1,0],
                      [0,0,0,0,1]],np.float64)
        
        inv_part = np.linalg.pinv(np.matmul(H,np.matmul(covariance_pred,H.T))+self.Q)
        K = np.matmul(covariance_pred,np.matmul(H.T,inv_part))
        sensor_model = self.state.copy()
        sensor_model[2,0] = (self.Tl + self.Tr - (DRAG*self.state[2]**2))/MASS
        self.state = state_pred + np.matmul(K,(self.sensor_data - sensor_model))
        self.covariance = np.matmul((np.eye(5) - np.matmul(K,H)),covariance_pred)
        msg = Float64MultiArray()

        msg.data = self.state
        self.pub.publish(msg)
        

    def return_state(self, request, response):
        response.state.data = self.state.T
        self.get_logger().info('Incoming request')
        return response
    
    def duty_cycle_callback(self,msg):
        Vl = (7.5-msg.data[0])/7.5*24
        Vr = (7.5-msg.data[1])/7.5*24
        self.Tl = Vl * V_TO_N
        self.Tr = Vr * V_TO_N

    def motor_speed_callback(self,msg):
        duty_l = 7.5 - 2.5*msg.data[0] #Center at 7.5 and capped at 5 and 10
        duty_r = 7.5 - 2.5*msg.data[1]
        Vl = (duty_l-7.5)/7.5*24
        Vr = (duty_r-7.5)/7.5*24
        self.Tl = Vl * V_TO_N
        self.Tr = Vr * V_TO_N


    def imu_response_callback(self,msg):
        #(roll,pitch,yaw) = euler_from_quaternion([msg.orientation.x,msg.orientation.y,msg.orientation.z,msg.orientation.w])
        roll,pitch,yaw = transforms3d.euler.quat2euler([msg.orientation.x,msg.orientation.y,msg.orientation.z,msg.orientation.w],axes='sxyz')
        acc = msg.linear_acceleration.x
        omega = msg.angular_velocity.z
        self.sensor_data[2:5,0] = [acc,yaw,omega]
        # self.get_logger().info('IMU Heading %5.3f, Acc %5.3f, Omega %5.3f:' %(yaw, acc, omega))

    def gps_response_callback(self,msg):
        fix_status = msg.status.status
        if fix_status >=0 :
            self.get_logger().info('GPS Fix %d, Lat %5.8f, Long %5.8f:' %(fix_status, msg.latitude, msg.longitude))
            self.get_logger().info('GPS Covariance Long %5.3f, Lat %5.2f' %(msg.position_covariance[0], msg.position_covariance[0]))
            if self.avg_i < AVERAGE-1:
                fix = [math.radians(msg.latitude), math.radians(msg.longitude)]
                self.avg_pos[self.avg_i,:] = fix    
                self.avg_i += 1               
            elif self.avg_i == AVERAGE-1: #if there hasn't been an origin established, keep averaging values
                fix = [math.radians(msg.latitude), math.radians(msg.longitude)]
                self.avg_pos[self.avg_i,:] = fix #stores fixes to average thm
                avg_lat = self.avg_pos[:,0].mean(axis=0)
                avg_lon = self.avg_pos[:,1].mean(axis=0)
                self.first_fix = [avg_lat,avg_lon,math.cos(avg_lat)] #stores the average as the first position and origin
                gps_covariance = self.calc_covariance(msg)
                self.Q[0,0] = gps_covariance[0]
                self.Q[1,1] = gps_covariance[1]
                self.get_logger().info('Position (X,Y): (%5.3f +/- %5.3f, %5.3f +/- %5.3f)' %(self.dx,self.covariance[0][0],self.dy,self.covariance[1][1]))  
                self.avg_i += 1
                self.gps_ready = True
            else: 
                [dx,dy] = self.calc_dist(msg) #once an origin has been established begin calculating distance from origin
                gps_covariance = self.calc_covariance(msg)
                self.sensor_data[0:2,0] = [dx,dy]
                self.Q[0,0] = gps_covariance[0]
                self.Q[1,1] = gps_covariance[1]
                # self.get_logger().info('Position (X,Y): (%5.3f +/- %5.3f, %5.3f +/- %5.3f)' %(self.dx,self.gps_covariance[0][0],self.dy,self.gps_covariance[1][1]))  
        else:
                self.get_logger().info('No GPS Fix')

    def calc_dist(self,fix):
        dx = W_RADIUS*(math.radians(fix.longitude) - self.first_fix[1])*self.first_fix[2] #Uses equirectangular projection to determine x,y distance from origin
        dy = W_RADIUS*(math.radians(fix.latitude) - self.first_fix[0])
        return [dx,dy]
    
    def calc_covariance(self,fix):
        if fix.position_covariance_type == NavSatFix.COVARIANCE_TYPE_APPROXIMATED: 
            x_lon = 1.2 * CEP
            y_lat = 1.2 * CEP
        else:
            x_lon = fix.position_covariance[0]
            y_lat = fix.position_covariance[4]
        sigma_x = x_lon
        sigma_y = y_lat
        return [sigma_x**2,sigma_y**2]

    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()

def main():
    rclpy.init()

    kalman_service = KalmanService()

    rclpy.spin(kalman_service)
    kalman_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()