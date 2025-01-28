# image edge detection can be done by using laplaze or sobelX and sobelY


import cv2
import numpy as np
img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image7.jpeg")
img = cv2.resize(img,(400, 400))

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# laplaze 


lap = cv2.Laplacian(img_grey,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))


# sobel operations - 
# it is a joint gaussian smoothing plus differentiation operation,
# it is more resistant to noise
# this is use for x and y both
# parmeters(img,type for -ve val , x = 1,y=0,ksize)
# sobel X focus on vertical lines 
# sobel Y focus on horizontal lines

sobelX = cv2.Sobel(img_grey,cv2.CV_64F,1,0,ksize=3) # here 1 means X direction 
sobelY = cv2.Sobel(img_grey,cv2.CV_64F,0,1,ksize=3) # here 1 means Y direction 

sobelX = np.uint8(np.absolute(lap))
sobelY = np.uint8(np.absolute(lap))
               
add = cv2.bitwise_or(sobelX,sobelY)               
cv2.imshow("window_name", img)
cv2.imshow("adding", add)
cv2.imshow("sobelX", sobelX)
cv2.imshow("sobelY", sobelY)
# cv2.imshow("grey scale image", img_grey)
cv2.imshow("laplaze image", lap)
cv2.waitKey(0)
cv2.destroyAllWindows()