from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()
try:
    detector = VideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath( os.path.join(execution_path , "yolov3.pt"))
    detector.loadModel()
except Exception as e:
    print(e)

try:
    video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "input_video.mp4"),
                                output_file_path=os.path.join(execution_path, "output_video"),
                                frames_per_second=20, log_progress=True, display_percentage_probability=False)
    print(video_path)
except Exception as e:
    print(e)