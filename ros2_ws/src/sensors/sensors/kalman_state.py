import time
import math


import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, Bool, Float32MultiArray, Float64MultiArray
from sensor_msgs.msg import NavSatFix, Imu
from tf_transformations import euler_from_quaternion

import math
import numpy as np

W_RADIUS = 6371000 #radius of earth in m
CEP = 2.5 #Circular error probable in m from Ozzmaker website
AVERAGE = 10 #Number of values for gps before beginning
MASS = 23 # Mass of robot in kg
DRAG = 160.65 # Linear drag estimate (all constants lumped) in Kg/m
ROT_DRAG = 8.44 # Rotational drag estimate (all constants lumped) in Kg*m/rad^2
INERTIA = 5.35  #Inertia from Solidworks model in Kg/m^2
R = 0.31875 #radius from center of robot to motor in m
V_TO_N = 4.6025 #conversion from Volts to Newtons of thrust


# This node reads and publishes GPS information for the robot.
# Using GPSD, the node interprets lat,long, and uncertainty data and publishes
# Publishers: 'get_state'
# Subscribers: 'IMU_data', 'get_GPS', 'set_motor_speeds', 'emergency_stop'

class KalmanState(Node):

    def __init__(self):
        super().__init__('Kalman_state')

        # Publisher for robot state
        # Message type: Float64MultiArray
        self.pub = self.create_publisher(Float64MultiArray,'get_state',10)

        # Subscription to IMU, GPS, and motor data. Each has its own callback to process and store values
        self.imu_sub = self.create_subscription(Imu,'IMU_data',self.imu_response_callback,10)
        self.gps_sub = self.create_subscription(NavSatFix,'get_GPS',self.gps_response_callback,10)
        self.motor_sub = self.create_subscription(Float32MultiArray,'set_motor_speeds',self.motor_speed_callback,10)

        # Subscription to emergency stop topic
        # If emergency stop is triggered, the node will be destroyed
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )
        
        # Initializing values to calculate initial position and acceleration bias
        self.avg_pos = np.zeros((AVERAGE,2))
        self.avg_i = 0
        self.acc_bias_data = np.zeros(AVERAGE)
        self.bias_i = 0
        self.acc_bias = 0
        self.gps_ready = False

        # Initializing state and covariance. State is set to all zeros
        self.state = np.zeros((5,1),np.float64) #x,y,v,theta,omega
        self.covariance = np.diag([2.5,2.5,1,1.5,1])
        
        # Timer loop to calculate state (same as gyro refresh rate)
        self.dt = 0.02
        self.timer = self.create_timer(self.dt,self.calc_state)

        # Model (R) and Sensor (Q) noise initialized along diag. Small noise to allow for inverting
        self.R = np.diag([2.5,2.5,0.1,0.1,0.1]) + 0.01*np.ones((5,5))#model noise
        self.Q = np.diag([0.75,0.75,1.5,1,1]) + 0.01*np.ones((5,5))#sensor noise

        # Vector to store sensor data and thrust
        self.sensor_data = np.zeros((5,1),np.float64)
        self.Tl = 0 # thrust left
        self.Tr = 0 # thrust right
    
    def calc_state(self):
        ''' EKF STATE PREDICTION '''

        # Accounting for direction of linear and angular drag
        drag_dir = -1 if self.state[2,0] >= 0 else 1 
        rot_dir = -1 if self.state[4,0] >= 0 else 1

        # State prediction based off of equations of motion
        state_pred = np.zeros((5,1))
        state_pred[0,0] = self.state[0,0] + self.state[2,0]*math.cos(self.state[3,0])*self.dt + ((self.Tl + self.Tr + drag_dir*DRAG*(self.state[2,0]**2))*math.cos(self.state[3,0])*self.dt**2)/(2*MASS)
        state_pred[1,0] = self.state[1,0] + self.state[2,0]*math.sin(self.state[3,0])*self.dt + ((self.Tl + self.Tr + drag_dir*DRAG*(self.state[2,0]**2))*math.sin(self.state[3,0])*self.dt**2)/(2*MASS)
        state_pred[2,0] = (self.Tl + self.Tr + (drag_dir*DRAG*(self.state[2,0]**2))*self.dt)/MASS + self.state[2,0]
        state_pred[3,0] = self.state[4,0]*self.dt + self.state[3,0]
        state_pred[4,0] = (-R*self.Tl + R*self.Tr + (rot_dir*ROT_DRAG*(self.state[4,0]**2))*self.dt)/INERTIA + self.state[4,0] 

        # Jacobian of predicted state wrt state
        G = np.array([[1,0,(math.cos(self.state[3,0])*self.dt + (self.dt**2)*drag_dir*DRAG*self.state[2,0]*math.cos(self.state[3,0])/MASS),(-self.state[2,0]*math.sin(self.state[3,0])*self.dt - ((self.Tl + self.Tr + drag_dir*DRAG*(self.state[2,0]**2))*math.sin(self.state[3,0])*self.dt**2)/(2*MASS)),0],
                      [0,1,(math.sin(self.state[3,0])*self.dt + (self.dt**2)*drag_dir*DRAG*self.state[2,0]*math.sin(self.state[3,0])/MASS),(self.state[2,0]*math.cos(self.state[3,0])*self.dt + ((self.Tl + self.Tr + drag_dir*DRAG*(self.state[2,0]**2))*math.cos(self.state[3,0])*self.dt**2)/(2*MASS)),0],
                      [0,0,(drag_dir*2*self.dt*DRAG*self.state[2,0]/MASS + 1),0,0],
                      [0,0,0,1,self.dt],
                      [0,0,0,0,(rot_dir*2*self.dt*ROT_DRAG*(self.state[4,0]**2)/INERTIA + 1)]],np.float64)

        # Covariance predicted
        covariance_pred = np.matmul(G,np.matmul(self.covariance,G.T)) + self.R

        ''' CORRECTION '''
        # Jacobian of observation model wrt state
        H = np.array([[1,0,0,0,0],
                      [0,1,0,0,0],
                      [0,0,(drag_dir*2*DRAG*state_pred[2,0])/MASS,0,0],
                      [0,0,0,1,0],
                      [0,0,0,0,1]],np.float64)
        
        # Pseudoinverse is computed to prevent singularities
        inv_part = np.linalg.pinv(np.matmul(H,np.matmul(covariance_pred,H.T))+self.Q) 

        # Kalman gain
        K = np.matmul(covariance_pred,np.matmul(H.T,inv_part))
        sensor_model = state_pred.copy()

        # Update sensor model with thrust and predicted velocity to find predicted acceleration
        drag_dir = -1 if state_pred[2,0] >= 0 else 1
        sensor_model[2,0] = (self.Tl + self.Tr + (drag_dir*DRAG*(state_pred[2,0]**2)))/MASS

        # Calculate corrected state and covariance
        self.state = state_pred + np.matmul(K,(self.sensor_data - sensor_model)) 
        self.covariance = np.matmul((np.eye(5) - np.matmul(K,H)),covariance_pred)
        
        # State is published to get_state topic
        msg = Float64MultiArray()
        msg.data = self.state.copy()
        self.pub.publish(msg)
        
    # Receives motor speed data and coverts into left and right thrust
    # Motor data is value between -1 and 1
    def motor_speed_callback(self,msg):

        # duty_l = 7.5 - 2.5*msg.data[0] #Center at 7.5 and capped at 5 and 10
        # duty_r = 7.5 - 2.5*msg.data[1]
        # Vl = (7.5-duty_l)/7.5*24
        # Vr = (7.5-duty_r)/7.5*24
        Vl = msg.data[0]*24
        Vr = msg.data[1]*24
        self.Tl = Vl * V_TO_N
        self.Tr = Vr * V_TO_N

    # Receives IMU data and saves it to sensor data vector
    # When initialized, will calculate accelerometer bias
    def imu_response_callback(self,msg):
        # covert heading quaternion back into radians
        (roll,pitch,yaw) = euler_from_quaternion([msg.orientation.x,msg.orientation.y,msg.orientation.z,msg.orientation.w])
        acc = msg.linear_acceleration.x
        omega = msg.angular_velocity.z

        # Reads the accelerometer and will get average if no thrust
        if self.Tl == 0 and self.Tr == 0 and self.bias_i < AVERAGE:
            self.acc_bias_data[self.bias_i] = acc
            self.bias_i += 1
        elif ((self.Tl != 0 or self.Tr != 0) and self.bias_i < AVERAGE) or self.bias_i == AVERAGE:
            elements = 0
            for e in self.acc_bias_data:
                self.acc_bias += e
                elements += 1
            if elements:
                self.acc_bias = self.acc_bias/elements
            self.bias_i = AVERAGE + 1

        # applies accelerometer bias
        acc -= self.acc_bias
        self.sensor_data[2:5,0] = [acc,yaw,omega]

    # Receives GPS data and will saves position to sensor data vector. 
    # Updates sensor noise with covariance from GPS
    def gps_response_callback(self,msg):
        fix_status = msg.status.status
        if fix_status >=0 :
            # Will save initial lat and lon to be averaged
            if self.avg_i < AVERAGE-1:
                fix = [math.radians(msg.latitude), math.radians(msg.longitude)]
                self.avg_pos[self.avg_i,:] = fix    
                self.avg_i += 1          

            # Calculates average lat and lon to serve as origin of coordinate system
            # Calculates initial covariance for position
            elif self.avg_i == AVERAGE-1:
                fix = [math.radians(msg.latitude), math.radians(msg.longitude)]
                self.avg_pos[self.avg_i,:] = fix
                avg_lat = self.avg_pos[:,0].mean(axis=0)
                avg_lon = self.avg_pos[:,1].mean(axis=0)
                self.first_fix = [avg_lat,avg_lon,math.cos(avg_lat)]
                gps_covariance = self.calc_covariance(msg)
                self.Q[0,0] = gps_covariance[0]
                self.Q[1,1] = gps_covariance[1]
                self.avg_i += 1
                self.gps_ready = True
            
            # If origin has already been set, calculates distance between current reading and origin
            # Updates position covariance
            else: 
                [dx,dy] = self.calc_dist(msg)
                gps_covariance = self.calc_covariance(msg)
                self.sensor_data[0:2,0] = [dx,dy]
                self.Q[0,0] = gps_covariance[0]
                self.Q[1,1] = gps_covariance[1]
        else:
            self.get_logger().info('No GPS Fix')

    # Calculates distance from current lat/lon to origin using equirectangular projection
    # dy is flipped because we want y axis to point west
    def calc_dist(self,fix):
        dx = W_RADIUS*(math.radians(fix.longitude) - self.first_fix[1])*self.first_fix[2]
        dy = W_RADIUS*(-math.radians(fix.latitude) + self.first_fix[0]) 
        return [dx,dy]
    
    # Calculates covariance of position using data from GPS
    # Uses CEP if not exactly known
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
    # Destroy the node when the emergency stop is triggered
    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()

# ROS Startup
def main():
    rclpy.init()

    kalman_state = KalmanState()

    rclpy.spin(kalman_state)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
