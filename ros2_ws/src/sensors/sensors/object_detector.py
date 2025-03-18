import rclpy
from rclpy.node import Node
from ultralytics import YOLO
from std_msgs.msg import String
import cv2
import time

class ObjectDetector(Node):
    def __init__(self):
        super().__init__('object_detector')

        # Path on Pi
        self.model = YOLO('/home/pi2/cleaningoceanplastics/ros2_ws/src/sensors/sensors/best.pt')
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error("Error: Could not open webcam.")
            self.destroy_node()
            return

        frame_width = int(self.cap.get(3))
        frame_height = int(self.cap.get(4))
        fps = 10

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.fps = 10  # Match ROS2 timer rate
        self.video_filename = f"/home/pi2/videos/detection_{int(time.time())}.mp4"
        self.video_writer = cv2.VideoWriter(self.video_filename, fourcc, self.fps, (frame_width, frame_height))
        
        self.detection_pub = self.create_publisher(String, 'object_detections', 10)
        
        self.timer_period = 0.1  # seconds
        self.timer = self.create_timer(self.timer_period, self.process_image)

        self.prev_time = time.time()

    def process_image(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 0)
            results = self.model(frame, verbose=True)
            annotated_frame = results[0].plot()  # YOLO outputs annotated images with .plot()

            elapsed_time = time.time() - self.prev_time
            if elapsed_time < self.timer_period:
                time.sleep(self.timer_period - elapsed_time)

            self.video_writer.write(frame)

            cv2.imshow("Real-Time Detection w/ YOLO", annotated_frame)
            cv2.waitKey(1)
        

    def destroy_node(self):
        if self.cap.isOpened():
            self.cap.release()
            self.video_writer.release()
            cv2.destroyAllWindows()
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


# import rclpy
# from rclpy.node import Node
# from ultralytics import YOLO
# from std_msgs.msg import String
# import cv2

# class ObjectDetector(Node):
#     def __init__(self):
#         super().__init__('object_detector')

#         self.model = YOLO('yolo11n.pt')
#         self.cap = cv2.VideoCapture(0)
#         if not self.cap.isOpened():
#             self.get_logger().error("Error: Could not open webcam.")
#             self.destroy_node()
#             return
        
#         self.detection_pub = self.create_publisher(String, 'object_detections', 10)
        
#         timer_period = 0.5  # seconds
#         self.timer = self.create_timer(timer_period, self.process_image)
#         self.i = 0

#     def process_image(self):
#         ret, frame = self.cap.read()
#         if ret:
#             results = self.model(frame)

#             publishString = String()
#             objectStrings = ""

#             for box in results[0].boxes:
#                 class_label = self.model.names[int(box.cls[0])]
#                 raw_conf = box.conf[0]
#                 conf = 100 * round(raw_conf.item(), 2)
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 objectString = f"{class_label}, {conf}, {x1}, {y1}, {x2}, {y2}"
#                 if objectStrings:
#                     objectStrings += " $ " + objectString
#                 else:
#                     objectStrings = objectString

#             if objectStrings != "":
#                 publishString.data = objectStrings
#             self.detection_pub.publish(publishString)

#     def destroy_node(self):
#         if self.cap.isOpened():
#             self.cap.release()
#         super().destroy_node()

# def main(args=None):
#     rclpy.init(args=args)

#     object_detector = ObjectDetector()
#     try:
#         rclpy.spin(object_detector)
#     except KeyboardInterrupt:
#         object_detector.get_logger().info("Shutting down camera")
#     finally:
#         object_detector.destroy_node()
#         rclpy.shutdown()


# if __name__ == '__main__':
#     main()
