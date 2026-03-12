import cv2

# open video
cap = cv2.VideoCapture("../videos/video.mp4")

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # save frame
    filename = "../output/frame_" + str(frame_count) + ".jpg"
    cv2.imwrite(filename, gray)

    frame_count += 1

cap.release()

print("Frames extracted:", frame_count)