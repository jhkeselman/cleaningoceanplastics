import rclpy
from rclpy.node import Node
import os
import psutil
import signal

from std_msgs.msg import Bool, Float64MultiArray
from sensor_msgs.msg import NavSatFix
from services.srv import IMUData

class Control(Node):

    def __init__(self):
        super().__init__('control')

        # Subscriber for water sensor
        self.create_subscription(Bool, 'water_detected', self.detect_water, 10)
        self.create_subscription(NavSatFix, 'fix', self.update_position, 10)
        # self.create_subscription(Float64MultiArray, 'imu', self.update_tilt, 10)
        self.cli = self.create_client(IMUData, 'get_heading')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = IMUData.Request()

        # Create a timer to send requests every second
        self.timer = self.create_timer(1.0, self.timer_callback)

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
    
    # '''
    # Update the x, y, z angle of the robot
    # '''
    # def update_tilt(self, msg):
    #     self.xAngle = msg.data[0]
    #     self.yAngle = msg.data[1]
    #     self.heading = msg.data[2]

    '''
    Runs on 5 second timer to update heading
    '''
    def timer_callback(self):
        # Callback to send a request periodically
        self.future = self.cli.call_async(self.req)
        self.future.add_done_callback(self.response_callback)

    '''
    Performs and displays the heading update
    '''
    def response_callback(self, future):
        try:
            response = future.result()
            GREEN = '\033[92m'
            RESET = '\033[0m'  # Resets to default color

            # Log message with green color
            self.get_logger().info(
                f'{GREEN}IMU Heading: {response.heading:.3f}, '
                f'Latitude: {self.latitude:.6f}, '
                f'Longitude: {self.longitude:.6f}, '
                f'Altitude: {self.altitude:.2f}{RESET}'
            )
        except Exception as e:
            self.get_logger().error('Service call failed: %r' % (e,))

def main(args=None):
    rclpy.init(args=args)

    control_node = Control()

    rclpy.spin(control_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
