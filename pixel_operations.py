import cv2
import numpy as np

img =cv2.imread("photo.jpg")

for i in range(30):
    img[200, i+100 ,0 ] = 0
    img[200, i + 100, 1] = 0
    img[200, i + 100, 2] = 0
cv2.imshow("araba",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
