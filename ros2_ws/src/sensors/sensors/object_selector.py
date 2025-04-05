import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool, Float64MultiArray
from enum import Enum
import statistics
import time

# This node handles calculating the centroid of the overall detected items in an image
# The center of each object is calculated and those centers are averaged to get the centroid
# Publishers: 'centroid'
# Subscribers: 'object_detections', 'emergency_stop'
class ObjectSelector(Node):
    def __init__(self):
        super().__init__('object_selector')
        
        # Subscription to the 'object_detections' topic
        self.object_listener = self.create_subscription(String, 'object_detections', self.calculate_centroid, 10)

        # The image width and height
        self.image_width = 640
        self.image_height = 480

        # Publisher for the calculated centroid
        # Message type: Float64MultiArray
        self.centroid_publisher = self.create_publisher(Float64MultiArray, 'centroid', 10)

        # Subscription to emergency stop topic
        # If emergency stop is triggered, the node will be destroyed
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

    # Calculates the centroid of the detected objects
    # Input: [String] msg containing the detected objects as a string
    # Format: "object_type, confidence, x1, y1, x2, y2 $ object_type, confidence, x1, y1, x2, y2 $ ..."
    def calculate_centroid(self, msg):
        data = msg.data
        # Splits the string into individual object detections
        objects = data.split(" $ ")
        self.get_logger().info("New detections")
        # Initializes lists to store the x and y coordinates of the centers of the detected objects
        xCenters = []
        yCenters = []
        # If there are detected objects, calculate their centers
        if objects != ['']:
            for object in objects:
                # Split each object string into its components
                components = object.split(", ")
                object_type = components[0]
                confidence = components[1]
                # x1: top left x coordinate
                x1 = components[2]
                # y1: top left y coordinate
                y1 = components[3]
                # x2: bottom right x coordinate
                x2 = components[4]
                # y2: bottom right y coordinate
                y2 = components[5]
                # Add the center of the object to the lists, using statistics.mean to calculate the average of the x and y coordinates
                xCenters.append(statistics.mean([float(x1), float(x2)]))
                yCenters.append(statistics.mean([float(y1), float(y2)]))

            # Calculate the centroid by averaging the x and y coordinates of all detected objects
            x = statistics.mean(xCenters)
            y = statistics.mean(yCenters)

            # Creates a Float64MultiArray message to publish the centroid
            msg = Float64MultiArray()
            msg.data = [x, y]
            # Publish the centroid message to 'centroid'
            self.centroid_publisher.publish(msg)
            self.get_logger().info(f"Centroid: {x}, {y}")

    # Destroy the node when the emergency stop is triggered
    def destroy_node(self,msg):
        time.sleep(0.1)
        super().destroy_node()

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
