import cv2
img1=cv2.imread("")
img2=cv2.imread("")

fark=cv2.substract(img1,img2)

cv2.imshow("1",fark)


cv2.waitKey(0)
cv2.destroyAllWindows()
