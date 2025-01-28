# bit-wise operations are AND,OR,NOT, and XOR


import cv2
import numpy as np

img = np.zeros((250,500,3),np.uint8)
img = cv2.rectangle(img,(150,100),(200,250),(255,255,0),-1)



img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2,(10,10),(170,190),(255,255,0),-1)

cv2.imshow("image 1",img)
cv2.imshow("image 2",img2)
# bit and
bitAND = cv2.bitwise_and(img,img2)
cv2.imshow("bit_and",bitAND)

# bit or 
bitor = cv2.bitwise_or(img,img2)
cv2.imshow("bit_or",bitor)

# bit not 
bitnot = cv2.bitwise_not(img,img2)
cv2.imshow("bit_not",bitnot)


# bit xor 
bitxor = cv2.bitwise_xor(img,img2)
cv2.imshow("bit_xor",bitxor)



cv2.waitKey(0)
cv2.destroyAllWindows()