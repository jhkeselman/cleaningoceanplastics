import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import struct
import sys
import time
from getkey import getkey, keys

class Teleop(Node):
    def __init__(self):
        super().__init__('teleop')
        self.key = getkey()
        self.speed_publisher = self.create_publisher(Float32MultiArray, 'set_motor_speeds', 10)
        timer_period: float = 0.05
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        print(self.key)
        if self.key == keys.UP:
            msg = Float32MultiArray()
            msg.data = (1,1)
            self.speed_publisher.publish(msg)
        elif self.key == keys.DOWN:
            msg = Float32MultiArray()
            msg.data = (-1,-1)
            self.speed_publisher.publish(msg)
        elif self.key == keys.LEFT:
            msg = Float32MultiArray()
            msg.data = (-1,1)
            self.speed_publisher.publish(msg)
        elif self.key == keys.RIGHT:
            msg = Float32MultiArray()
            msg.data = (1,-1)
            self.speed_publisher.publish(msg)
        elif self.key == 'x':
            msg = Float32MultiArray()
            msg.data = (0,0)
            self.speed_publisher.publish(msg)
            
            

    def destroy_node(self):
        #send message to stop motors
        time.sleep(0.1)
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    teleop = Teleop()
    try:
        rclpy.spin(teleop)
    finally:
        teleop.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()