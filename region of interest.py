import cv2
import numpy as np


img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image2.webp")
img2 = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image3.webp")


# (717,84)    (950,310)
# x = 200 y = 225
roi1 = img[84:310,717:950]

# #passing data into img
# # changing X
# img[84:310,917:1150] = roi1
# img[84:310,517:750] = roi1


#passing data into img
# changing Y
# img[309:535,917:1150] = roi


# changing the face in seconf image
#(680,70) (990,460)
img2[70:460,680:990] = roi1

cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()