import cv2
import numpy as np

def cross(x):
    pass

# Initialize an image with extra space at the bottom for RGB and HEX values
img = np.zeros((650, 600, 3), np.uint8)  # Increased height to 650 for text display below
cv2.namedWindow("Color Picker")
font = cv2.FONT_HERSHEY_SIMPLEX

# Create a switch for turning color display ON/OFF
switch = "0 : OFF\n1 : ON"
cv2.createTrackbar(switch, "Color Picker", 0, 1, cross)

# Create trackbars for RGB color selection
cv2.createTrackbar("R", "Color Picker", 0, 255, cross)
cv2.createTrackbar("G", "Color Picker", 0, 255, cross)
cv2.createTrackbar("B", "Color Picker", 0, 255, cross)

while True:
    # Get the positions of the switch and RGB trackbars
    s = cv2.getTrackbarPos(switch, "Color Picker")
    r = cv2.getTrackbarPos("R", "Color Picker")
    g = cv2.getTrackbarPos("G", "Color Picker")
    b = cv2.getTrackbarPos("B", "Color Picker")
    
    # Update color display area (top 600x600 pixels) based on switch position
    if s == 0:
        img[:600, :] = 0  # Black screen if OFF
    else:
        img[:600, :] = [b, g, r]  # Color display if ON
    
    # Clear the bottom text area
    img[600:, :] = (50, 50, 50)  # Gray background for the text area

    # Display RGB and HEX color values below the color picker
    color_text = f"RGB: ({r}, {g}, {b}) | HEX: #{r:02X}{g:02X}{b:02X}"
    cv2.putText(img, color_text, (10, 635), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # Show the updated image in the window
    cv2.imshow("Color Picker", img)
    
    # Exit on pressing 'ESC'
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
