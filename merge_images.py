import cv2
import numpy as np

# Create a white background for the circle
circle_img = np.zeros((512, 512, 3), np.uint8) + 255
cv2.circle(circle_img, (256, 256), 50, (255, 0, 0), -1)

# Create a white background for the rectangle
rectangle_img = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle_img, (150, 150), (350, 350), (0, 255, 0), -1)

# Blend the two images with weights
blended_img = cv2.addWeighted(circle_img, 0.6, rectangle_img, 0.4, 0)

# Display the result
cv2.imshow("Blended Image", blended_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
