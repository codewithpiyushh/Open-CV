import cv2
import datetime 

# Load the video
cap = cv2.VideoCapture("C:/Users/hp/Desktop/coding/opencv/video.mp4")

# print("width",cap.get(3)) # width of the original video 3 for width
# print("height",cap.get(4)) # height of the original video 4 for height

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Resize the frame to 600x600
        resized_frame = cv2.resize(frame, (800, 600))
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "height: "+ str(cap.get(4))+'   ' + 'width: '+ str(cap.get(3))
        
        resized_frame = cv2.putText(resized_frame,text,(10,40),font,1,(0,155,255),1,cv2.LINE_AA)
        date_data = "Date: "+str(datetime.datetime.now())
        resized_frame = cv2.putText(resized_frame,date_data,(10,80),font,1,(0,155,255),1,cv2.LINE_AA)
        # Display the resized frame
        cv2.imshow('Resized Frame', resized_frame)
        
        # Exit the loop when 'd' is pressed
        if cv2.waitKey(30) & 0xFF == ord('d'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()

