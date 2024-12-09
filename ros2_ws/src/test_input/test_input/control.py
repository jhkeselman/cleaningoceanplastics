import rclpy
from rclpy.node import Node
import os

from std_msgs.msg import Bool, Float64MultiArray
from sensor_msgs.msg import NavSatFix

class Control(Node):

    def __init__(self):
        super().__init__('control')

        # Subscriber for water sensor
        self.create_subscription(Bool, 'water_detected', self.detect_water, 10)
        self.create_subscription(NavSatFix, 'fix', self.update_position, 10)
        self.create_subscription(Float64MultiArray, 'imu', self.update_tilt, 10)

        # Initialize variables
        self.longitude = 0.0
        self.latitude = 0.0
        self.altitude = 0.0

        self.xAngle = 0.0
        self.yAngle = 0.0
        self.heading = 0.0
        
        self.get_logger().info('Initialized control node')

    '''
    Perform an emergency stop if water is detected in the system
    '''
    def detect_water(self, msg):
        if(msg.data):
            #Shutdown everything
            self.get_logger().warn("Emergency Stop Received! Shutting down the system...")
            os.system('sudo shutdown now')
    
    '''
    Update the x, y, z position of the robot
    '''
    def update_position(self, msg):
        self.latitude = msg.latitude
        self.longitude = msg.longitude
        self.altitude = msg.altitude
    
    '''
    Update the x, y, z angle of the robot
    '''
    def update_tilt(self, msg):
        self.xAngle = msg.data[0]
        self.yAngle = msg.data[1]
        self.heading = msg.data[2]

        


def main(args=None):
    rclpy.init(args=args)

    control_node = Control()

    rclpy.spin(control_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
