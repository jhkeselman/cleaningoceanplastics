import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, Bool
import struct
import sys
import time
from sys import stdin
import select

class Teleop(Node):
    def __init__(self):
        super().__init__('teleop')
        self.speed_publisher = self.create_publisher(Float32MultiArray, 'set_motor_speeds', 10)
        
        self.timer = self.create_timer(0.1, self.check_input)

        self.last_input = ''
        self.left_value = 0
        self.right_value = 0

    def check_input(self):
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)
            key = key.strip()
            if key:
                self.process_key(key)

    def process_key(self, key):
        if key == 'w':
            if key == self.last_input or self.last_input == 's':
                self.left_value = min(1, self.left_value + 0.2)
                self.right_value = min(1, self.right_value + 0.2)
            else:
                self.left_value = 0.6
                self.right_value = 0.6
        elif key == 's':
            if key == self.last_input or self.last_input == 'w':
                self.left_value = max(0, self.left_value - 0.2)
                self.right_value = max(0, self.right_value - 0.2)
            else:
                self.left_value = 0.2
                self.right_value = 0.2
        elif key == 'a': # Turn left
            if key == self.last_input:
                self.left_value = max(0, self.left_value - 0.2)
                self.right_value = min(1, self.right_value + 0.2)
            else:
                self.left_value = 0.2
                self.right_value = 0.4
        elif key == 'd': # Turn Right
            if key == self.last_input:
                self.left_value = min(1, self.left_value + 0.2)
                self.right_value = max(0, self.right_value - 0.2)
            else:
                self.left_value = 0.4
                self.right_value = 0.2
        elif key == 'x':
            self.left_value = 0.0
            self.right_value = 0.0
        self.last_input = key
        self.publish_speed()
    
    def publish_speed(self):
        msg = Float32MultiArray()
        msg.data = [self.left_value, self.right_value]
        self.speed_publisher.publish(msg)
    

    def destroy_node(self):
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