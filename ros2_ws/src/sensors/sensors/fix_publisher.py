import serial
import time
import rclpy
import os
import math
from gps import *


from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, NavSatStatus
from std_msgs.msg import Bool

class GPSFixPub(Node):
    def __init__(self):
        super().__init__('gps_fix_publisher')
        
        self.gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE) 
        self.create_timer(0.05,self.read_gpsd)

        self.pub = self.create_publisher(NavSatFix, 'get_GPS', 10)

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )
        
        self.fix = NavSatFix()
        self.fix.header.frame_id = 'fix_pub'
    
    def parse_gpsd(self,report):
        if report['class'] == 'TPV':
            fix = getattr(report,'mode',0)
            if fix > 1: self.fix.status.status = NavSatStatus.STATUS_FIX
            else: 
                self.fix.status.status = NavSatStatus.STATUS_NO_FIX
                self.fix.position_covariance_type = NavSatFix.COVARIANCE_TYPE_UNKNOWN
                return
            self.fix.latitude = getattr(report,'lat',0.0)
            self.fix.longitude = getattr(report,'lon',0.0)
            current_time = self.get_clock().now().to_msg()
            self.fix.header.stamp = current_time
            self.pub.publish(self.fix)
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
        elif report['class'] == 'GST':
            self.fix.position_covariance[0] = getattr(report,'lon',4.0)
            self.fix.position_covariance[4] = getattr(report,'lat',4.0)
            self.fix.position_covariance_type = NavSatFix.COVARIANCE_TYPE_DIAGONAL_KNOWN

    def read_gpsd(self):
        report = self.gpsd.next()
        self.parse_gpsd(report)

    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    gps_pub = GPSFixPub()

    rclpy.spin(gps_pub)

    rclpy.shutdown()
