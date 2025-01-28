# # hue saturation value 
# import cv2
# import numpy as np

# img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image4.jpg")

# def blend(x):
#     pass

# # Create a window and trackbars
# cv2.namedWindow("Color Adjustment")
# cv2.createTrackbar('Lower_H', 'Color Adjustment', 0, 225, blend)
# cv2.createTrackbar('Lower_S', 'Color Adjustment', 0, 225, blend)
# cv2.createTrackbar('Lower_V', 'Color Adjustment', 0, 225, blend)

# cv2.createTrackbar('Higher_H', 'Color Adjustment', 225, 225, blend)
# cv2.createTrackbar('Higher_S', 'Color Adjustment', 225, 225, blend)
# cv2.createTrackbar('Higher_V', 'Color Adjustment', 225, 225, blend)

# while True:
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
#     # Retrieve trackbar positions
#     l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustment")
#     l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustment")
#     l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustment")
    
#     u_h = cv2.getTrackbarPos("Higher_H", "Color Adjustment")
#     u_s = cv2.getTrackbarPos("Higher_S", "Color Adjustment")
#     u_v = cv2.getTrackbarPos("Higher_V", "Color Adjustment")

#     # Define lower and upper bounds for HSV filtering
#     lower_bound = np.array([l_h, l_s, l_v])
#     upper_bound = np.array([u_h, u_s, u_v])
    
#     # Apply mask and result
#     mask = cv2.inRange(hsv, lower_bound, upper_bound)
#     res = cv2.bitwise_and(img, img, mask=mask)
    
#     # Display the images
#     cv2.imshow("image", img)
#     cv2.imshow("mask", mask)
#     cv2.imshow("res", res)
    
#     # Exit on pressing 'ESC' key
#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# cv2.destroyAllWindows()


import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def blend(x):
    pass

# Create a window and trackbars
cv2.namedWindow("Color Adjustment")
cv2.createTrackbar('Lower_H', 'Color Adjustment', 0, 225, blend)
cv2.createTrackbar('Lower_S', 'Color Adjustment', 0, 225, blend)
cv2.createTrackbar('Lower_V', 'Color Adjustment', 0, 225, blend)

cv2.createTrackbar('Higher_H', 'Color Adjustment', 225, 225, blend)
cv2.createTrackbar('Higher_S', 'Color Adjustment', 225, 225, blend)
cv2.createTrackbar('Higher_V', 'Color Adjustment', 225, 225, blend)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (400, 400))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Pass `frame` instead of `cap`
    
    # Retrieve trackbar positions
    l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustment")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustment")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustment")
    
    u_h = cv2.getTrackbarPos("Higher_H", "Color Adjustment")
    u_s = cv2.getTrackbarPos("Higher_S", "Color Adjustment")
    u_v = cv2.getTrackbarPos("Higher_V", "Color Adjustment")

    # Define lower and upper bounds for HSV filtering
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    
    # Apply mask and result
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Display the images
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)
    
    # Exit on pressing 'ESC' key
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
