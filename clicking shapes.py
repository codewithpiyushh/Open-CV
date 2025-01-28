import cv2
import numpy as np

# Set font
font = cv2.FONT_ITALIC

# Create a black image of size 600x600
img = np.zeros((600, 600, 3), dtype=np.uint8)

# Define mouse callback function
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left button click
        print(f"Coordinates: x={x}, y={y}")
        # Show coordinates on the image at the clicked position
        coord_text = f". {x}, {y}"
        cv2.putText(img, coord_text, (x, y), font, 1, (155, 200, 220), 2)

    if event == cv2.EVENT_RBUTTONDOWN:  # Right button click
        # Extract BGR values from the image at the clicked position
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        
        # Display color values at the clicked position
        color_text = f". {b}, {g}, {r}"
        cv2.putText(img, color_text, (x, y), font, 1, (154, 214, 220), 2)

# Create a window
cv2.namedWindow("res")

# Set the mouse callback function to the window
cv2.setMouseCallback("res", mouse_event)

# Display loop
while True:
    cv2.imshow("res", img)
    # Exit the loop when 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cv2.destroyAllWindows()
