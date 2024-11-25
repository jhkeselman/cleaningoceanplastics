import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from resource.priority_queue import PriorityQueue
from enum import Enum

class State(Enum):
        SEARCHING = 1
        MOVING = 2

class Waste(Enum):
    BOTTLE = 10
    BAG = 9

class ObjectSelector(Node):
    def __init__(self):
        super().__init__('object_selector')
        
        self.object_listener = self.create_subscription(String, 'object_detections', self.listener_callback, 10)

        self.min_confidence = 50
        self.image_width = 640
        self.image_height = 480
        self.image_size = self.dist(self.image_width, self.image_height)

        self.state = self.State.SEARCHING
        self.target = None

    def listener_callback(self, msg):
        data = msg.data
        objects = data.split(" $ ")
        self.get_logger().info("New detections")
        # TEMP FOR TESTING
        for object in objects:
            self.get_logger().info(f"{object}")
        # FUTURE CODE
        # if self.state == State.SEARCHING:
        #     queue = PriorityQueue()
        #     for object in objects:
        #         object_info = object.split(",")
        #         priority = self.rate_object(object_info[0], object_info[1], object_info[2], object_info[3], object_info[4], object_info[5])
        #         queue.put(priority, object_info)
        #     self.target = queue.get()
        # elif self.state == State.MOVING:
        #     # genuinely very little idea how this one will work rn, probably need to dig more into results formatting
        #     pass
                


    def rate_object(self, object_type, confidence, x1, y1, x2, y2):
        score = Waste[object_type.upper()]
        score += min(0, confidence - self.min_confidence) / 10.0
        center_X = (x1 + x2) / 2.0
        center_Y = (y1 + y2) / 2.0
        dist_from_center = self.dist(self.image_width - center_X, self.image_height - center_Y)
        score += 10.0 / (dist_from_center / self.image_size)

    def dist(self, x, y):
        return (x^2 + y^2)^(0.5)
        


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