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

        # self.amplitude = 2.5
        self.left_amp = 2.5
        self.right_amp = 2.0
        self.center = 7.5

        self.I2C_address = 0x55
        self.bus = smbus.SMBus(1)

        self.pwm_subscription = self.create_subscription(
            Float32MultiArray,
            'set_duty_cycle',
            self.duty_cycle_callback,
            10)
        
        self.speed_subscription = self.create_subscription(
            Float32MultiArray,
            'set_motor_speeds',
            self.set_motor_speeds,
            10)

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

    def convert_speed(self, speed, side=True):
        # 
        if side == True:
            return -self.left_amp*speed + self.center
        else:
            return -self.right_amp*speed + self.center

    def set_motor_speeds(self, msg):
        if (-1 <= msg.data[0] <= 1 and -1 <= msg.data[1] <= 1):
            self.send_value(self.convert_speed(msg.data[0], True), self.convert_speed(msg.data[1], False))

    def duty_cycle_callback(self, msg):
        if (5 <= msg.data[0] <= 10 and 5 <= msg.data[1] <= 10):
            self.send_value(msg.data[0], msg.data[1])
                
    def send_value(self, left_value, right_value):
        data = struct.pack('ff',left_value, right_value) #sending 1 means the data is motor values
        byte_list = list(data)
        try:
            self.bus.write_i2c_block_data(self.I2C_address, 0, byte_list)
        except:
            self.get_logger().info("Failed to send value")

    def stop_motors(self):
        self.send_value(7.5, 7.5)

    def destroy_node(self, msg):
        self.stop_motors()
        time.sleep(0.1)
        super().destroy_node()

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