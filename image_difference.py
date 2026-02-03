import cv2
img1=cv2.imread("")
img2=cv2.imread("")

different=cv2.substract(img1,img2)

cv2.imshow("1",different)


cv2.waitKey(0)
cv2.destroyAllWindows()
