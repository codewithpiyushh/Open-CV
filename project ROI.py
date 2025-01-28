# extracting object from the image and place on another image
# random figure ROI or background subtraction

import cv2
import numpy as np 
img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image2.jpg")
img2 = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image3.jpg")

img = cv2.resize(img,(800,600))
img2 = cv2.resize(img2,(600,400))

r,c,ch = img.shape
print(r,c,ch)

roi = img[0:r,0:c]
print(roi)


img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,mask = cv2.threshold(img_grey,50,255,cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img_bg = cv2.bitwise_and(img2,img2,mask = mask_inv)


img2_bg = cv2.bitwise_and(img2,img2,mask = mask_inv)

cv2.imshow("image1",img)
cv2.imshow("image2",img_grey)
cv2.imshow("mask",mask)
cv2.imshow("mask_inverse",mask_inv)
cv2.imshow("ROI",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()