import rclpy
from rclpy.node import Node
from gpiozero import DigitalOutputDevice
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Bool
import smbus
import struct
import sys
import time

# This node handles the transmission of motor speed commands to the motor controller (ESP32) via I2C.
# Scaled speed control values from either teleoperation or autonomous control are converted to PWM signals.
# Publishers:
# Subscribers: 'set_motor_speeds', 'emergency_stop'
class MotorControllerNode(Node):
    def __init__(self):
        super().__init__('motor_controller')

        # PWM commands for the motors are in the range of 5 to 10: 5 is full positive speed, 7.5 is stopped, 10 is full negative speed
        # Amplitude is used to set the range of the PWM signal
        # Center is the value at which the motors are stopped
        self.amplitude = 2.5
        self.center = 7.5

        # I2C address of the motor controller (ESP32)
        self.I2C_address = 0x55
        self.bus = smbus.SMBus(1)
        
        # Subscription to the 'set_motor_speeds' topic
        self.speed_subscription = self.create_subscription(
            Float32MultiArray,
            'set_motor_speeds',
            self.set_motor_speeds,
            10)

        # Subscription to emergency stop topic
        # If emergency stop is triggered, the node will be destroyed and both motors will be stopped
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

    # Convert the speed from the range -1 to 1 to the range of PWM signals
    # Input: [float] speed in the range -1 to 1
    # Output: [float] speed in the range 5 to 10
    def convert_speed(self, speed):
            return -self.amplitude*speed + self.center

    # Processes the incoming speed command from the 'set_motor_speeds' topic
    # Input: [Float32MultiArray] msg containing the speed values for left and right motors
    def set_motor_speeds(self, msg):
        # Check if the message is correctly formatted and scaled speed values are valid in the range -1 to 1
        if (-1 <= msg.data[0] <= 1 and -1 <= msg.data[1] <= 1):
            # Scale the speed values to the range of PWM signals and call 'send_value'
            self.send_value(self.convert_speed(msg.data[0]), self.convert_speed(msg.data[1]))
                
    # Send the scaled speed values to the motor controller via I2C
    # Input: [float] left_value, [float] right_value
    def send_value(self, left_value, right_value):
        # Pack the values into a binary format (12 bytes total)
        # The first byte is a command identifier: 1 for setting motor speeds
        # The second and third bytes are the left and right motor speed values
        data = struct.pack('iff',1, left_value, right_value)
        # Convert the packed data to a list of bytes for I2C transmission
        byte_list = list(data)
        # Send the data to the motor controller via I2C
        try:
            self.bus.write_i2c_block_data(self.I2C_address, 0, byte_list)
        except:
            self.get_logger().info("Failed to send value")
        

    # Stop the motors by sending the stop PWM values (7.5 for both left and right)
    def stop_motors(self):
        self.send_value(7.5, 7.5)

    # Destroy the node when the emergency stop is triggered
    # Stops the motors before shutting down
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