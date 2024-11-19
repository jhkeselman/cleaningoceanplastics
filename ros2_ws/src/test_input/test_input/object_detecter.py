import rclpy
from rclpy.node import Node
from ultralytics import YOLO
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
        
        self.detection_pub = self.create_publisher(ObjectList, 'object_detections', 10)
        
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.process_image)
        self.i = 0

    def process_image(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error("Error: Could not read from camera.")
            return

        results = self.model(frame)

        object_list = ObjectList()
        object_list.header.stamp = self.get_clock().now().to_msg()

        for box in results[0].boxes:
            object = ObjectBox()
            object.name = str(box.cls)
            object.confidence = float(box.conf)
            object.x_center = float(box.xywh[0])
            object.y_center = float(box.xywh[1])
            object_list.objects.append(object)

        self.detection_pub.publish(object_list)
        self.i += 1

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
