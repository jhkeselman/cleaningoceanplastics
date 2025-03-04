from services.srv import KalmanState

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

import math
import numpy as np

class KalmanService(Node):

    def __init__(self):
        super().__init__('Kalman_service')
        self.srv = self.create_service(KalmanState, 'get_Kalman_state', self.return_state)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def return_state(self, request, response):
        response.state = np.zeros(5)
        self.get_logger().info('Incoming request')
        return response
    
    def timer_callback(self):
        pass


def main():
    rclpy.init()

    kalman_service = KalmanService()

    rclpy.spin(kalman_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()