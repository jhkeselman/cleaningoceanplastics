import rclpy
from rclpy.node import Node
from gpiozero import DigitalOutputDevice
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Bool
import smbus
import struct
import sys
import time


class MotorControllerNode(Node):
    def __init__(self):
        super().__init__('motor_controller')

        self.center = 7.5

        self.I2C_address = 0x55
        self.bus = smbus.SMBus(1)

        self.subscription = self.create_subscription(
            Float32MultiArray,
            'set_duty_cycle',
            self.duty_cycle_callback,
            10)

    def duty_cycle_callback(self, msg):
        if (5 <= msg.data[0] <= 10 and 5 <= msg.data[1] <= 10):
            self.left_value = msg.data[0]
            self.right_value = msg.data[1]
            self.send_value(self.left_value)
                
    def send_value(self, value):
        data = struct.pack('f', value)
        byte_list = list(data)
        try:
            self.bus.write_i2c_block_data(self.I2C_address, 0, byte_list)
        except:
            self.get_logger().info("Failed to send value")

    def destroy_node(self):
        pass

def main(args=None):
    rclpy.init(args=args)

    motor_controller = MotorControllerNode()
    try:
        rclpy.spin(motor_controller)
    except KeyboardInterrupt:
        motor_controller.get_logger().info("Stopping motors")
    finally:
        motor_controller.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()