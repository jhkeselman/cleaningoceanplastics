import rclpy
from rclpy.node import Node
from gpiozero import DigitalOutputDevice
from std_msgs.msg import Float32
import time
import threading

class MotorControllerNode(Node):
    def __init__(self):
        super().__init__('motor_controller')

        self.GPIO_PIN_LEFT = 24
        self.LEFT_MOTOR = DigitalOutputDevice(self.GPIO_PIN_LEFT)

        # self.frequency = 50
        self.period = 20
        self.current_duty_cycle = 7
        self.target_duty_cycle = 7

        # Proportional gain
        self.kp = 0.5
        self.init_complete = False

        self.running = True

        self.subscription = self.create_subscription(
            Float32,
            'set_duty_cycle',
            self.duty_cycle_callback,
            10)

        self.thread = threading.Thread(target=self.pwm_loop)
        self.thread.start()

    def duty_cycle_callback(self, msg):
        if 5 <= msg.data <= 10:
            self.init_complete = True
            self.target_duty_cycle = msg.data

    def pwm_loop(self):
        while self.running:
            error = self.target_duty_cycle - self.current_duty_cycle
            self.current_duty_cycle += self.kp * error

            # Bound between these values if not being initalized
            if self.init_complete:
                self.current_duty_cycle = max(5.0, min(10.0, self.current_duty_cycle))

            high = (self.current_duty_cycle / 100) * self.period
            low = self.period - high

            self.LEFT_MOTOR.on()
            time.sleep(high / 1000)
            self.LEFT_MOTOR.off()
            time.sleep(low / 1000)

    def destroy_node(self):
        self.running = False
        self.thread.join()
        self.LEFT_MOTOR.off()
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

# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Float64MultiArray
# # from simple_pid import PID
# from gpiozero import PWMOutputDevice
# import time
# from rpi_hardware_pwm import HardwarePWM

# class MotorControllerNode(Node):
#     def __init__(self):

#         super().__init__('motor_controller')

#         # Replace these with the actual GPIO pin numbers
#         self.GPIO_PIN_LEFT = 12  # Actually on the right side
#         self.GPIO_PIN_RIGHT = 26  # Actually on the left side

#         # Define the pulse width modulation ranges
#         self.MIN_PWM = 0.05  # gpiozero expects values between 0.0 and 1.0
#         self.MID_PWM = 0.075
#         self.MAX_PWM = 0.1

#         import RPi.GPIO as GPIO
#         GPIO.setmode(GPIO.BOARD)
#         GPIO.setup(12, GPIO.OUT)

#         p = GPIO.PWM(12, 50)
#         p.start(0.075)
#         input('Press return to stop:')   # use raw_input for Python 2
#         p.stop()
#         GPIO.cleanup()

#         # pwm = HardwarePWM(pwm_channel=0, hz=50, chip=)
#         # pwm.start(7.5) # full duty cycle
#         # time.sleep(2)

#         # pwm.change_duty_cycle(5)
#         # time.sleep(2)

#         # pwm.stop()

#         # Initialize the PWM output devices
#         # self.left_motor = PWMOutputDevice(self.GPIO_PIN_LEFT, initial_value=0.079, frequency=50)
#         # self.right_motor = PWMOutputDevice(self.GPIO_PIN_RIGHT, initial_value=self.MID_PWM, frequency=50)

#         # # Double check it's on by running this
#         # # self.left_motor.on()

#         # # Test if ESC is connected
#         # self.left_motor.blink(on_time=3, off_time=3, fade_in_time=0, fade_out_time=0, n=2, background=False)


#         # self.left_motor.value = 0.079
#         # ARMING SEQUENCE
#         # self.left_motor.value = self.MAX_PWM
#         # self.left_motor.value = self.MIN_PWM
#         # for i in range(5000):
#         #     self.left_motor.value = self.MID_PWM
#         #     time.sleep(0.001)

#         # time.sleep(1)
#         # self.left_motor.value = 0.05
#         # self.left_motor.value = 0.0
#         # self.left_motor.blink(on_time=0.0015, off_time=0.9985, fade_in_time=0, fade_out_time=0, n=None, background=True)        


#         # self.motor_subscription = self.create_subscription(Float64MultiArray, 'set_motor_vels', self.hard_code, 10)

#     def hard_code(self, msg):
#         print(msg.data[0])
#         self.left_motor.value = msg.data[0]

#     #takes in an array with two floats, the first of which is the power (0.0-1.0) of the left motor and the second of which is the power (0.0-1.0) of the right motor
#     def set_motor_velocity(self, msg):
#         print("Message recieved")
#         print(msg.data[0])
#         print(msg.data[1])
#         self.set_motor_speeds(min(1.0, max(msg.data[0], 0.0)), min(1.0, max(msg.data[1], 0.0)))

#     def set_motor_speeds(self, left_speed, right_speed):
#         # Map the speeds to the PWM range
#         print("left speed")
#         print(left_speed)
#         print("right speed")
#         print(right_speed)
#         left_pwm = self.map_speed_to_pwm(left_speed, 'left')  # Speed increases with decreasing PWM
#         right_pwm = self.map_speed_to_pwm(right_speed, 'right')  # Speed increases with increasing PWM

#         # Set the PWM duty cycle for each motor
#         self.left_motor.value = left_pwm
#         self.right_motor.value = right_pwm
#         # self.left_motor.on()
#         # self.right_motor.on()
#         print(self.left_motor.value)

#     def map_speed_to_pwm(self, speed, motor):
#         if motor == 'left':
#             # Scale the speed value (e.g., -1 to 1) to the PWM range
#             print("setting left pwm")
#             print(speed)
            
#             return max(0.0, min(1.0, (speed * (self.MAX_PWM - self.MIN_PWM))))
#         elif motor == 'right':
#             print("setting right pwm")
#             print(speed)
#             return max(0.0, min(1.0, (speed * (self.MAX_PWM - self.MIN_PWM)) + 0))


#     def destroy_node(self):
#         super().destroy_node()

# def main(args=None):
#     rclpy.init(args=args)

#     motor_controller = MotorControllerNode()
#     try:
#         rclpy.spin(motor_controller)
#     except KeyboardInterrupt:
#         motor_controller.get_logger().info("Stopping motor")
#     finally:
#         motor_controller.destroy_node()
#         rclpy.shutdown()


# if __name__ == '__main__':
#     main()
