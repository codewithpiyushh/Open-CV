import cv2 
import numpy as np 
from matplotlib import pyplot as plt

# # Load the image in grayscale mode (required for binary transformations)
# img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image4.jpg", 0)
# img = cv2.resize(img, (400, 400))  # Resize for easier visualization

# # Erosion and dilation are part of morphological transformations
# # These transformations rely on a structuring element (kernel) to modify the image shape
# # They are typically applied to binary images (black and white)

# # Threshold the image to create a binary mask
# # Any pixel intensity above 230 becomes white (foreground), and below becomes black (background)
# _, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)

# # Define the structuring element (kernel) used for the transformations
# # A larger kernel (e.g., 3x3) will create more noticeable effects in erosion and dilation
# kernel = np.ones((3, 3), np.uint8)  # A 3x3 matrix of ones, defining the shape of the operation

# # EROSION: This operation erodes away the boundaries of the foreground object
# # - Foreground (object of interest) should be white, background should be black
# # - It reduces white regions in the image, "shrinking" them
# # - Useful for removing small white noise in the background
# eroded_img = cv2.erode(mask, kernel)

# # DILATION: The opposite of erosion
# # - It expands the white regions in the binary image, "growing" the object
# # - Helpful to close small holes within white regions
# # - Often used after erosion to smooth the object boundaries
# dilated_img = cv2.dilate(mask, kernel)

# # Display the images using OpenCV windows
# cv2.imshow("Original Image", img)
# cv2.imshow("Binary Mask", mask)
# cv2.imshow("Eroded Image", eroded_img)
# cv2.imshow("Dilated Image", dilated_img)

# # Use matplotlib to plot and compare images side-by-side for better visualization
# # Titles and images lists for creating subplots
# titles = ["Original Image", "Binary Mask", "Erosion", "Dilation"]
# images = [img, mask, eroded_img, dilated_img]

# # Set up a figure with a size suitable for 4 images in a row
# plt.figure(figsize=(12, 4))
# for i in range(4):
#     plt.subplot(1, 4, i+1)  # Create subplots in a 1x4 grid
#     plt.imshow(images[i], 'gray')  # Show image in grayscale
#     plt.title(titles[i])  # Set title for each subplot
#     plt.xticks([]), plt.yticks([])  # Remove x and y ticks for clarity

# # Display the plotted images
# plt.show()

# # Wait for the user to press 'ESC' key to close OpenCV windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# OPENING 
# OPENING is just another name of erosion followed by dialation 
# means first erosion take place then dialation

img = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image4.jpg", 0)
img = cv2.resize(img, (400, 400))
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
kernel = np.ones((3, 3), np.uint8)  
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)


# CLOSING 
# CLOSING is just another name of dilation followed by erosion  
# means first dilation take place then erosion


kernel = np.ones((3, 3), np.uint8)  
b = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel) # difference between the mask and opening 
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) # difference between the dilation and erosion 
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel) # difference between the input image and closing 


cv2.imshow("image",img)
cv2.imshow("masking",mask)
cv2.imshow("morphology",o)
cv2.imshow("x1",x1)
cv2.imshow("x2",x2)
cv2.imshow("x3",x3)
cv2.imshow("morphology2",b)
cv2.waitKey(0)
cv2.destroyAllWindows()