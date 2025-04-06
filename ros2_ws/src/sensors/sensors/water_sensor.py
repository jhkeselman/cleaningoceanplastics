import rclpy, os, time
from rclpy.node import Node
from std_msgs.msg import Bool

from gpiozero import DigitalInputDevice

# This node interfaces with the water sensor on the robot.
# It listens for a HIGH signal detecting water and publishes an emergency stop signal to all nodes.
# Publishers: 'emergency_stop'
# Subscribers: ''

class WaterSensor(Node):

    def __init__(self):
        super().__init__('water_sensor')

        # Create publisher to broadcast status of water sensor as a boolean (1 water, 0 no water)
        self.publisher_ = self.create_publisher(Bool, 'emergency_stop', 10)
        
        # Create a timer for the callback function
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Initialize water sensor as DigitalInputDevice (HIGH/LOW)
        SENSOR_GPIO = 27
        self.sensor = DigitalInputDevice(SENSOR_GPIO)

        # Used to check if value changes in callback function (starts with no water detected)
        self.prev = False

        self.get_logger().info("Water sensor initialized...")
   
    def get_data(self):
        try:
            # Read the sensor state
            sensor_state = self.sensor.value  # 1 if HIGH, 0 if LOW
            if sensor_state == 1:
                return True
            else:
                return False
        except Exception as e:
            return True # False positive
    
    # Callback function to handle water sensor logic
    def timer_callback(self):
        # Update the status of the water sensor (True/False)
        status = self.get_data()

        # If the current status is different than the previous (water!)
        if status != self.prev:
            # Structure the ROS message to be sent over the publisher
            msg = Bool()
            msg.data = status
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)

            # Set the previous value to be the current
            self.prev = status

            # And...shut everything down
            time.sleep(0.5)
            os.system('sudo shutdown -h now')



# Typical ROS node stuff
def main(args=None):
    rclpy.init(args=args)

    water_sensor = WaterSensor()

    rclpy.spin(water_sensor)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
