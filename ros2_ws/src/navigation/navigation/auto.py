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

        self.kp_x = 0.2
        self.kp_y = 0.05

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

        self.no_centroid_timer = None
        self.no_centroid_timer = self.reset_timer()

    def reset_timer(self):
        if self.no_centroid_timer:
            self.no_centroid_timer.cancel()

        self.no_centroid_timer = self.create_timer(3.0, self.handle_missing_centroid)

    def update_heading(self, msg):
        x = msg.data[0]
        y = msg.data[1]

        self.reset_timer()

        x_error = x - self.x_center
        y_error = self.y_max - y

        turn_speed = self.kp_x * x_error
        forward_speed = self.kp_y * y_error

        left_speed = forward_speed + turn_speed
        right_speed = forward_speed - turn_speed

        left_speed = max(-0.5, min(0.5, left_speed))
        right_speed = max(-0.5, min(0.5, right_speed))

        self.publish_speed(left_speed, right_speed)

    def handle_missing_centroid(self):
        self.publish_speed(0.1, -0.1)


    def publish_speed(self, left_value, right_value):
        msg = Float32MultiArray()
        msg.data = [left_value, right_value]
        self.speed_publisher.publish(msg)
    
    def destroy_node(self, msg):
        self.publish_speed(0, 0)
        time.sleep(0.1)
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    autonomous = Autonomous()
    try:
        rclpy.spin(autonomous)
    except KeyboardInterrupt:
        autonomous.get_logger().info("Stopping motors")
    finally:
        autonomous.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()