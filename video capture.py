# ret indicated whether the frame was successfully captured

# importing a video and greyscaling it 
import cv2
vid = cv2.VideoCapture(r'C:\Users\hp\Desktop\coding\opencv\video.mp4')
print('vid',vid)
while True:
    ret,frame=vid.read() #there are two variables ret and frame which one show the booloean and one show the images
    frame = cv2.resize(frame,(500,500))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame',frame)
    cv2.imshow("gray",gray)
    k = cv2.waitKey(10)
    if k==ord('d'):
        break

vid.release()
vid.destroy



# using webcam for it 
import cv2
vid = cv2.VideoCapture(0) #capture the video 

# DIVX, XVID , MJPG ,X264, WMV1,WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480),0)
print('vid',vid)
while vid.isOpened():
    ret,frame=vid.read() #there are two variables ret and frame which one show the booloean and one show the images
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # gray scaling
        frame = cv2.flip(frame,0)
        cv2.imshow('Frame',frame)
        cv2.imshow("gray",gray)
        output.write(frame)
        k  = cv2.waitKey(10)
        if k==ord('d'):
            break

vid.release()
output.release()
vid.destroy

#connecting mobile webcam with the laptop 

import cv2
camera = "https://192.168.1.5:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camera)
print("check===",cap.isOpened())\

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output2 = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480),0)
print('vid',cap)

while cap.isOpened():
    ret,frame=cap.read() #there are two variables ret and frame which one show the booloean and one show the images
    if ret == True:
        cv2.imshow('Colorframe',frame)
        k  = cv2.waitKey(10)
        if k==ord('d'):
            break

cap.release()
output2.release()
cap.destroy

import cv2
import numpy as np

camera = "https://192.168.1.5:8080/video"
# Initialize the video capture directly from the IP camera URL
cap = cv2.VideoCapture(camera)

# Verify if the capture is opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # Set up the video writer with XVID codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter(r'C:\Users\hp\Desktop\coding\opencv\output.avi', fourcc, 20.0, (640, 480), True)

    # Create an empty (black) frame to initialize the video
    empty_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    output.write(empty_frame)  # This will only be used if no frames are read from the camera

    while cap.isOpened():
        # Read the frame
        ret, frame = cap.read()
        if ret:
            # Resize frame to match output dimensions (optional if needed)
            frame = cv2.resize(frame, (640, 480))
            
            # Show and save each frame
            cv2.imshow('Video Frame', frame)
            output.write(frame)

            # Press 'd' to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('d'):
                break
        else:
            print("No frame received from the camera.")
            break

    # Release resources after finishing
    cap.release()
    output.release()
    cv2.destroyAllWindows()

 
# capturing video from youtube without download
import yt_dlp as youtube_dl
import pafy
import cv2
url = 'https://www.youtube.com/watch?v=YTDHcEJs684'
data = pafy.new(url)
data = data.getbest(preftype='mp4')
cap = cv2.VideoCapture(0)
cap.open(data.url)
if not cap.isOpened():
    print("Error: Could not open video.")

while cap.isOpened():
        # Read the frame
    ret, frame = cap.read()
    if ret == True:
            # Resize frame to match output dimensions (optional if needed)
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            # Show and save each frame
        cv2.imshow('Video Frame', frame)
        cv2.imshow('gray',gray)
       
            # Press 'd' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('d'):
            break
        else:
            print("No frame received from the camera.")
            break

    # Release resources after finishing
    cap.release()
    cv2.destroyAllWindows()

