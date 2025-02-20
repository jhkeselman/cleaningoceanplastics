import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import struct
import sys
import time

class Teleop(Node):
    def __init__(self):
        super().__init__('teleop')

    def destroy_node(self):
        #send message to stop motors
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