import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float64MultiArray
from enum import Enum
import statistics

class ObjectSelector(Node):
    def __init__(self):
        super().__init__('object_selector')
        
        self.object_listener = self.create_subscription(String, 'object_detections', self.listener_callback, 10)

        self.image_width = 640
        self.image_height = 480

        self.centroid_publisher = self.create_publisher(Float64MultiArray, 'centroid', 10)

    def listener_callback(self, msg):
        data = msg.data
        objects = data.split(" $ ")
        self.get_logger().info("New detections")
        xCenters = []
        yCenters = []
        if objects != ['']:
            for object in objects:
                components = object.split(", ")
                object_type = components[0]
                confidence = components[1]
                x1 = components[2]
                y1 = components[3]
                x2 = components[4]
                y2 = components[5]
                xCenters.append(statistics.mean([float(x1), float(x2)]))
                yCenters.append(statistics.mean([float(y1), float(y2)]))

            x = statistics.mean(xCenters)
            y = statistics.mean(yCenters)

            msg = Float64MultiArray()
            msg.data = [x, y]
            self.centroid_publisher.publish(msg)
            self.get_logger().info(f"Centroid: {x}, {y}")


def main(args=None):
    rclpy.init(args=args)

    object_selector = ObjectSelector()
    try:
        rclpy.spin(object_selector)
    except KeyboardInterrupt:
        object_selector.get_logger().info("Shutting down subscriber")
    finally:
        object_selector.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
