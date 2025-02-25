import sys

from services.srv import IMUData
import rclpy
from rclpy.node import Node


class IMUClient(Node):

    def __init__(self):
        super().__init__('imu_client')
        self.cli = self.create_client(IMUData, 'get_heading')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = IMUData.Request()

    def send_request(self):
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    imu_client = IMUClient()
    response = imu_client.send_request()
    imu_client.get_logger().info(
        'IMU Heading %5.3f:' %response.heading)

    imu_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()