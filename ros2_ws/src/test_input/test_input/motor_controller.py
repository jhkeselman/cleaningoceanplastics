import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from simple_pid import PID
from gpiozero import PWMOutputDevice

class MotorControllerNode(Node):
    def __init__(self):

        super().__init__('motor_controller')

        # Replace these with the actual GPIO pin numbers
        self.GPIO_PIN_LEFT = 24  # Actually on the right side
        self.GPIO_PIN_RIGHT = 26  # Actually on the left side
        # Define the pulse width modulation ranges
        self.MIN_PWM = 0.0  # gpiozero expects values between 0.0 and 1.0
        self.MAX_PWM = 1.0
        # Initialize the PWM output devices
        self.left_motor = PWMOutputDevice(self.GPIO_PIN_LEFT, initial_value=0, frequency=100)
        self.right_motor = PWMOutputDevice(self.GPIO_PIN_RIGHT, initial_value=0, frequency=100)

        self.motor_subscription = self.create_subscription(Float64MultiArray, 'set_motor_vels', self.set_motor_velocity, 10)

    #takes in an array with two floats, the first of which is the power (0.0-1.0) of the left motor and the second of which is the power (0.0-1.0) of the right motor
    def set_motor_velocity(self, msg):
        self.set_motor_speeds(min(0.0, max(msg.value.data[0], 1.0)), min(0.0, max(msg.data[1], 1.0)))

    def set_motor_speeds(self, left_speed, right_speed):
        # Map the speeds to the PWM range
        left_pwm = self.map_speed_to_pwm(left_speed, 'left')  # Speed increases with decreasing PWM
        right_pwm = self.map_speed_to_pwm(right_speed, 'right')  # Speed increases with increasing PWM
        
        # Set the PWM duty cycle for each motor
        self.left_motor.value = left_pwm
        self.right_motor.value = right_pwm

    def map_speed_to_pwm(self, speed, motor):
        if motor == 'left':
            # Scale the speed value (e.g., -1 to 1) to the PWM range
            return max(0.0, min(1.0, 1 - (speed * (1 - self.MIN_PWM))))
        elif motor == 'right':
            return max(0.0, min(1.0, (speed * (self.MAX_PWM - 0)) + 0))


    def destroy_node(self):
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    motor_controller = MotorControllerNode()
    try:
        rclpy.spin(motor_controller)
    except KeyboardInterrupt:
        motor_controller.get_logger().info("Stopping motor")
    finally:
        motor_controller.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
