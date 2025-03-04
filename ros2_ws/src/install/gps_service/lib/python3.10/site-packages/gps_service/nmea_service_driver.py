import serial
import time
import rclpy
import os

from .driver import Ros2NMEADriver
from ament_index_python.packages import get_package_share_directory

from rclpy.executors import SingleThreadedExecutor



def main(args=None):
    rclpy.init(args=args)

    driver = Ros2NMEADriver()
    executor = SingleThreadedExecutor()
    executor.add_node(driver)
    frame_id = driver.get_frame_id()

    serial_port = driver.declare_parameter('port', '/dev/ttyAMA0').value
    serial_baud = driver.declare_parameter('baud', 4800).value

    try:
        # GPS = serial.Serial(port=serial_port, baudrate=serial_baud, timeout=2)
        # driver.get_logger().info("Successfully connected to {0} at {1}.".format(serial_port, serial_baud))
        # try:
        #     while rclpy.ok():
        #         data = GPS.readline().strip()
        #         try:
        #             if isinstance(data, bytes):
        #                 data = data.decode("utf-8")
        #             driver.add_sentence(data, frame_id)
        #         except ValueError as e:
        #             driver.get_logger().warn(
        #                 "Unable to obtain fix: %s" % e)

        package_dir = get_package_share_directory('gps_service')  
        file_path = os.path.join(package_dir, 'test_nmea_path.txt') 
        GPS = open(file_path,'r')   
        try:
            while rclpy.ok():
                executor.spin_once(timeout_sec=0.1)
                for data in GPS:
                    try:
                        if isinstance(data, bytes):
                            data = data.decode("utf-8")
                        driver.add_sentence(data, frame_id)
                    except ValueError as e:
                        driver.get_logger().warn(
                            "Unable to obtain fix: %s" % e)
                    time.sleep(0.1)
                

        except Exception as e:
            driver.get_logger().error("Ros error: {0}".format(e))
            GPS.close()  # Close GPS serial port
    except serial.SerialException as ex:
        driver.get_logger().fatal("Could not open serial port: I/O error({0}): {1}".format(ex.errno, ex.strerror))
