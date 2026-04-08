from picamera2 import Picamera2
import cv2
import numpy as np

class Camera:
    def __init__(self):
        self.picam2 = Picamera2()
        self.picam2.configure(
            self.picam2.create_preview_configuration(main={"size": (640, 480)})
        )
        self.picam2.start()

    def get_frame(self):
        frame = self.picam2.capture_array()
        frame = frame[:, :, :3]
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return np.ascontiguousarray(frame)