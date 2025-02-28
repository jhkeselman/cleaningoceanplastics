import sys
import time

from std_msgs.msg import Bool
from services.srv import GPSdata
import rclpy
from rclpy.node import Node


class GPSClient(Node):

    def __init__(self):
        super().__init__('gps_client')
        self.cli = self.create_client(GPSdata, 'get_GPS_fix')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GPSdata.Request()
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.send_request)

    def send_request(self):
        self.get_logger().info('Sent Request')
        self.future = self.cli.call_async(self.req)
        self.future.add_done_callback(self.response_callback)
    
    def response_callback(self,future):
        try:
            response = future.result()
            fix = response.fix.status.status
            self.get_logger().info('GPS Fix %d, Lat %5.3f, Long %5.3f:' %(fix, response.fix.latitude, response.fix.longitude))
        except Exception as e:
            self.get_logger().error(f'Service call failed {str(e)}')

    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    gps_client = GPSClient()
    rclpy.spin(gps_client)
    gps_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()