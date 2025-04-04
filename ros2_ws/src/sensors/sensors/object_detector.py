import rclpy
from rclpy.node import Node
from ultralytics import YOLO
from std_msgs.msg import String, Float64MultiArray, Bool
import cv2
import time

class ObjectDetector(Node):
    def __init__(self):
        super().__init__('object_detector')

        # Path on Pi
        self.model = YOLO('/home/pi2/cleaningoceanplastics/ros2_ws/src/sensors/resource/bestv12.pt')
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error("Error: Could not open webcam.")
            self.destroy_node()
            return
        
        self.save_video = False # Set to False to disable video recording

        if self.save_video:
            frame_width = int(self.cap.get(3))
            frame_height = int(self.cap.get(4))

            timestamp = time.strftime("%Y%m%d_%H%M%S")
            self.video_filename = f"detection_{timestamp}.mp4"
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = 5
            self.out = cv2.VideoWriter(self.video_filename, fourcc, fps, (frame_width, frame_height))
        
        self.detection_pub = self.create_publisher(String, 'object_detections', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.process_image)

        self.centroid_listener = self.create_subscription(Float64MultiArray, 'centroid', self.publish_centroid, 10)
        self.centroid = [320, 240]

        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

    def process_image(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 0)
            results = self.model(frame, verbose=False)

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

            if objectStrings != "":
                publishString.data = objectStrings
            self.detection_pub.publish(publishString)

            if self.save_video:
                annotated_frame = results[0].plot()  # YOLO outputs annotated images with .plot()
                self.out.write(frame)
                cx, cy = map(int, self.centroid)
                cv2.circle(annotated_frame, (cx, cy), 5, (0,0,255), -1)
                cv2.imshow("Real-Time Detection w/ YOLO", annotated_frame)
            
            cv2.waitKey(1)

    def publish_centroid(self, msg):
        self.centroid = msg.data
        

    def destroy_node(self,msg):
        if self.cap.isOpened():
            self.cap.release()
            if self.save_video:
                self.out.release()
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
