import sys
import time

from std_msgs.msg import Bool
from services.srv import IMUData
import rclpy
from rclpy.node import Node


class IMUClient(Node):

    def __init__(self):
        super().__init__('imu_client')
        self.cli = self.create_client(IMUData, 'get_IMU_data')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = IMUData.Request()

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )
        
        timer_period = 0.25
        self.timer = self.create_timer(timer_period, self.send_request)

    def send_request(self):
        self.future = self.cli.call_async(self.req)
        self.future.add_done_callback(self.response_callback)
    
    def response_callback(self,future):
        try:
            response = future.result()
            self.get_logger().info('IMU Heading %5.3f, Acc %5.3f, Omega %5.3f:' %(response.heading, response.acceleration, response.omega))
        except Exception as e:
            self.get_logger().error(f'Service call failed {str(e)}')

    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()



def main(args=None):
    rclpy.init(args=args)

    imu_client = IMUClient()
    rclpy.spin(imu_client)
    imu_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()