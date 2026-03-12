import cv2

img = cv2.imread("../images/test.jpg")

resized = cv2.resize(img,(400,400))

cv2.imwrite("../output/resized.jpg", resized)

print("Image resized")