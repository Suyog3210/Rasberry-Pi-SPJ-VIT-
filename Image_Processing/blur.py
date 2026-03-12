import cv2

img = cv2.imread("../images/test.jpg")

blur = cv2.GaussianBlur(img,(11,11),0)

cv2.imwrite("../output/blur.jpg", blur)

print("Blur image saved")