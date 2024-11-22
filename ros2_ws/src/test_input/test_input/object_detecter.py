import rclpy
from rclpy.node import Node
from ultralytics import YOLO
from std_msgs.msg import String
import cv2

class ObjectDetector(Node):
    def __init__(self):
        super().__init__('object_detector')

        self.model = YOLO('yolo11n.pt')
        self.cap = cv2.VideoCapture(2)
        if not self.cap.isOpened():
            self.get_logger().error("Error: Could not open webcam.")
            self.destroy_node()
            return
        
        self.detection_pub = self.create_publisher(String, 'object_detected', 10)
        
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.process_image)
        self.i = 0

    def process_image(self):
        ret, frame = self.cap.read()
        if ret:
            results = self.model(frame)

            publishString = String()
            objectStrings = ""

            for box in results[0].boxes:
                class_label = self.model.names[int(box.cls[0])]
                raw_conf = box.conf[0]
                conf = 100 * round(raw_conf.item(), 2)
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                objectString = f"{class_label}, {conf}, {x1}, {y1}, {x2}, {y2}"
                if objectStrings:
                    objectStrings += " $ " + objectString
                else:
                    objectStrings = objectString

            publishString.data = objectStrings

    def destroy_node(self):
        if self.cap.isOpened():
            self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    object_detector = ObjectDetector()
    try:
        rclpy.spin(object_detector)
    except KeyboardInterrupt:
        object_detector.get_logger().info("Shutting down camera")
    finally:
        object_detector.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
