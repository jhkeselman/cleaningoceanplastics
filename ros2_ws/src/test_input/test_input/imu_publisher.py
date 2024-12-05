import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import math
import datetime
import sys

# sys.path.append('./test_input/test_input/')

from .IMU_lib import *

RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA =  0.40      # Complementary filter constant

class IMU(Node):

    def __init__(self):
        super().__init__('imu')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.gyroXangle = 0.0
        self.gyroYangle = 0.0
        self.gyroZangle = 0.0
        self.CFangleX = 0.0
        self.CFangleY = 0.0

        # Initialize IMU
        detectIMU()     #Detect if BerryIMU is connected.
        if(BerryIMUversion == 99):
            print(" No BerryIMU found... exiting ")
            sys.exit()
        initIMU()       #Initialise the accelerometer, gyroscope and compass
        self.a = datetime.datetime.now()

        self.get_logger().info("IMU initialized...")

        self.prev_gyr_heading = 180 * math.atan2(readMAGy,readMAGx())/M_PI
   
    def get_data(self):
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

        ##Calculate loop Period(LP). How long between Gyro Reads
        b = datetime.datetime.now() - self.a
        self.a = datetime.datetime.now()
        LP = b.microseconds/(1000000*1.0)
        outputString = "Loop Time %5.2f " % ( LP )

        #Convert Gyro raw to degrees per second
        rate_gyr_x =  GYRx * G_GAIN
        rate_gyr_y =  GYRy * G_GAIN
        rate_gyr_z =  GYRz * G_GAIN

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

        gyr_heading = self.prev_gyr_heading + rate_gyr_z*LP
        K = 0.9
        CF_heading = K*gyr_heading + (1-K)*tiltCompensatedHeading
        self.prev_gyr_heading = gyr_heading #should this update to the CF heading? or just always keep the gyro heading?


        if 0:                       #Change to '0' to stop showing the angles from the accelerometer
            outputString += "#  ACCX Angle %5.2f ACCY Angle %5.2f  #  " % (AccXangle, AccYangle)

        if 0:                       #Change to '0' to stop  showing the angles from the gyro
            outputString +="\t# GRYX Angle %5.2f  GYRY Angle %5.2f  GYRZ Angle %5.2f # " % (self.gyroXangle,self.gyroYangle,self.gyroZangle)

        if 1:                       #Change to '0' to stop  showing the angles from the complementary filter
            outputString +="\t#  CFangleX Angle %5.2f   CFangleY Angle %5.2f  #" % (self.CFangleX,self.CFangleY)

        if 1:                       #Change to '0' to stop  showing the heading
            outputString +="\t# HEADING %5.2f  tiltCompensatedHeading %5.2f #" % (heading,tiltCompensatedHeading)

        if 1:                       #Change to '0' to stop  showing the heading
            outputString +="\t# CFHeading %5.2f #" % (CF_heading)

        return outputString

    def timer_callback(self):
        msg = String()
        msg.data = self.get_data() 
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    imu = IMU()

    rclpy.spin(imu)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
