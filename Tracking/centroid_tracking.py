import cv2

# initialize HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# open video
cap = cv2.VideoCapture("../videos/video.mp4")

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # resize for faster processing
    frame = cv2.resize(frame,(320,240))

    # detect people
    boxes, weights = hog.detectMultiScale(frame)

    for (x, y, w, h) in boxes:

        # centroid coordinates
        cx = int(x + w/2)
        cy = int(y + h/2)

        # draw bounding box
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        # draw centroid
        cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

    # save some frames
    if frame_count % 30 == 0:
        filename = "../output/tracking_" + str(frame_count) + ".jpg"
        cv2.imwrite(filename, frame)

    frame_count += 1

cap.release()

print("Centroid tracking completed")