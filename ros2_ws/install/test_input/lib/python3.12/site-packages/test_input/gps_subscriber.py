import rclpy
from rclpy.node import Node

from sensor_msgs.msg import NavSatFix


class GPSSubscriber(Node):

    def __init__(self):
        super().__init__('gps_subscriber')
        self.subscription = self.create_subscription(
            NavSatFix,
            'fix',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        # Initialize variables
        self.longitude = 0.0
        self.latitude = 0.0
        self.altitude = 0.0

        self.get_logger().info('Initialized gps_subscriber')

    def listener_callback(self, msg):
        self.latitude = msg.latitude
        self.longitude = msg.longitude
        self.altitude = msg.altitude


def main(args=None):
    rclpy.init(args=args)

    gps_subscriber = GPSSubscriber()

    rclpy.spin( gps_subscriber)

    rclpy.shutdown()


if __name__ == '__main__':
    main()