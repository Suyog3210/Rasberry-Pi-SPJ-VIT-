===============================
PEOPLE COUNTER SYSTEM PIPELINE
===============================

--------------------------------
1. OVERALL PIPELINE
--------------------------------

Camera → Frame Capture → Detection → Tracking → Counting → Streaming Output


--------------------------------
2. CAMERA MODULE (camera.py)
--------------------------------

Purpose:
Capture real-time frames from Raspberry Pi camera.

Working:
- Picamera2 initializes the camera.
- Frame is captured using capture_array().
- Frame format is converted:
    RGBA → BGR (required for OpenCV)
- Frame is returned as NumPy array.

Key Function:
get_frame()

Output:
Image frame (640x480)


--------------------------------
3. DETECTION MODULE (detect.py)
--------------------------------

Purpose:
Detect people in each frame using a lightweight AI model.

Model Used:
MobileNet SSD (TFLite)

Working:
1. Resize frame to model input size.
2. Convert to uint8 tensor.
3. Run inference using TFLite interpreter.
4. Extract:
   - bounding boxes
   - class IDs
   - confidence scores
5. Filter only "person" class (class_id = 0).
6. Convert normalized coordinates → pixel coordinates.

Output:
List of detections:
[x1, y1, x2, y2, confidence]


--------------------------------
4. TRACKING MODULE (tracker.py)
--------------------------------

Purpose:
Track each detected person across frames and assign unique IDs.

Algorithm:
ByteTrack (modified version without PyTorch)

Working:
- Takes detections as input.
- Uses:
    - Kalman Filter (motion prediction)
    - IoU matching (object association)
- Assigns consistent ID to each person.
- Handles:
    - overlapping people
    - temporary detection loss

Output:
Tracked objects:
- bounding box (tlwh)
- unique track_id


--------------------------------
5. COUNTING MODULE (counter.py)
--------------------------------

Purpose:
Count people entering and exiting using line crossing.

Modes:
1. SIDE CAMERA:
   - People move LEFT ↔ RIGHT
   - Uses X-axis crossing

2. TOP CAMERA:
   - People move UP ↕ DOWN
   - Uses Y-axis (bottom point)

Working:
For each tracked object:
- Store previous position
- Compare with current position

If crossing occurs:
- LEFT → RIGHT = Entry
- RIGHT → LEFT = Exit

Important:
- Each object counted only once using "counted" flag

Output:
entry count
exit count


--------------------------------
6. MAIN MODULE (main.py)
--------------------------------

Purpose:
Connect all modules and run system.

Workflow:
1. Capture frame from camera
2. Detect people
3. Track objects
4. Update counting logic
5. Draw:
   - bounding boxes
   - IDs
   - counting line
   - entry/exit counts
6. Encode frame as JPEG
7. Stream using Flask

Output:
Live video stream at:
http://<raspberry_pi_ip>:5000


--------------------------------
7. LINE CROSSING LOGIC
--------------------------------

SIDE CAMERA:
prev_x < line AND current_x >= line → Entry
prev_x > line AND current_x <= line → Exit

TOP CAMERA:
prev_y < line AND bottom >= line → Entry
prev_y > line AND bottom <= line → Exit
