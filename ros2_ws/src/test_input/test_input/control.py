import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Control(Node):

    def __init__(self):
        super().__init__('control')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        


def main(args=None):
    rclpy.init(args=args)

    control_node = Control()

    rclpy.spin(control_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
