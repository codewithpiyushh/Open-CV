import cv2
import numpy as np

# Read and resize the image
img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image3.webp")
img = cv2.resize(img, (1000, 700))

# Create a border with a specified color using BORDER_CONSTANT
# Border dimensions: top, bottom, left, right
brd = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[255, 0, 155])

# Display the image with the border
cv2.imshow("Image with Border", brd)
cv2.waitKey(0)
cv2.destroyAllWindows()
