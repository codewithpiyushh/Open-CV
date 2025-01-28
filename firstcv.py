# import cv2 
# # read image 
# img = cv2.imread(r"C:/Users/hp/Desktop/coding/opencv/image.png",0)
# original_height, original_width = img.shape[:2]
# new_height = 600 
# resized_image = cv2.resize(img, (original_width, new_height))
# img

# cv2.imshow("original",img)
# cv2.waitKey(5000)
# cv2.destroyAllWindows

import cv2
import numpy as np
import yt_dlp

url = 'https://youtu.be/YTDHcEJs684?si=gH_FmIZUXP3LhfUW'

# Using yt-dlp to fetch the video stream URL
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # You can adjust this option
    'noplaylist': True,                     # Download single video
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    video_url = info_dict['https://www.youtube.com/watch?v=YTDHcEJs684']  # The direct video URL

# Open the video stream using OpenCV
cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("Error: Could not open video.")
else:
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter(r'C:\Users\hp\Desktop\coding\opencv\output.avi', fourcc, 20.0, (640, 480), True)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            cv2.imshow('Video Frame', frame)
            output.write(frame)

            if cv2.waitKey(1) & 0xFF == ord('d'):
                break
        else:
            print("No frame received from the video.")
            break

    cap.release()
    output.release()
    cv2.destroyAllWindows()
