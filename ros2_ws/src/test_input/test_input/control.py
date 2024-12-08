import rclpy
from rclpy.node import Node
import os

from std_msgs.msg import Bool

class Control(Node):

    def __init__(self):
        super().__init__('control')

        # Subscriber for water sensor
        self.create_subscription(Bool, 'water_detected', self.detect_water, 10)
        
        self.get_logger().info('Initialized control node')

    def detect_water(self, msg):
        if(msg.data):
            #Shutdown everything
            self.get_logger().warn("Emergency Stop Received! Shutting down all nodes...")
            os.system('ros2 lifecycle set / all shutdown')  # For managed nodes
            os.system('killall -9 ros2')

        


def main(args=None):
    rclpy.init(args=args)

    control_node = Control()

    rclpy.spin(control_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
