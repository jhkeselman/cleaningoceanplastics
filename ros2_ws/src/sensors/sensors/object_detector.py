import rclpy
from rclpy.node import Node
from ultralytics import YOLO
from std_msgs.msg import String, Float64MultiArray, Bool
import cv2
import time

# This node handles real-time object detection using the YOLO model
# It captures video from the camera, processes each frame using the custom YOLO model, and publishes a string with info about the detected objects
# Publishers: 'object_detections'
# Subscribers: 'centroid', 'emergency_stop'
class ObjectDetector(Node):
    def __init__(self):
        super().__init__('object_detector')

        # Loads the YOLO weights from the specified path (on the Raspberry Pi)
        # Using YOLO12, with version 12 of our custom weights
        self.model = YOLO('/home/pi2/cleaningoceanplastics/ros2_ws/src/sensors/resource/bestv12.pt')
        # Opens the webcam footage at index 0 (for the Pi) 
        self.cap = cv2.VideoCapture(0)
        # If webcame cannot open the node is shut down
        if not self.cap.isOpened():
            self.get_logger().error("Error: Could not open webcam.")
            self.destroy_node()
            return
        
        # Flag to control displaying the video
        # Set to True to enable video display
        self.show_video = True

        # Flag to control saving the video to a file
        # Set to True to enable video recording
        self.save_video = True

        # Flag to control saving annotated vs. unannotated video
        # Set to True to save the annotated video
        self.save_annotated = False

        # If video recording is enabled, set up the video writer
        # The video will be saved in the current directory labeled with the current timestamp as an .mp4 file (ignored by .gitignore)
        if self.save_video:
            frame_width = int(self.cap.get(3))
            frame_height = int(self.cap.get(4))

            timestamp = time.strftime("%Y%m%d_%H%M%S")
            self.video_filename = f"detection_{timestamp}.mp4"
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = 5
            self.out = cv2.VideoWriter(self.video_filename, fourcc, fps, (frame_width, frame_height))
        
        # Publisher for detected objects
        # Message type: String
        self.detection_pub = self.create_publisher(String, 'object_detections', 10)
        
        # Timer to process the image every 0.1 seconds (artificially 10 FPS)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.process_image)

        # Subscription to the 'centroid' topic
        # Used during debugging to visualize the centroid of the detected objects
        self.centroid_listener = self.create_subscription(Float64MultiArray, 'centroid', self.update_centroid, 10)
        self.centroid = [320, 240]

        # Subscription to emergency stop topic
        # If emergency stop is triggered, the node will be destroyed and the camera will be released and recording saved
        self.emergency_stop = self.create_subscription(
            Bool,
            'emergency_stop',
            self.destroy_node,
            10
        )

    # Processes the image from the camera
    def process_image(self):
        # Read a frame from the camera
        ret, frame = self.cap.read()
        # If the frame is read successfully, process it
        if ret:
            # Flip the frame vertically (raw image is update down due to camera orientation)
            frame = cv2.flip(frame, 0)
            # Passes the frame to the YOLO model for processing and returns detected objects
            results = self.model(frame, verbose=False)

            # Initializes the output msg String for detected objects
            publishString = String()
            objectStrings = ""

            # Loop over detected objects
            for box in results[0].boxes:
                # Class label, confidence, and bounding box coordinates
                class_label = self.model.names[int(box.cls[0])]
                raw_conf = box.conf[0]
                conf = 100 * round(raw_conf.item(), 2)
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                # Format object information into a single string
                objectString = f"{class_label}, {conf}, {x1}, {y1}, {x2}, {y2}"
                # Append the object string to the output string
                # Each object is separated by a $ symbol
                if objectStrings:
                    objectStrings += " $ " + objectString
                else:
                    objectStrings = objectString

            # Publish the object strings to the 'object_detections' topic
            # If there are no detected objects, publish an empty string
            if objectStrings != "":
                publishString.data = objectStrings
                self.detection_pub.publish(publishString)


            # Annotate the frame with bounding boxes and labels
            annotated_frame = results[0].plot()
            # If video recording is enabled, write the frame to the video file
            if self.save_video:
                if self.save_annotated:
                    # Save the annotated frame to the video file
                    self.out.write(annotated_frame)
                else:
                    # Save the raw frame to the video file
                    self.out.write(frame)
            # If video display is enabled, show the annotated frame
            if self.show_video:
                # Display the annotated frame (with labeled bounding boxes) and the centroid of the detected items
                cx, cy = map(int, self.centroid)
                cv2.circle(annotated_frame, (cx, cy), 5, (0,0,255), -1)
                cv2.imshow("Real-Time Detection w/ YOLO", annotated_frame)
            
            # 1 ms delay to allow for smoother video playback, helps prevent issues with lag due to detection speed
            cv2.waitKey(1)

    # Updates the centroid of the detected objects
    # Input: [Float64MultiArray] msg containing the centroid coordinates
    def update_centroid(self, msg):
        self.centroid = msg.data

    # Destroy the node when the emergency stop is triggered
    # Stops the camera and ends video recording if enabled
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
