import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float64MultiArray, Float32MultiArray
import time

# This node provides the autonomous navigation interface for the robot.
# It manages the robot's movement based on the centroid of the detected waste, and handles temporary 'patrol' movement when no centroid is detected.
# Publishers: 'set_motor_speeds'
# Subscribers: 'centroid', 'emergency_stop'
class Autonomous(Node):
    def __init__(self):
        super().__init__('autonomous')

        # Publisher for motor speeds
        # Message type: Float32MultiArray
        self.speed_publisher = self.create_publisher(Float32MultiArray, 'set_motor_speeds', 10)

        # Subscription to the centroid topic
        # This topic provides the coordinates of the detected waste centroid
        self.centroid_listener = self.create_subscription(Float64MultiArray, 'centroid', self.update_heading, 10)
        # Center of the robot's field of view based on the camera's resolution
        self.x_center = 320
        # Maximum y value based on the camera's resolution
        self.y_max = 480

        # Initializes the gain values for the proportional controller
        self.kp_x = 0.0005
        self.kp_y = 0.0005

        # Subscription to emergency stop topic
        # If emergency stop is triggered, the node will be destroyed
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

        # Timer to check for no centroids detected recently
        self.no_centroid_timer = self.reset_timer()

    # Reset the 'patrol' timer
    def reset_timer(self):
        # If the timer is already running, cancel it
        if self.no_centroid_timer:
            self.no_centroid_timer.cancel()

        # Create a new timer that will call the handle_missing_centroid method after 3 seconds
        self.no_centroid_timer = self.create_timer(3.0, self.handle_missing_centroid)

    # Update the robot's heading based on the centroid coordinates
    # This method is called whenever a new centroid message is received as a Float64MultiArray
    def update_heading(self, msg):
        # Seperate the x and y coordinates from the message
        x = msg.data[0]
        y = msg.data[1]

        # Reset the 'patrol' timer whenever a new centroid is detected
        self.reset_timer()

        # Get the error in the x and y coordinates
        # The x error is the horizontal distance from the center of the camera's field of view
        # The y error is the vertical distance from the maximum y value (bottom of the camera's field of view)
        x_error = x - self.x_center
        y_error = self.y_max - y

        # Calculate the turn speed and forward speed using the proportional controller
        turn_speed = self.kp_x * x_error
        forward_speed = self.kp_y * y_error

        # Calculate the left and right motor speeds
        left_speed = forward_speed + turn_speed
        right_speed = forward_speed - turn_speed

        # Limit the speed values to a maximum of 0.5 and a minimum of -0.5 to prevent the motors from going too fast
        left_speed = max(-0.5, min(0.5, left_speed))
        right_speed = max(-0.5, min(0.5, right_speed))

        # Publish the updated motor speeds
        self.publish_speed(left_speed, right_speed)

    # Spin the robot slowly clockwise when no centroid is detected
    # This method is called by the timer when no centroid has been detected for 3 seconds
    def handle_missing_centroid(self):
        self.publish_speed(0.15, -0.15)

    # Publish the motor speed values to the 'set_motor_speeds' topic
    # The message contains two float values representing the left and right motor speeds
    # The values are in the range -1 to 1, where 0 is stop, positive values are forward, and negative values are backward
    def publish_speed(self, left_value, right_value):
        msg = Float32MultiArray()
        msg.data = [left_value, right_value]
        self.speed_publisher.publish(msg)
    
    # Destroy the node when the emergency stop is triggered
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