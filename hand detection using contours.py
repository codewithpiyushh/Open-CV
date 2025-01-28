import cv2
import numpy as np

# Load and preprocess the image
img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image9.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(img1, 7)
ret, thresh = cv2.threshold(blur, 240, 255, cv2.THRESH_BINARY_INV)

# Find contours
cnts, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    epsilon = 0.0001 * cv2.arcLength(c, True)
    data = cv2.approxPolyDP(c, epsilon, True)

    # Find convex hull and draw contours
    hull = cv2.convexHull(data)
    cv2.drawContours(img, [c], -1, (50, 50, 150), 2)
    cv2.drawContours(img, [hull], -1, (255, 0, 0), 2)

# Process convexity defects for the first contour
if len(cnts) > 0:
    hull2 = cv2.convexHull(cnts[0], returnPoints=False)
    defect = cv2.convexityDefects(cnts[0], hull2)

    if defect is not None:  # Check if there are defects
        for i in range(defect.shape[0]):
            s, e, f, d = defect[i, 0]
            print(s, e, f, d)
            start = tuple(cnts[0][s][0])
            end = tuple(cnts[0][e][0])
            far = tuple(cnts[0][f][0])
            cv2.circle(img, far, 5, [0, 0, 255], -1)

# Display contours and hierarchy
print("Contours:", cnts)
print("Number of contours:", len(cnts))
print("Hierarchy:", hier)

# Display images
cv2.imshow("Original Image with Contours", img)
cv2.imshow("Grayscale Image", img1)
cv2.imshow("Threshold Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
