import time
import math


import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64, Bool, Float64MultiArray
from sensor_msgs.msg import NavSatFix, Imu
from services.srv import KalmanState
from tf_transformations import euler_from_quaternion

import math
import numpy as np

RADIUS = 6371000
UERE = 4.0
AVERAGE = 10
MASS = 23 #NEED VALUES
DRAG = 0.5
INERTIA = 200 

class KalmanService(Node):

    def __init__(self):
        super().__init__('Kalman_service')
        self.srv = self.create_service(KalmanState, 'get_Kalman_state', self.return_state)

        self.imu_sub = self.create_subscription(Imu,'IMU_data',self.imu_response_callback,10)
        self.gps_sub = self.create_subscription(NavSatFix,'get_GPS',self.gps_response_callback,10)
        self.motor_sub = self.create_subscription(Float64MultiArray, 'motor_speeds', self.motor_callback,10)

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )
        
        self.avg_pos = np.zeros((AVERAGE,2))
        self.avg_i = 0
        self.gps_ready = False
        self.state = np.zeros((5,1),np.float32) #x,y,v,theta,omega
        self.covariance = np.zeros((5,5))
        
        self.dt = 0.1
        self.timer = self.create_timer(self.dt,self.calc_state)

        R = 0.1 * np.ones((5,5)) #model noise
        Q = 0.1 * np.ones((5,5)) #sensor noise
        self.sensor_data = np.zeros((5,1))
        self.Tl = 0
        self.Tr = 0
    
    def calc_state(self):
        #NON-LINEAR STATE PREDICTION
        state_pred = np.zeros((5,1))
        state_pred[0] = self.state[0] + self.state[2]*math.cos(self.state[3])*self.dt + (self.Tl + self.Tr - (DRAG*self.state[2]**2)*math.cos(self.state[3])*self.dt**2)/(2*MASS)
        state_pred[1] = self.state[1] + self.state[2]*math.sin(self.state[3])*self.dt + (self.Tl + self.Tr - (DRAG*self.state[2]**2)*math.sin(self.state[3])*self.dt**2)/(2*MASS)
        state_pred[2] = (self.Tl + self.Tr - (DRAG*self.state[2]**2)*self.dt)/MASS + self.state[2]
        state_pred[3] = self.state[4]*self.dt + self.state[3]
        state_pred[4] = (self.Tl + self.Tr - (1.25*DRAG*self.state[2]**2)*self.dt)/INERTIA + self.state[4] #drag increased by 25% for rotation

        G1 = np.array([1,0,math.cos(self.state[3,0])*self.dt - (self.dt**2)*DRAG*self.state[2,0]*math.cos(self.state[3,0])/MASS,-self.state[2,0]*math.sin(self.state[3,0])*self.dt - (self.Tl + self.Tr - (DRAG*self.state[2,0]**2)*math.sin(self.state[3,0])*self.dt**2)/(2*MASS),0])
        print(G1)
        G = np.array([[1,0,(math.cos(self.state[3])*self.dt - (self.dt**2)*DRAG*self.state[2]*math.cos(self.state[3])/MASS),(-self.state[2]*math.sin(self.state[3])*self.dt - (self.Tl + self.Tr - (DRAG*self.state[2]**2)*math.sin(self.state[3])*self.dt**2)/(2*MASS)),0],
                      [0,1,(math.sin(self.state[3])*self.dt - (self.dt**2)*DRAG*self.state[2]*math.sin(self.state[3])/MASS),(self.state[2]*math.cos(self.state[3])*self.dt + (self.Tl + self.Tr - (DRAG*self.state[2]**2)*math.cos(self.state[3])*self.dt**2)/(2*MASS)),0],
                      [0,0,(-2*self.dt*DRAG*self.state[2]/MASS + 1),0,0],
                      [0,0,0,1,self.dt],
                      [0,0,0,0,1]])
        
        covariance_pred = np.matmul(G,np.matmul(self.covariance,G.T)) + self.R

        #CORRECTION
        H = np.array([[1,0,0,0,0],
                      [0,1,0,0,0],
                      [0,0,(self.Tl + self.Tr - (DRAG*self.state[2]**2))/MASS,0,0],
                      [0,0,0,1,0],
                      [0,0,0,0,1]])
        
        K = np.matmul(covariance_pred,np.matmul(H.T,np.inv(np.matmul(H,np.matmul(covariance_pred,H.T))+self.Q)))
        sensor_model = self.state
        sensor_model[2] = (self.Tl + self.Tr - (DRAG*self.state[2]**2))/MASS
        self.state = state_pred + np.matmul(K,(self.sensor_data - sensor_model))
        self.covariance = np.matmul((np.eye(5) - np.mapmul(K,H)),covariance_pred)

    def return_state(self, request, response):
        response.state.data = self.state.T
        self.get_logger().info('Incoming request')
        return response
    
    def motor_callback(self,msg):
        self.Tl = msg.data[0]
        self.Tr = msg.data[1]

    def imu_response_callback(self,msg):
        print(type(msg.orientation))
        (roll,pitch,yaw) = euler_from_quaternion([msg.orientation.x,msg.orientation.y,msg.orientation.z,msg.orientation.w])
        acc = msg.linear_acceleration.x
        omega = msg.angular_velocity.z
        self.get_logger().info('IMU Heading %5.3f, Acc %5.3f, Omega %5.3f:' %(yaw, acc, omega))

    def gps_response_callback(self,msg):
        fix_status = msg.status.status
        if fix_status >=0 :
            self.get_logger().info('GPS Fix %d, Lat %5.8f, Long %5.8f:' %(fix_status, msg.fix.latitude, msg.fix.longitude))
            self.get_logger().info('GPS Covariance Long %5.3f, Lat %5.2f' %(msg.fix.position_covariance[0], msg.fix.position_covariance[0]))
            if self.avg_i < AVERAGE-1:
                fix = [math.radians(msg.fix.latitude), math.radians(msg.fix.longitude)]
                self.avg_pos[self.avg_i,:] = fix    
                self.avg_i += 1               
            elif self.avg_i == AVERAGE-1:
                fix = [math.radians(msg.fix.latitude), math.radians(msg.fix.longitude)]
                self.avg_pos[self.avg_i,:] = fix
                avg_lat = self.avg_pos[:,0].mean(axis=0)
                avg_lon = self.avg_pos[:,1].mean(axis=0)
                self.first_fix = [avg_lat,avg_lon,math.cos(avg_lat)]
                self.covariance = self.calc_covariance(msg.fix)
                self.dx = 0
                self.dy = 0
                self.get_logger().info('Position (X,Y): (%5.3f +/- %5.3f, %5.3f +/- %5.3f)' %(self.dx,self.covariance[0][0],self.dy,self.covariance[1][1]))  
                self.avg_i += 1
                self.gps_ready = True
            else:
                [self.dx,self.dy] = self.calc_dist(msg.fix)
                self.covariance = self.calc_covariance(msg.fix)
                self.get_logger().info('Position (X,Y): (%5.3f +/- %5.3f, %5.3f +/- %5.3f)' %(self.dx,self.covariance[0][0],self.dy,self.covariance[1][1]))  
        else:
                self.get_logger().info('No GPS Fix')

    def calc_dist(self,fix):
        dx = RADIUS*(math.radians(fix.longitude) - self.first_fix[1])*self.first_fix[2]
        dy = RADIUS*(math.radians(fix.latitude) - self.first_fix[0])
        return [dx,dy]
    
    def calc_covariance(self,fix):
        if fix.position_covariance_type == NavSatFix.COVARIANCE_TYPE_APPROXIMATED:
            x_lon = fix.position_covariance[0]*UERE
            y_lat = fix.position_covariance[4]*UERE
        else:
            x_lon = fix.position_covariance[0]
            y_lat = fix.position_covariance[4]
        sigma_x = x_lon
        sigma_y = y_lat

        covariance = np.array([[sigma_x**2,0],[0,sigma_y**2]])
        return covariance

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