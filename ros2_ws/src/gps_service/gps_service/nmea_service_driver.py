import serial

import rclpy

from driver import Ros2NMEADriver


def main(args=None):
    rclpy.init(args=args)

    driver = Ros2NMEADriver()
    frame_id = driver.get_frame_id()

    serial_port = driver.declare_parameter('port', '/dev/ttyAMA0').value
    serial_baud = driver.declare_parameter('baud', 4800).value

    try:
        GPS = serial.Serial(port=serial_port, baudrate=serial_baud, timeout=2)
        driver.get_logger().info("Successfully connected to {0} at {1}.".format(serial_port, serial_baud))
        try:
            while rclpy.ok():
                data = GPS.readline().strip()
                try:
                    if isinstance(data, bytes):
                        data = data.decode("utf-8")
                    driver.add_sentence(data, frame_id)
                except ValueError as e:
                    driver.get_logger().warn(
                        "Unable to obtain fix: %s" % e)

        except Exception as e:
            driver.get_logger().error("Ros error: {0}".format(e))
            GPS.close()  # Close GPS serial port
    except serial.SerialException as ex:
        driver.get_logger().fatal("Could not open serial port: I/O error({0}): {1}".format(ex.errno, ex.strerror))
