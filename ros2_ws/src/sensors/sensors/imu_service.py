from services.srv import IMUData

import rclpy
from rclpy.node import Node


from std_msgs.msg import String, Bool

import math
import datetime
import sys
import time
import numpy as np

from .IMU_lib import *

RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA =  0.40      # Complementary filter constant
GYRO_MAX = 32767

class IMUService(Node):

    def __init__(self):
        super().__init__('IMU_service')

        

        # Initialize IMU
        detectIMU()     #Detect if BerryIMU is connected.
        if(BerryIMUversion == 99):
            print(" No BerryIMU found... exiting ")
            sys.exit()
        initIMU()       #Initialise the accelerometer, gyroscope and compass
        self.a = datetime.datetime.now()

        self.get_logger().info("IMU initialized...")

        self.biasz = 0.0

        init_magZ = readMAGz()
        init_magY = readMAGy()
        self.gyroXangle = 0.0
        self.gyroYangle = 0.0
        init_heading = 180 * math.atan2(init_magY,init_magZ)/M_PI
        if init_heading < 0:
            init_heading += 360
        self.gyroZangle = init_heading
        #print(self.gyroZangle)
        self.CFangleX = 0.0
        self.CFangleY = 0.0
        self.heading = 0.0

        self.declination = -214.1/1000 * RAD_TO_DEG #calculated at Worcester (-214 milliradians)

        # self.magXmin = 32767
        # self.magYmin = 32767
        # self.magZmin = 32767
        # self.magXmax = -32767
        # self.magYmax = -32767
        # self.magZmax = -32767
        # self.calibrate_Mag()

        #print((" magXmin  %i  magYmin  %i  magZmin  %i  ## magXmax  %i  magYmax  %i  magZmax %i  " %(self.magXmin,self.magYmin,self.magZmin,self.magXmax,self.magYmax,self.magZmax)))

        self.magXmin = -1261 #Previous Calibration values of magnetometer
        self.magYmin = -2286
        self.magZmin = -2048
        self.magXmax = 2465
        self.magYmax = 1529
        self.magZmax = 1822

        self.gyro_avg_data = GYRO_MAX*np.ones(20)

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

        self.srv = self.create_service(IMUData, 'get_IMU_data', self.get_data_callback)
        timer_period = 0.02
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()


    def calibrate_Mag(self):
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

        MAGx -= (self.magXmin + self.magXmax) /2
        MAGy -= (self.magYmin + self.magYmax) /2
        MAGz -= (self.magZmin + self.magZmax) /2

        ##Calculate loop Period(LP). How long between Gyro Reads
        b = datetime.datetime.now() - self.a
        self.a = datetime.datetime.now()
        LP = b.microseconds/(1000000*1.0)
        outputString = "Loop Time %5.2f " % ( LP )

        #Convert Gyro raw to degrees per second
        rate_gyr_x =  GYRx * G_GAIN
        rate_gyr_y =  GYRy * G_GAIN
        rate_gyr_z =  GYRz * G_GAIN

        #self.omega = rate_gyr_z*M_PI/180 #MAY NEED TO ACCOUNT FOR BIAS
        
        self.gyro_avg_data = np.roll(self.gyro_avg_data,1) #shift moving average data by one and then store current reading
        self.gyro_avg_data[0] = rate_gyr_x*M_PI/180
        self.omega = self.calc_avg_gyro()

        #Calculate the angles from the gyro.
        self.gyroXangle+=rate_gyr_x*LP
        self.gyroYangle+=rate_gyr_y*LP
        self.gyroZangle+=rate_gyr_z*LP

        #Convert Accelerometer values to degrees
        AccXangle =  (math.atan2(ACCy,ACCz)*RAD_TO_DEG)
        AccYangle =  (math.atan2(ACCz,ACCx)+M_PI)*RAD_TO_DEG

        #convert the values to -180 and +180
        if AccYangle > 90:
            AccYangle -= 270.0
        else:
            AccYangle += 90.0

        #Complementary filter used to combine the accelerometer and gyro values.
        self.CFangleX=AA*(self.CFangleX+rate_gyr_x*LP) +(1 - AA) * AccXangle
        self.CFangleY=AA*(self.CFangleY+rate_gyr_y*LP) +(1 - AA) * AccYangle

        #Calculate heading
        heading = 180 * math.atan2(MAGy,MAGz)/M_PI
        #heading += self.declination

        #Only have our heading between 0 and 360
        if heading < 0:
            heading += 360.0

        self.acc_bias = 0.4 #experimentally found but should be updated #-0.2 for Z axis
        self.acceleration = (ACCy * 0.244/1000 * 9.81) + self.acc_bias #conversion between raw accelerometer and m/s^s

        ####################################################################
        ###################Tilt compensated heading#########################
        ####################################################################
        #Normalize accelerometer raw values.
        accXnorm = ACCx/math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)
        accYnorm = ACCy/math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)

        #Calculate pitch and roll
        pitch = math.asin(accXnorm)
        roll = -math.asin(accYnorm/math.cos(pitch))

        #Calculate the new tilt compensated values
        #X compensation
        magXcomp = MAGx*math.cos(pitch)+MAGz*math.sin(pitch)
        magYcomp = MAGx*math.sin(roll)*math.sin(pitch)+MAGy*math.cos(roll)-MAGz*math.sin(roll)*math.cos(pitch)

        #Calculate tilt compensated heading
        tiltCompensatedHeading = 180 * math.atan2(magYcomp,magXcomp)/M_PI

        if tiltCompensatedHeading < 0:
            tiltCompensatedHeading += 360


        ##################### END Tilt Compensation ########################

        '''
        Fusing gyroscope and magnetometer data
        '''

        # K = 0.9
        # B = 0.001
        # CF_heading = K*(self.gyroZangle-self.biasz)+ (1-K)*heading
        # if CF_heading < 0:
        #     CF_heading += 360
        # elif CF_heading > 360:
        #     CF_heading -= 360
        # self.biasz += B*(CF_heading-self.gyroZangle)
        #self.heading = tiltCompensatedHeading
        self.heading = heading
#        print("#  CFheading Angle %5.2f   Gyro Angle %5.2f  Bias %5.2f  Mag %5.2f#" % (CF_heading, self.gyroZangle, self.biasz, tiltCompensatedHeading))

    def calc_avg_gyro(self):
        avg_omega = 0
        elements = 0
        for n in self.gyro_avg_data:
            if n != GYRO_MAX:
                avg_omega += n
                elements += 1
        if elements:
            avg_omega = avg_omega/elements
        return avg_omega
        

    def get_data_callback(self, request, response):

        response.heading = self.heading 
        response.acceleration = self.acceleration
        response.omega = self.omega
        self.get_logger().info('Incoming IMU request')

        return response


def main(args=None):
    rclpy.init(args=args)

    imu_service = IMUService()

    rclpy.spin(imu_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
