import cv2

cap = cv2.VideoCapture("../videos/video.mp4")

# get video properties
width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("../output/output.avi", fourcc, fps, (width, height))

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # convert grayscale to BGR (required for VideoWriter)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    out.write(gray_bgr)

cap.release()
out.release()

print("Processed video saved")