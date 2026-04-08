from flask import Flask, Response
import cv2

from camera_stream.camera import Camera
from detection.detect import Detector
from tracking.tracker import Tracker
from counting.counter import Counter

app = Flask(__name__)

camera = Camera()
detector = Detector()
tracker = Tracker()
counter = Counter(mode="side", line_pos=320)

def generate_frames():
    while True:
        frame = camera.get_frame()

        detections = detector.detect(frame)
        tracks = tracker.update(detections, frame.shape)

        for t in tracks:
            x, y, w, h = map(int, t.tlwh)
            obj_id = t.track_id

            cx = x + w // 2
            cy = y + h // 2
            bottom = y + h

            counter.update(obj_id, cx, cy, bottom)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, f"ID {obj_id}", (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        # Draw line
        cv2.line(frame, (counter.line, 0), (counter.line, 480), (0,0,255), 2)

        # Draw counts
        cv2.putText(frame, f"Entry: {counter.entry}", (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        cv2.putText(frame, f"Exit: {counter.exit}", (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)