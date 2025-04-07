import serial
import time
import rclpy
import os
import math
from gps import *


from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, NavSatStatus
from std_msgs.msg import Bool

# This node reads and publishes GPS information for the robot.
# Using GPSD, the node interprets lat,long, and uncertainty data and publishes
# Publishers: 'get_GPS'
# Subscribers: 'emergency_stop'

class GPSFixPub(Node):
    def __init__(self):
        super().__init__('gps_fix_publisher')
        
        # Creates GPSD object to read data
        self.gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE) 
        
        # Timer to read GPS data
        self.create_timer(0.05,self.read_gpsd)

        # Publisher for GPS data
        # Message type: NavSatFix
        self.pub = self.create_publisher(NavSatFix, 'get_GPS', 10)

        # Subscription to emergency stop topic
        # If emergency stop is triggered, the node will be destroyed
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

        # Creates fix object to be modified with each new data point
        self.fix = NavSatFix()
        self.fix.header.frame_id = 'fix_pub'

    
    # Parse GPS data using GPSD. GPSD returns a JSON object to be interpeted
    # TPV contains lat, long data or if no fix is found
    # SKY is currently only being used to say if covariance ins't directly known.
    # GST contains known standard deviation of lat, long in meters
    def parse_gpsd(self,report):
        # TIME POSITION VELOCITY REPORT
        if report['class'] == 'TPV': 
            fix = getattr(report,'mode',0)
            if fix > 1: self.fix.status.status = NavSatStatus.STATUS_FIX
            else: 
                # Will return if no fix found
                self.fix.status.status = NavSatStatus.STATUS_NO_FIX 
                self.fix.position_covariance_type = NavSatFix.COVARIANCE_TYPE_UNKNOWN
                return
            self.fix.latitude = getattr(report,'lat',0.0)
            self.fix.longitude = getattr(report,'lon',0.0)
            current_time = self.get_clock().now().to_msg()
            self.fix.header.stamp = current_time
            # Only publishes when new lat,long data is sent
            self.pub.publish(self.fix) 

        # SKY REPORT (contains dilution of precision data)
        # CURRENTLY ONLY BEING USED TO FLAG APPROXIMATED COVARIANCE NOT ACTUALLY USED IN CALCULATIONS
        elif report['class'] == 'SKY': 
            if hasattr(report,'xdop') and hasattr(report, 'ydop'):
                xdop = getattr(report,'xdop')
                ydop = getattr(report,'ydop')
                self.fix.position_covariance[0] = xdop
                self.fix.position_covariance[4] = ydop
            else:
                hdop = getattr(report,'hdop',2.0)
                self.fix.position_covariance[0] = hdop
                self.fix.position_covariance[4] = hdop
            self.fix.position_covariance_type = NavSatFix.COVARIANCE_TYPE_APPROXIMATED

        # GST Pseudorange noise report (gives std for lat, long directly)
        elif report['class'] == 'GST': 
            self.fix.position_covariance[0] = getattr(report,'lon',4.0)
            self.fix.position_covariance[4] = getattr(report,'lat',4.0)
            self.fix.position_covariance_type = NavSatFix.COVARIANCE_TYPE_DIAGONAL_KNOWN


    # Read GPS on timer
    def read_gpsd(self):
        report = self.gpsd.next()
        self.parse_gpsd(report)

    # Destroy the node when the emergency stop is triggered
    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()

# ROS STARTUP
def main(args=None):
    rclpy.init(args=args)
    gps_pub = GPSFixPub()

    rclpy.spin(gps_pub)

    rclpy.shutdown()