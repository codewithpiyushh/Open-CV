
# Image pyramids in OpenCV are a multi-scale representation of images, 
# useful for various image processing tasks, such as image blending, 
# object detection, and feature extraction. The idea behind image pyramids
# is to create a series of images that are progressively reduced in size, 
# allowing for the analysis of an image at different scales.


import cv2
import numpy as np
# img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image3.jpg")
# img = cv2.resize(img, (6 00, 400))

# py_down = cv2.pyrDown(img)
# py_down2 = cv2.pyrDown(py_down)

# py_up = cv2.pyrUp(img)
# py_up2 = cv2.pyrUp(py_up)


# cv2.imshow("window_name", img)
# cv2.imshow("pyramid", py_down)
# cv2.imshow("pyramid", py_down2)

# cv2.imshow("pyramid up", py_up)
# cv2.imshow("pyramid up", py_up2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image3.jpg")
img = cv2.resize(img,(600, 400))

img1 = img.copy()
data = [img]
for i in range(4):
    img1 = cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow("res"+str(i),img1)
    
cv2.waitKey(0)
cv2.destroyAllWindows()