import cv2

img = cv2.imread("../images/test.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("../output/gray.jpg", gray)

print("Grayscale image saved")