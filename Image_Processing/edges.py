import cv2

img = cv2.imread("../images/test.jpg")

edges = cv2.Canny(img,100,200)

cv2.imwrite("../output/edges.jpg", edges)

print("Edge detection done")