import cv2
import numpy as np

# Capture the video from the webcam
vid = cv2.VideoCapture(0) 

def nothing(x):
    pass

# Create a window with trackbars for color adjustment
cv2.namedWindow("Color Adjustments", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustments", 300, 300)

# Trackbars for lower and upper HSV values
cv2.createTrackbar("Lower_H", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_S", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_V", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Upper_H", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_S", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_V", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Thresh", "Color Adjustments", 0, 255, nothing)

while vid.isOpened():
    ret, frame = vid.read()
    if not ret:
        break

    # Resize the frame for consistency
    frame = cv2.resize(frame, (400, 400))

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar positions for lower and upper HSV values
    l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustments")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustments")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustments")
    u_h = cv2.getTrackbarPos("Upper_H", "Color Adjustments")
    u_s = cv2.getTrackbarPos("Upper_S", "Color Adjustments")
    u_v = cv2.getTrackbarPos("Upper_V", "Color Adjustments")
    thresh_val = cv2.getTrackbarPos("Thresh", "Color Adjustments")

    # Define lower and upper bounds for HSV thresholding
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    # Create masks based on HSV range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    filtered = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Invert the mask for thresholding
    mask_inv = cv2.bitwise_not(mask)
    ret, thresh = cv2.threshold(mask_inv, thresh_val, 255, cv2.THRESH_BINARY)

    # Apply dilation to the thresholded image
    dilated = cv2.dilate(thresh, None, iterations=6)

    # Find contours on the thresholded image
    cnts, hier = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     
    frame = cv2.drawContours(frame,cnts,-1,(176,21,14),4)
    # Display the images
    cv2.imshow("Threshold", thresh)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filtered", filtered)
    cv2.imshow("Frame", frame)

    # Exit on pressing 'Esc' key
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release resources
vid.release()
cv2.destroyAllWindows()
