import rclpy
from rclpy.node import Node
from gpiozero import DigitalOutputDevice
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Bool
from smbus2 import SMBus
import time


class MotorControllerNode(Node):
    def __init__(self):
        super().__init__('motor_controller')

        self.GPIO_PIN_LEFT = 5
        self.LEFT_MOTOR = DigitalOutputDevice(self.GPIO_PIN_LEFT)
        self.GPIO_PIN_RIGHT = 6
        self.RIGHT_MOTOR = DigitalOutputDevice(self.GPIO_PIN_RIGHT)

        self.I2C_BUS = 1
        self.esp_address = 0x1D
        self.bus = SMBus(self.I2C_BUS)

        self.center = 7.5
        self.left_value = self.center
        self.right_value = self.center

        self.running = True

        self.subscription = self.create_subscription(
            Float32MultiArray,
            'set_duty_cycle',
            self.duty_cycle_callback,
            10)

    def duty_cycle_callback(self, msg):
        if (5 <= msg.data[0] <= 10 and 5 <= msg.data[1] <= 10):
            with self.value_lock:
                self.left_value = msg.data[0]
                self.right_value = msg.data[1]
    
    def send_motor_values(self):
        scaled_left = self.left_value * 100
        scaled_right = self.right_value * 100

    def send_i2c_data(self, left_value, right_value):

        # Break the values into bytes
        left_msb = (left_value >> 8) & 0xFF
        left_lsb = left_value & 0xFF
        right_msb = (right_value >> 8) & 0xFF
        right_lsb = right_value & 0xFF

        try:
            # Send both motor values in one I2C transaction
            self.bus.write_i2c_block_data(
                self.slave_address,
                0x00,  # Command byte (can be used to identify motor data packet)
                [left_msb, left_lsb, right_msb, right_lsb]
            )
        except Exception as e:
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