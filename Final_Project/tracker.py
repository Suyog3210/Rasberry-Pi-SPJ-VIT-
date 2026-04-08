import sys
import numpy as np

sys.path.append("ByteTrack/yolox/tracker")
from byte_tracker import BYTETracker

class Tracker:
    def __init__(self):
        class Args:
            track_thresh = 0.5
            track_buffer = 30
            match_thresh = 0.8
            frame_rate = 10
            mot20 = False

        self.tracker = BYTETracker(Args())

    def update(self, detections, frame_shape):
        if len(detections) > 0:
            return self.tracker.update(
                np.array(detections),
                [frame_shape[0], frame_shape[1]],
                (frame_shape[0], frame_shape[1])
            )
        return []