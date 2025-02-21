import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, Bool
import struct
import sys
import time
from getkey import getkey, keys

class Teleop(Node):
    def __init__(self):
        super().__init__('teleop')
        self.pwm_publisher = self.create_publisher(Float32MultiArray, 'set_duty_cycle', 10)
        
        self.timer = self.create_timer(0.1, self.check_input)

        self.last_input = ''
        self.left_value = 7.5
        self.right_value = 7.5

    def check_input(self):
        key = getkey()
        if key == keys.UP:
            if key == self.last_input:
                self.left_value = min(10, self.left_value + 0.5)
                self.right_value = min(10, self.right_value + 0.5)
            else:
                self.left_value = 8.0
                self.right_value = 8.0
        elif key == keys.DOWN:
            if key == self.last_input:
                self.left_value = max(5, self.left_value - 0.5)
                self.right_value = max(5, self.right_value - 0.5)
            else:
                self.left_value = 6.0
                self.right_value = 6.0
        elif key == keys.LEFT:
            if key == self.last_input:
                self.left_value = max(5, self.left_value - 0.5)
                self.right_value = min(10, self.right_value + 0.5)
            else:
                self.left_value = 6.0
                self.right_value = 8.0
        elif key == keys.RIGHT:
            if key == self.last_input:
                self.left_value = min(10, self.left_value + 0.5)
                self.right_value = max(5, self.right_value - 0.5)
            else:
                self.left_value = 8.0
                self.right_value = 6.0
        elif key == 'x':
            self.left_value = 7.5
            self.right_value = 7.5
        self.last_input = key
        self.publish_pwm()
    
    def publish_pwm(self):
        msg = Float32MultiArray()
        msg.data = [self.left_value, self.right_value]
        self.pwm_publisher.publish(msg)
    

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