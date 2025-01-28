# contours -
# these are simply a curve joining all the continous points
# (along the boundary), havinf same colors or intensity

# this is used to detect analyze the shapes and detect objects 
# find contors always detect the white object from black background

# import cv2
# import numpy as np
# img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image7.jpeg")
# img = cv2.resize(img, (400, 400))
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(img1,70,255,0)


# cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # contour is a NumPy array of (x, y) coordinates of points along the contour boundary.
# # cnts is the list which stores the coordinates
 
# img = cv2.drawContours(img,cnts,-1,(25,10,15),4)

# # if you want to detect the specific contour change the -1 digit 

# img = cv2.drawContours(img,cnts,5,(25,10,15),4)
 
# print(cnts)
# print(len(cnts))
# cv2.imshow("path_to_image", img)
# cv2.imshow("second image", img1)
# cv2.imshow("thresh image", thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# image contours function

# moment
# approximation 
# concvexnull

# import cv2
# import numpy as np

# # Load the image
# img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image4.jpg")
# img = cv2.resize(img, (400, 400))

# # Convert to grayscale
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply thresholding
# ret, thresh = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

# # Find contours
# cnts, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # Loop through contours to draw and label centers
# for c in cnts:
#     M = cv2.moments(c)
#     if M["m00"] != 0:
#         cx = int(M["m10"] / M["m00"])
#         cy = int(M["m01"] / M["m00"])
#         cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
#         cv2.circle(img, (cx, cy), 7, (255, 255, 255), 5)
#         cv2.putText(img, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# # Show images
# cv2.imshow("Original Image with Contours", img)
# cv2.imshow("Grayscale Image", img1)
# cv2.imshow("Threshold Image", thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# contour Area 


import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image4.jpg")
img = cv2.resize(img, (400, 400))

# Convert to grayscale
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
ret, thresh = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

# Find contours
cnts, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area1 = []
# Loop through contours to draw and label centers
for c in cnts:
    M = cv2.moments(c)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        # find area
        area = cv2.contourArea(c)
        area1.append(area)
        epsilon = 0.1*cv2.arcLength(c,True)
        data = cv2.approxPolyDP(c,epsilon,True)
        
        hull = cv2.convexHull(data)
        x,y,w,h = cv2.boundingRect(hull)
        
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(125,10,20,5))
        # cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
        
        # cv2.putText(img, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Show images
cv2.imshow("Original Image with Contours", img)
# cv2.imshow("Grayscale Image", img1)
# cv2.imshow("Threshold Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()