import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import time

class Autonomous(Node):
    def __init__(self):
        super().__init__('autonomous')

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )
    
    def destroy_node(self, msg):
        time.sleep(0.1)
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    auto = Autonomous()
    try:
        rclpy.spin(auto)
    finally:
        auto.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()