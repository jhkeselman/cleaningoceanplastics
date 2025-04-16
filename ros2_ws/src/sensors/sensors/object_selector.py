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
        # Initializes lists to store the x and y coordinates of the centers of the detected objects
        x_weighted = 0
        y_weighted = 0
        total_weight = 0
        # If there are detected objects, calculate their centers
        for object in objects:
            # Split each object string into its components
            components = object.split(", ")
            object_type = components[0]
            if object_type == "Bottle" or object_type == "Can":
                confidence = components[1]
                # if confidence < 30:
                #     continue
                # x1: top left x coordinate
                x1 = components[2]
                # y1: top left y coordinate
                y1 = components[3]
                # x2: bottom right x coordinate
                x2 = components[4]
                # y2: bottom right y coordinate
                y2 = components[5]

                # Get average of the x and y coordinates to get the center of the object
                x = (float(x1) + float(x2)) / 2
                y = (float(y1) + float(y2)) / 2

                # Add the weighted x and y coordinates to the total
                # The weight is the confidence of the detection
                x_weighted += x * float(confidence)
                y_weighted += y * float(confidence)
                
                # Add the confidence to the total weight
                total_weight += float(confidence)
        
        # If there are detected objects, calculate the centroid (prevents division by zero)
        if total_weight > 0:
            # Calculate the centroid by averaging the x and y coordinates of all detected objects using weighted average
            x = x_weighted / total_weight
            y = y_weighted / total_weight
            
            # Publish the centroid message to 'centroid'
            msg = Float64MultiArray()
            msg.data = [x, y]
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
