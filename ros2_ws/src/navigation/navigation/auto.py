import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float64MultiArray, Float32MultiArray
import time

class Autonomous(Node):
    def __init__(self):
        super().__init__('autonomous')

        self.speed_publisher = self.create_publisher(Float32MultiArray, 'set_motor_speeds', 10)

        self.centroid_listener = self.create_subscription(Float64MultiArray, 'centroid', self.update_heading, 10)
        self.x_center = 320
        self.y_max = 480

        self.kp_x = 0.1
        self.kp_y = 0.1

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

    def update_heading(self, msg):
        x = msg.data[0]
        y = msg.data[1]

        x_error = x - self.x_center
        y_error = self.y_max - y

        turn_speed = self.kp_x * x_error
        forward_speed = self.kp_y * y_error

        left_speed = forward_speed + turn_speed
        right_speed = forward_speed - turn_speed

        left_speed = max(-1, min(1, left_speed))
        right_speed = max(-1, min(1, right_speed))

        self.publish_speed(left_speed, right_speed)


    def publish_speed(self, left_value, right_value):
        msg = Float32MultiArray()
        msg.data = [left_value, right_value]
        self.speed_publisher.publish(msg)
    
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