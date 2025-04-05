import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, Bool
import struct
import sys
import time
from sys import stdin
import select

# This node provides the teleoperation interface for the robot.
# It reads keyboard inputs and publishes corresponding motor speed commands on the range -1 to 1.
# Publishers: 'set_motor_speeds'
# Subscribers: 'emergency_stop'
class Teleop(Node):
    def __init__(self):
        super().__init__('teleop')
        # Publisher for motor speeds
        self.speed_publisher = self.create_publisher(Float32MultiArray, 'set_motor_speeds', 10)
        
        # Timer to check for keyboard inputs every 0.1 seconds
        self.timer = self.create_timer(0.1, self.check_input)

        # Initializes variable to store the last key pressed
        self.last_input = ''
        # Initializes left and right motor speed values
        self.left_value = 0
        self.right_value = 0

        # Subscription to emergency stop topic
        # If emergency stop is triggered, the node will be destroyed
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

    # Check for keyboard input, called every 0.1 seconds by the timer
    def check_input(self):
        # Check if there is input from stdin
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            # Read a single character from stdin
            key = sys.stdin.read(1)
            # Remove any whitespace characters
            key = key.strip()
            # If key is not empty, process it
            if key:
                self.process_key(key)

    # Process key inputs and update motor speeds accordingly
    # 'w' for forward, 's' for backward, 'a' for left, 'd' for right, 'x' for stop
    # If the same key is pressed consecutively, increase the speed at which the robot moves in that direction
    # If a different key is pressed, set the speed to a default value
    # If 'x' is pressed, stop the robot
    def process_key(self, key):
        # Key 'w': forward linear movement
        if key == 'w':
            # If 'w' is pressed after another linear speed command ('w' or 's'), increase speed in the forward direction
            if key == self.last_input or self.last_input == 's':
                self.left_value = min(1, self.left_value + 0.1)
                self.right_value = min(1, self.right_value + 0.1)
            # If 'w' is pressed after a turn command ('a' or 'd'), set speed to a default forward value
            else:
                self.left_value = 0.2
                self.right_value = 0.2
        # Key 's': backward linear movement
        elif key == 's':
            # If 's' is pressed after another linear speed command ('w' or 's'), increase speed in the backward direction
            if key == self.last_input or self.last_input == 'w':
                self.left_value = max(-1, self.left_value - 0.1)
                self.right_value = max(-1, self.right_value - 0.1)
            # If 's' is pressed after a turn command ('a' or 'd'), set speed to a default backward value
            else:
                self.left_value = -0.2
                self.right_value = -0.2
        # Key 'a': turn left
        elif key == 'a':
            # If 'a' is pressed after another turn command ('a' or 'd'), increase speed in the left direction
            if key == self.last_input or self.last_input == 'd':
                self.left_value = max(-1, self.left_value - 0.1)
                self.right_value = min(1, self.right_value + 0.1)
            # If 'a' is pressed after a linear speed command ('w' or 's'), set speed to a default left turn value
            else:
                self.left_value = -0.2
                self.right_value = 0.2
        # Key 'd': turn right
        elif key == 'd':
            # If 'd' is pressed after another turn command ('a' or 'd'), increase speed in the right direction
            if key == self.last_input  or self.last_input == 'a':
                self.left_value = max(-1, self.left_value + 0.1)
                self.right_value = min(1, self.right_value - 0.1)
            # If 'd' is pressed after a linear speed command ('w' or 's'), set speed to a default right turn value
            else:
                self.left_value = 0.2
                self.right_value = -0.2
        # Key 'x': stop the robot
        elif key == 'x':
            self.left_value = 0.0
            self.right_value = 0.0
        # Store the last key pressed to check for consecutive inputs of the same movement type (linear or rotational)
        self.last_input = key
        # Publish the updated motor speeds
        self.publish_speed()
    
    # Publish the motor speed values to the 'set_motor_speeds' topic
    # The message contains two float values representing the left and right motor speeds
    # The values are in the range -1 to 1, where 0 is stop, positive values are forward, and negative values are backward
    # The message type is Float32MultiArray
    def publish_speed(self):
        msg = Float32MultiArray()
        msg.data = [self.left_value, self.right_value]
        self.speed_publisher.publish(msg)
    
    # Destroy the node when the emergency stop is triggered
    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    teleop = Teleop()
    try:
        rclpy.spin(teleop)
    finally:
        teleop.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()