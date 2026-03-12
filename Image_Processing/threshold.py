import cv2

img = cv2.imread("../images/test.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

cv2.imwrite("../output/thresh.jpg", thresh)

print("Threshold image saved")