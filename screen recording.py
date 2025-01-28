import cv2 as c 
import pyautogui as p 
import numpy as np

# Create resolution
rc = p.size()
fn = input("Please enter the output file name (e.g., output.avi): ")
fps = 60.0

# Initialize the codec and create VideoWriter object
fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter(fn, fourcc, fps, rc)

# Create a window to display the recording
c.namedWindow("Live_recording", c.WINDOW_NORMAL)
c.resizeWindow("Live_recording", (600, 400))

while True:
    img = p.screenshot()  # Take a screenshot
    f = np.array(img)  # Convert the screenshot to a NumPy array
    f = c.cvtColor(f, c.COLOR_RGB2BGR)  # Convert color from RGB to BGR

    output.write(f)  # Write the frame to the video file
    c.imshow("Live_recording", f)  # Show the frame in the window

    if c.waitKey(1) == ord('d'):  # Break the loop if 'd' is pressed
        break

# Release resources
output.release()  # Correctly release the video writer
c.destroyAllWindows()  # Close all OpenCV windows
