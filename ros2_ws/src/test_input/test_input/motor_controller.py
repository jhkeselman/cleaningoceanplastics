import rclpy
from rclpy.node import Node
from gpiozero import DigitalOutputDevice
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Bool
import time
import threading


class MotorControllerNode(Node):
    def __init__(self):
        super().__init__('motor_controller')

        self.GPIO_PIN_LEFT = 5
        self.LEFT_MOTOR = DigitalOutputDevice(self.GPIO_PIN_LEFT)
        self.GPIO_PIN_RIGHT = 6
        self.RIGHT_MOTOR = DigitalOutputDevice(self.GPIO_PIN_RIGHT)
        

        self.center = 7.5
        self.period = 20
        self.left_value = self.center
        self.right_value = self.center

        self.running = True

        self.value_lock = threading.Lock()

        self.subscription = self.create_subscription(
            Float32MultiArray,
            'set_duty_cycle',
            self.duty_cycle_callback,
            10)

        print("starting left")
        self.thread_left = threading.Thread(target=self.binary_left)
        self.thread_left.start()
        print("left started")
        print("starting right")
        self.thread_right = threading.Thread(target=self.binary_right)
        self.thread_right.start()
        print("right started")

    def send_binary(self, value, motor):
        binary_value = bin(value)[2:]
        for bit in binary_value:
            if bit == '1':
                motor.on()
            else:
                motor.off()
            time.sleep(0.1)
        motor.off()

    def duty_cycle_callback(self, msg):
        if (5 <= msg.data[0] <= 10 and 5 <= msg.data[1] <= 10):
            with self.value_lock:
                self.left_value = msg.data[0]
                self.right_value = msg.data[1]

    def binary_left(self, value):
        while self.running:
            with self.value_lock:
                int_value = int(value * 10)
            self.send_binary(int_value, self.LEFT_MOTOR)
            time.sleep(0.5)

    def binary_right(self, value):
        while self.running:
            with self.value_lock:
                int_value = int(value * 10)
            self.send_binary(int_value, self.RIGHT_MOTOR)
            time.sleep(0.5)


    def destroy_node(self):
        self.running = False
        self.thread_left.join()
        self.thread_right.join()
        self.LEFT_MOTOR.off()
        self.RIGHT_MOTOR.off()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    motor_controller = MotorControllerNode()
    try:
        rclpy.spin(motor_controller)
    except KeyboardInterrupt:
        motor_controller.get_logger().info("Stopping motors")
    finally:
        motor_controller.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()