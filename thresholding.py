# thresholding is of 3 types - simple, adaptive
# simple threshold(img,pixel_threshold,max threshold pixel style)

# import numpy as np
# import cv2

# img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image2.jpg")
# img = cv2.resize(img, (500, 500))

# _, th1 = cv2.threshold(img,50,225,cv2.THRESH_BINARY)
# _, th2 = cv2.threshold(img,50,225,cv2.THRESH_BINARY_INV)


# cv2.imshow("image", img)
# cv2.imshow("threshold", th1)
# cv2.imshow("threshold2", th2)


# cv2.waitKey(0)
# cv2.destroyAllWindows()

# adaptive threshold : data loss is less 

import numpy as np
import cv2

img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image5.jpeg")
img = cv2.resize(img, (500, 500))

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple binary threshold
_, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Adaptive threshold with mean calculation
th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Adaptive threshold with Gaussian calculation
th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Simple Threshold", th1)
cv2.imshow("Adaptive Mean Threshold", th2)
cv2.imshow("Adaptive Gaussian Threshold", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
