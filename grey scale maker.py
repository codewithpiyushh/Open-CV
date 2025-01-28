import cv2

# Get the image path from the user
path = input("Enter the path: ")

# Read the image
img = cv2.imread(path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize the grayscale image to 800x700 pixels
    gray_img = cv2.resize(gray_img, (800, 700))
    # Display the modified image
    cv2.imshow("Converted Image", gray_img)
    k = cv2.waitKey(0)
    if k==ord("s"):
        cv2.imwrite('Downloads\\output.png',img)
    else:
        cv2.destroyAllWindows()
