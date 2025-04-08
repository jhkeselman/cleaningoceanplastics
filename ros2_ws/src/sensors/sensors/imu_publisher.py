import rclpy
from rclpy.node import Node


from std_msgs.msg import String, Bool
from sensor_msgs.msg import Imu
from tf_transformations import quaternion_from_euler
from geometry_msgs.msg import Quaternion

import math
import sys
import time
import struct
import numpy as np
import smbus
import struct

from .utils.IMU_lib import * #BerryIMU library containing configuration of acc, gryo, and mag chips

RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
DECLINATION = math.degrees(-214.1/1000) # Magnetic declination calculated at Worcester (-214 milliradians)
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
K =  0.35     # Complementary filter constant gain
E = 0.0001     # Complementary filter bias gain
MAX_DATA = 32767 # Arbitrary value to ignore when calculating average


# This node reads linear acceleration, angular velocity, and heading from the onboard IMU
# Heading data is processed to calibrate for hard iron distortion along with a complementary filter with gyro
# All data is run through moving average of previous 20 values to reduce random noise
# Heading data is sent to ESP for motor drift control over I2C
# Publishers: 'IMU_data'
# Subscribers: 'emergency_stop'
class IMUPub(Node):

    def __init__(self):
        super().__init__('IMU_publisher')

        # Initialize IMU
        detectIMU()     
        # Detect if BerryIMU is connected.
        if(BerryIMUversion == 99):
            print(" No BerryIMU found... exiting ")
            sys.exit()
        # Initialise the accelerometer, gyroscope and magnetometer
        initIMU()       

        self.get_logger().info("IMU initialized...")

        # I2C address of ESP32
        self.I2C_address = 0x55 
        self.bus = smbus.SMBus(1)       


        # self.magXmin = -1089 #Previous Calibration values of magnetometer at +/- 8 gauss
        # self.magYmin = -1203
        # self.magZmin = -901
        # self.magXmax = 1279
        # self.magYmax = 498
        # self.magZmax = 808


        # Calibration values of magnetometer at +/- 16 gauss
        self.magXmin = -627 
        self.magYmin = -449
        self.magZmin = -250
        self.magXmax = -568
        self.magYmax = -77
        self.magZmax = 202

        # Moving average data of Acc, Gyro, X-heading, Y-heading
        self.avg_data = MAX_DATA*np.ones((20,4)) 

        # Subscription to emergency stop topic
        # If emergency stop is triggered, the node will be destroyed
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

        # Timer to check IMU data at 50 Hz
        self.timer_period = 0.02
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        # Publisher for IMU data
        # Message type: Imu
        self.pub = self.create_publisher(Imu, 'IMU_data', 10)
        
        # Timer to send heading data to ESP at 50 Hz
        self.esp_timer_period = 0.02
        self.esp_timer = self.create_timer(self.esp_timer_period, self.write_esp)

        # Flag heading to be updated upon first run
        self.heading = MAX_DATA

        # Initialize gyro bias to be 0 at beginning
        self.gyro_bias = 0


        # self.calibrate_Mag()

    # Destroy the node when the emergency stop is triggered
    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()


    # NOT USED IN LOOP
    # Function to continuously measure min and max magnetometer readings
    # Spin the IMU (or electronics box) continuosly to gather data
    def calibrate_Mag(self): 
        self.magXmin = MAX_DATA #Resets calibrated values
        self.magYmin = MAX_DATA
        self.magZmin = MAX_DATA
        self.magXmax = -MAX_DATA
        self.magYmax = -MAX_DATA
        self.magZmax = -MAX_DATA

        while True:
            MAGx = readMAGx()
            MAGy = readMAGy()
            MAGz = readMAGz()

            if MAGx > self.magXmax:
                self.magXmax = MAGx
            if MAGy > self.magYmax:
                self.magYmax = MAGy
            if MAGz > self.magZmax:
                self.magZmax = MAGz

            if MAGx < self.magXmin:
                self.magXmin = MAGx
            if MAGy < self.magYmin:
                self.magYmin = MAGy
            if MAGz < self.magZmin:
                self.magZmin = MAGz

            time.sleep(0.025)
        

    # Reads and processes all IMU data
    def timer_callback(self):
        # Read the accelerometer,gyroscope and magnetometer raw values
        ACCx = readACCx()
        ACCy = readACCy()
        ACCz = readACCz()
        GYRx = readGYRx()
        GYRy = readGYRy()
        GYRz = readGYRz()
        MAGx = readMAGx()
        MAGy = readMAGy()
        MAGz = readMAGz()
        
        #Shift magnetometer readings back to origin to componsate for hard iron distortion
        MAGx -= (self.magXmin + self.magXmax) /2 
        MAGy -= (self.magYmin + self.magYmax) /2
        MAGz -= (self.magZmin + self.magZmax) /2

        # Convert Gyro raw to degrees per second
        # Current gryoscope is mounted with yaw (x) downwards
        rate_gyr_x =  -GYRx * G_GAIN 
        rate_gyr_y =  GYRy * G_GAIN
        rate_gyr_z =  GYRz * G_GAIN
        
        # Subtract bias from gyro data
        ang_vel = rate_gyr_x - self.gyro_bias

        # Calculate heading from Y and Z magnetometer readings
        # Atan2 used so north is 0, west is 90 degrees
        mag_heading = math.degrees(math.atan2(MAGz,-MAGy))

        # Account for magnetic declination
        mag_heading += DECLINATION    
    
        
        ''' COMPLEMENTARRY FILTER '''

        # Initialize gyro to mag heading if not already
        # Otherwise uses previous heading value
        if self.heading == MAX_DATA:
            prev_heading = mag_heading 
        else:
            prev_heading = math.degrees(math.atan2(self.avg_data[0,3],self.avg_data[0,2]))

        # Add heading change according to gyroscope to previous fused heading
        self.gyro_heading = prev_heading + ang_vel*self.timer_period

        # Innovation is the error between the mag and gyro heading
        # Must be bound between -pi and pi to prevent errors
        innovation = mag_heading-self.gyro_heading
        if innovation > 180: innovation -= 360
        elif innovation < -180: innovation += 360

        # Fused heading is calculated using gain term K
        heading = math.radians(self.gyro_heading + K*innovation)

        # Bias in gyroscope is accounted for next loop
        self.gyro_bias -= E/self.timer_period*innovation

        # The heading is split into unit vectors to be averaged to prevent bounding errors
        headingx = math.cos(heading) 
        headingy = math.sin(heading)

        # Shift moving average data by one
        self.avg_data = np.roll(self.avg_data,axis=0,shift=1) 
        
        # Linear acceleration in robot's x direction is converted from mg to m/s^2
        # All current sensor data is stored in matrix
        self.avg_data[0,0] = (ACCy * 0.244/1000 * 9.81)
        self.avg_data[0,1] = rate_gyr_x
        self.avg_data[0,2] = headingx
        self.avg_data[0,3] = headingy

        # Moving average values are returned from self.calc_avg()
        self.acceleration, self.omega, headingx, headingy = self.calc_avg()

        # Overall heading needs to be recalculated from averaged unit vectors
        self.heading = math.atan2(headingy,headingx)
        # print(self.heading, math.radians(self.omega))

        #ROS Imu message is constructed using sensor data
        imu_msg = Imu()
        imu_msg.header.frame_id = 'imu_pub'
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.angular_velocity.x = 0.0
        imu_msg.angular_velocity.y = 0.0
        imu_msg.angular_velocity.z = math.radians(self.omega)

        # Heading is stored as quaternion value
        q = quaternion_from_euler(0,0,self.heading)
        imu_msg.orientation.x = q[0]
        imu_msg.orientation.y = q[1]
        imu_msg.orientation.z = q[2]
        imu_msg.orientation.w = q[3]
        imu_msg.linear_acceleration.x = self.acceleration
        imu_msg.linear_acceleration.y = (ACCx * 0.244/1000 * 9.81)
        imu_msg.linear_acceleration.z = (ACCz * 0.244/1000 * 9.81)

        # imu_msg.angular_velocity_covariance = [(70/1000)**2,0,0,0,0,0,0,0,0] #covariance based on sensitivity of sensors from data sheet
        # imu_msg.linear_acceleration_covariance = [(0.244/1000*9.81)**2,0,0,0,0,0,0,0,0]
        # imu_msg.orientation_covariance = [(0.1**2),0,0,0,0,0,0,0,0] #sort of a guess based in radians

        # Imu data is published to IMU_data topic
        self.pub.publish(imu_msg)

        # Imu data is then written to esp
        self.write_esp() 

        # print(MAGx, MAGy, MAGz, self.heading)


    # Calculates average of previous 20 values for acc, ang_vel, heading_x, and heading_y
    # If any data points are MAX_DATA they are excluded from the average
    def calc_avg(self):
        avg_data = np.zeros(4)
        elements = np.zeros(4)
        for i in range(4):
            for n in self.avg_data[:,i]:
                if n != MAX_DATA:
                    avg_data[i] += n
                    elements[i] += 1
            if elements[i]:
                avg_data[i] = avg_data[i]/elements[i]
        return avg_data
    
    # Sends heading data to ESP over I2C
    def write_esp(self):
        # Sending 0 means that the data is gyro related, sends the heading in rad
        data = struct.pack('if',0,self.heading) 
        byte_list = list(data)
        try:
            self.bus.write_i2c_block_data(self.I2C_address, 0, byte_list)
        except:
            self.get_logger().info("Failed to send value")
        
        
        
        # NOTE DEBUG: Read the motor values
        # try:
        #     data = self.bus.read_i2c_block_data(self.I2C_address, 0, 8)
        #     currentLeft, currentRight = struct.unpack('ff', bytes(data)) # 8 bytes of data (2 floats)
        #     currentLeft, currentRight = round(currentLeft, 2), round(currentRight, 2)
        #     # print(currentLeft, currentRight, self.heading)
        # except:
        #     self.get_logger().info("Failed to read value")

# ROS Startup
def main(args=None):
    rclpy.init(args=args)

    imu_publisher = IMUPub()

    rclpy.spin(imu_publisher)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
