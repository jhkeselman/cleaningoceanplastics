import rclpy
from rclpy.node import Node


from std_msgs.msg import String, Bool
from sensor_msgs.msg import Imu
from tf_transformations import quaternion_from_euler
from geometry_msgs.msg import Quaternion

import math
import datetime
import sys
import time
import struct
import numpy as np
import smbus

from .IMU_lib import *

RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA =  0.40      # Complementary filter constant
MAX_DATA = 32767 

class IMUPub(Node):

    def __init__(self):
        super().__init__('IMU_publisher')

        # Initialize IMU
        detectIMU()     #Detect if BerryIMU is connected.
        if(BerryIMUversion == 99):
            print(" No BerryIMU found... exiting ")
            sys.exit()
        initIMU()       #Initialise the accelerometer, gyroscope and compass
        self.a = datetime.datetime.now()

        self.get_logger().info("IMU initialized...")

        self.I2C_address = 0x55 #I2C address of ESP32
        self.bus = smbus.SMBus(1)       

        self.heading = 0.0

        self.declination = -214.1/1000 * RAD_TO_DEG #calculated at Worcester (-214 milliradians)

        # self.magXmin = -1261 #Previous Calibration values of magnetometer at +/- 8 gauss
        # self.magYmin = -2286
        # self.magZmin = -2048
        # self.magXmax = 2465
        # self.magYmax = 1529
        # self.magZmax = 1822

        self.magXmin = -1089 #Previous Calibration values of magnetometer at +/- 8 gauss
        self.magYmin = -1203
        self.magZmin = -901
        self.magXmax = 1279
        self.magYmax = 498
        self.magZmax = 808

        self.gyro_avg_data = MAX_DATA*np.ones(20)
        self.acc_avg_data = MAX_DATA*np.ones(20)
        self.mag_avg_data = MAX_DATA*np.ones(20)
        self.avg_data = MAX_DATA*np.ones((20,3))

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

        self.pub = self.create_publisher(Imu, 'IMU_data', 10)
        timer_period = 0.02
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.prev_time = self.get_clock().now()
        self.gyro_heading = 0

    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()


    def calibrate_Mag(self): #NOT USED, BUT TO CALIBRATE AGAINST HARD IRON DISTORTION
        for i in range(200):
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
        


    def timer_callback(self):
        #Read the accelerometer,gyroscope and magnetometer values
        ACCx = readACCx()
        ACCy = readACCy()
        ACCz = readACCz()
        GYRx = readGYRx()
        GYRy = readGYRy()
        GYRz = readGYRz()
        MAGx = readMAGx()
        MAGy = readMAGy()
        MAGz = readMAGz()

        MAGx -= (self.magXmin + self.magXmax) /2 #SHIFT MAGNETOMETER BACK TO ORIGIN to componsate for hard iron distortion
        MAGy -= (self.magYmin + self.magYmax) /2
        MAGz -= (self.magZmin + self.magZmax) /2

        #Convert Gyro raw to degrees per second
        rate_gyr_x =  -GYRx * G_GAIN #current gryoscope is mounted with yaw (x) downwards
        rate_gyr_y =  GYRy * G_GAIN
        rate_gyr_z =  GYRz * G_GAIN
        
        self.gyro_avg_data = np.roll(self.gyro_avg_data,1) #shift moving average data by one and then store current reading
        self.avg_data[:,0] = np.roll(self.avg_data[:,0],1)
        self.gyro_avg_data[0] = rate_gyr_x*M_PI/180
        self.avg_data[0,0] = rate_gyr_x*M_PI/180
        self.omega= self.calc_avg_gyro()

        #Calculate heading
        heading = 180 * math.atan2(MAGy,MAGz)/M_PI
        
        heading += self.declination
        self.avg_data[:,1] = np.roll(self.avg_data[:,1],1)
        self.avg_data[0,1] = heading

        # #Only have our heading between 0 and 360
        # if heading < 0:
        #     heading += 360.0

        self.acc_bias = 0.2 #experimentally found but should be updated #-0.2 for Z axis
        self.acc_avg_data[0] = (ACCy * 0.244/1000 * 9.81) + self.acc_bias #conversion between raw accelerometer and m/s^s
        self.acceleration = self.calc_avg_acc()
        self.avg_data[:,2] = np.roll(self.avg_data[:,2],1)
        self.avg_data[0,2] = (ACCy * 0.244/1000 * 9.81) + self.acc_bias

        print(self.calc_avg())

        imu_msg = Imu()
        imu_msg.header.frame_id = 'imu_pub'
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.angular_velocity.x = 0.0
        imu_msg.angular_velocity.y = 0.0
        imu_msg.angular_velocity.z = self.omega
        q = quaternion_from_euler(0,0,math.radians(heading))
        imu_msg.orientation.x = q[0]
        imu_msg.orientation.y = q[1]
        imu_msg.orientation.z = q[2]
        imu_msg.orientation.w = q[3]
        imu_msg.linear_acceleration.x = self.acceleration
        imu_msg.linear_acceleration.y = (ACCx * 0.244/1000 * 9.81)
        imu_msg.linear_acceleration.z = (ACCz * 0.244/1000 * 9.81)
        imu_msg.angular_velocity_covariance = [(70/1000)**2,0,0,0,0,0,0,0,0] #covariance based on sensitivity of sensors from data sheet
        imu_msg.linear_acceleration_covariance = [(0.244/1000*9.81)**2,0,0,0,0,0,0,0,0]
        imu_msg.orientation_covariance = [(0.1**2),0,0,0,0,0,0,0,0] #sort of a guess based in radians
        self.pub.publish(imu_msg)
        #self.write_esp() #waiting until we have a plan to interpret

    def calc_avg(self):
        avg_data = np.zeros(3)
        elements = np.zeros(3)
        for i in range(3):
            for n in self.avg_data[:,i]:
                if n != MAX_DATA:
                    avg_data[i] += n
                    elements[i] += 1
            if elements[i]:
                avg_data[i] = avg_data[i]/elements[i]
        return avg_data

    def calc_avg_gyro(self):
        avg_omega = 0.0
        elements = 0
        for n in self.gyro_avg_data:
            if n != MAX_DATA:
                avg_omega += n
                elements += 1
        if elements:
            avg_omega = avg_omega/elements
        return avg_omega
    
    def calc_avg_acc(self):
        avg_acc = 0.0
        elements = 0
        for n in self.acc_avg_data:
            if n != MAX_DATA:
                avg_acc += n
                elements += 1
        if elements:
            avg_acc = avg_acc/elements
        return avg_acc
    
    def write_esp(self):
        data = struct.pack('if',0,self.omega) #Sending 0 means that the data is gyro related, sends the angular vel in rad/s
        byte_list = list(data)
        try:
            self.bus.write_i2c_block_data(self.I2C_address, 0, byte_list)
        except:
            self.get_logger().info("Failed to send value")


def main(args=None):
    rclpy.init(args=args)

    imu_publisher = IMUPub()

    rclpy.spin(imu_publisher)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
