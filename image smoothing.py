# image smoothing or bluring is most common used operation 
# LOW pass filter which is use to remove noise from the image 
# HIGH pass filter which use to detech and finding edges in an image 

import cv2
import numpy as np

img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image6.png")
img = cv2.resize(img,(400,400))

kernel = np.ones((6,6),np.float32)/36
h_filter = cv2.filter2D(img,-1,kernel)

C_blur = cv2.blur(img,(4,4))

# gaussian blur filter
gau = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow("image",img)
cv2.imshow("blur",C_blur)
cv2.imshow("gaussian",gau)
cv2.imshow("filtered",h_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()