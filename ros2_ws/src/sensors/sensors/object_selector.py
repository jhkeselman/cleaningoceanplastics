import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from enum import Enum
import numpy as np

class ObjectSelector(Node):
    def __init__(self):
        super().__init__('object_selector')
        
        self.object_listener = self.create_subscription(String, 'object_detections', self.listener_callback, 10)

        self.image_width = 640
        self.image_height = 480
        # self.image_size = self.dist(self.image_width, self.image_height)

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
                print(x1)
                y1 = components[3]
                print(y1)
                x2 = components[4]
                print(x2)
                y2 = components[5]
                print(y2)
                # xCenters.append(np.mean(np.array([x1, x2])))
                # yCenters.append(np.mean(np.array([y1, y2])))

            # x = np.mean(np.array(xCenters))
            # y = np.mean(np.array(yCenters))
            # print(f"Mass center: ({x}, {y})")


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
