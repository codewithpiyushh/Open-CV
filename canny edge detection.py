# this approch combines 5 steps:
# 1. it reduce the noise using gradient
# 2. non maximun suppresion
# 3. gradient calculation
# 4. double threshold
# 5. edge tracking

# it is use multi stage algorithum to detect a edges

# import cv2
# import numpy as np
# img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image7.jpeg")
# img = cv2.resize(img, (400, 400))
# img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# # parameters canny(img,thresh1,thresh2) thresh1 and thresh2 are different lvl

# can = cv2.Canny(img_grey,50,150)

# cv2.imshow("window_name", img_grey)
# cv2.imshow("canny_image", can)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Read the image from the given path
img = cv2.imread(input("Enter the path: "))
img = cv2.resize(img, (400, 400))  # Resize the image to 400x400 pixels

# Convert the image to grayscale for edge detection
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Function to do nothing; this is a placeholder for the trackbar callback
def nothing(x):
    pass

# Create a window for Canny edge detection
cv2.namedWindow("Canny")

# Create a trackbar to adjust the threshold for Canny edge detection
cv2.createTrackbar("Threshold", "Canny", 0, 255, nothing)

while True:
    # Get the current position of the trackbar
    threshold = cv2.getTrackbarPos("Threshold", "Canny")
    
    # Print the current threshold value to the console
    print(f"Current threshold: {threshold}")
    
    # Apply the Canny edge detection algorithm
    # Use the threshold value from the trackbar as the lower threshold
    res = cv2.Canny(img_grey, threshold, 255)
    
    # Display the resulting edge-detected image
    cv2.imshow("Canny", res)
    
    # Wait for a key event; exit if the 'Esc' key is pressed
    key = cv2.waitKey(1)
    if key == 27:  # ASCII value for 'Esc' key
        break

# Clean up and close all OpenCV windows
cv2.destroyAllWindows()
