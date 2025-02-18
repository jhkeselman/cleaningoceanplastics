from services.srv import IMUData

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import math
import datetime
import sys
import time

from .IMU_lib import *

RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA =  0.40      # Complementary filter constant

class IMUService(Node):

    def __init__(self):
        super().__init__('IMU_service')
        self.srv = self.create_service(IMUData, 'get_IMU_data', self.get_data_callback)
        timer_period = 0.02
        self.timer = self.create_timer(timer_period, self.timer_callback)
        

        # Initialize IMU
        detectIMU()     #Detect if BerryIMU is connected.
        if(BerryIMUversion == 99):
            print(" No BerryIMU found... exiting ")
            sys.exit()
        initIMU()       #Initialise the accelerometer, gyroscope and compass
        self.a = datetime.datetime.now()

        self.get_logger().info("IMU initialized...")

        #self.calibrate(500)
        self.biasz = 0.0

        init_magX = readMAGx()
        init_magY = readMAGy()
        self.gyroXangle = 0.0
        self.gyroYangle = 0.0
        init_heading = 180 * math.atan2(init_magY,init_magX)/M_PI
        if init_heading < 0:
            init_heading += 360
        self.gyroZangle = init_heading
        print(self.gyroZangle)
        self.CFangleX = 0.0
        self.CFangleY = 0.0
        self.heading = 0.0

        self.magXmin = 309
        self.magYmin = -2350
        self.magZmin = -1496
        self.magXmax = 2684
        self.magYmax = 753
        self.magZmax = 1770


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

        self.omega = rate_gyr_z #MAY NEED TO ACCOUNT FOR BIAS

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
        heading = 180 * math.atan2(MAGy,MAGx)/M_PI

        #Only have our heading between 0 and 360
        if heading < 0:
            heading += 360

        self.acceleration = ACCz * 0.244/1000 * 9.81 #conversion between raw accelerometer and m/s^s

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

        K = 0.9
        B = 0.001
        CF_heading = K*(self.gyroZangle-self.biasz)+ (1-K)*heading
        if CF_heading < 0:
            CF_heading += 360
        elif CF_heading > 360:
            CF_heading -= 360
        self.biasz += B*(CF_heading-self.gyroZangle)
        self.heading = tiltCompensatedHeading
#        print("#  CFheading Angle %5.2f   Gyro Angle %5.2f  Bias %5.2f  Mag %5.2f#" % (CF_heading, self.gyroZangle, self.biasz, tiltCompensatedHeading))

    def calibrate(self,readings):
        biasx = 0
        biasy = 0
        biasz = 0
        for i in range(readings):
            biasx += readGYRx() * G_GAIN * 0.02
            biasy += readGYRy() * G_GAIN * 0.02
            biasz += readGYRz() * G_GAIN * 0.02
            time.sleep(0.02)
        
        self.biasx = biasx/readings
        self.biasy = biasy/readings
        self.biasz = biasz/readings

    def get_data_callback(self, request, response):

        response.heading = self.heading #UPDATE
        response.acceleration = self.acceleration
        response.omega = self.omega
        self.get_logger().info('Incoming request')

        return response


def main(args=None):
    rclpy.init(args=args)

    imu_service = IMUService()

    rclpy.spin(imu_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
