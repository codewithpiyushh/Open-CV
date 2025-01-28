import cv2
import numpy as np 

# Read and resize images to ensure they are the same size
img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image2.jpg")
img2 = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image3.jpg")
img = cv2.resize(img, (500, 500))
img2 = cv2.resize(img2, (500, 500))

# Define a dummy function for the trackbar callback
def blend(x):
    pass

# Create a window and trackbars
cv2.namedWindow("win")
cv2.createTrackbar('alpha', 'win', 0, 100, blend)  # Trackbar for alpha value
switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'win', 0, 1, blend)  # Switch trackbar

while True:
    # Get the switch and alpha values
    s = cv2.getTrackbarPos(switch, 'win')
    alpha = cv2.getTrackbarPos('alpha', 'win') / 100.0  # Normalize alpha to [0, 1]
    print(f"Alpha: {alpha}")

    if s == 0:
        # Show the first image if switch is off
        dst = img.copy()
    else:
        # Blend the images using the alpha value
        dst = cv2.addWeighted(img, 1 - alpha, img2, alpha, 0)
        cv2.putText(dst, f"Alpha: {alpha:.2f}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Display the result
    cv2.imshow("win", dst)

    # Break on ESC key press
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
