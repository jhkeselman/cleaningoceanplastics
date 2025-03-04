import serial
import time
import rclpy
import os
import math
from gps import *

from ament_index_python.packages import get_package_share_directory
from rclpy.executors import SingleThreadedExecutor

from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, NavSatStatus, TimeReference
from std_msgs.msg import Bool
from .checksum_utils import check_nmea_checksum
from .parser import *
from services.srv import GPSdata

class GPSFixDriver(Node):
    def __init__(self):
        super().__init__('gps_fix_driver')
        
        self.gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE) 
        self.create_timer(0.05,self.read_gpsd)

        self.fix_service = self.create_service(GPSdata, 'get_GPS_fix', self.data_callback)
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )
        
        self.fix = NavSatFix()
    
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

    """Helper method for getting the frame_id with the correct TF prefix"""
    def get_frame_id(self):
        frame_id = self.declare_parameter('frame_id', 'gps').value
        prefix = self.declare_parameter('tf_prefix', '').value
        if len(prefix):
            return '%s/%s' % (prefix, frame_id)
        
        self.frame_id = frame_id
        return frame_id

    def read_gpsd(self):
        current_time = self.get_clock().now().to_msg()
        self.fix.header.stamp = current_time
        self.fix.header.frame_id = self.frame_id
        report = self.gpsd.next()
        self.parse_gpsd(report)

    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()
    
    def data_callback(self,request,response):
        self.get_logger().info('Incoming request')
        response.fix = self.fix

        return response


def main(args=None):
    rclpy.init(args=args)
    driver = GPSFixDriver()

    frame_id = driver.get_frame_id()

    rclpy.spin(driver)

    rclpy.shutdown()
