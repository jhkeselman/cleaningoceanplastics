import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool

from gpiozero import DigitalInputDevice

class WaterSensor(Node):

    def __init__(self):
        super().__init__('water_sensor')
        self.publisher_ = self.create_publisher(Bool, 'emergency_stop', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
        # Initialize water sensor
        SENSOR_GPIO = 27
        self.sensor = DigitalInputDevice(SENSOR_GPIO)
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

    def timer_callback(self):
        status = self.get_data()
        if status != self.prev:
            msg = Bool()
            msg.data = status
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.i += 1
            self.prev = status


def main(args=None):
    rclpy.init(args=args)

    water_sensor = WaterSensor()

    rclpy.spin(water_sensor)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
