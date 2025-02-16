import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray

import math
import numpy as np

class KalmanService(Node):

    def __init__(self):
        super().__init__('Kalman_service')
        self.srv = self.create_service(KalmanState, 'get_Kalman_state', self.return_state)

    def return_state(self, request, response):
        response.state = np.zeros(5)
        self.get_logger().info('Incoming request')
        return response


def main():
    rclpy.init()

    kalman_service = KalmanService()

    rclpy.spin(kalman_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()