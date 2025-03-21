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
K =  0.35     # Complementary filter constant gain
E = 0.0001     # Complementary filter bias gain
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
        self.avg_data = MAX_DATA*np.ones((20,4)) #Acc, Gyro, X-heading, Y-heading

        self.csv_data = np.zeros((1500,5))
        self.i = 0

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

        self.pub = self.create_publisher(Imu, 'IMU_data', 10)
        self.timer_period = 0.02
        self.esp_timer_period = 0.2
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.esp_timer = self.create_timer(self.esp_timer_period, self.write_esp)
        self.prev_time = self.get_clock().now()
        self.heading = MAX_DATA
        self.gyro_bias = 0

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
        
        ang_vel = rate_gyr_x - self.gyro_bias

        #Calculate heading
        mag_heading = math.degrees(math.atan2(MAGy,MAGz))
        
        mag_heading += self.declination

        if self.heading == MAX_DATA:
            prev_heading = mag_heading #Initialize gyro to mag heading if not already
        else:
            prev_heading = math.degrees(math.atan2(self.avg_data[0,3],self.avg_data[0,2]))
        #Complementary filter 
        self.gyro_heading = prev_heading + ang_vel*self.timer_period
        if self.gyro_heading > 180: self.gyro_heading -= 360
        elif self.gyro_heading < -180: self.gyro_heading += 360

        innovation = mag_heading-self.gyro_heading
        heading = math.radians(self.gyro_heading + K*innovation)
        self.gyro_bias -= E/self.timer_period*innovation
        headingx = math.cos(heading) #split heading into unit vector to be averaged to prevent bounding errors
        headingy = math.sin(heading)

        self.acc_bias = 0.2 #experimentally found but should be updated #-0.2 for Z axis
        self.avg_data = np.roll(self.avg_data,axis=0,shift=1) #shift moving average data by one and then store current reading
        self.avg_data[0,0] = (ACCy * 0.244/1000 * 9.81) + self.acc_bias
        self.avg_data[0,1] = ang_vel
        self.avg_data[0,2] = headingx
        self.avg_data[0,3] = headingy

        self.acceleration, self.omega, headingx, headingy = self.calc_avg()
        self.heading = math.degrees(math.atan2(headingy,headingx))
        if self.i < 1500:
            self.csv_data[self.i,:] = [ang_vel, self.gyro_heading,mag_heading,math.degrees(heading),self.heading]
            self.i += 1
        elif self.i == 1500:
            np.savetxt("Heading_data.csv",self.csv_data,delimiter = ',')
            print("got here")
            self.i += 1
        self.get_logger().info("Gyro: %5.3f  Mag: %5.3f  CF: %5.3f" %(self.gyro_heading,mag_heading,self.heading))

        imu_msg = Imu()
        imu_msg.header.frame_id = 'imu_pub'
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.angular_velocity.x = 0.0
        imu_msg.angular_velocity.y = 0.0
        imu_msg.angular_velocity.z = math.radians(self.omega)
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
        # self.write_esp() #waiting until we have a plan to interpret

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
        data = struct.pack('Bf',0,self.heading) #Sending 0 means that the data is gyro related, sends the angular vel in rad/s
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
