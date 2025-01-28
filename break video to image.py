import cv2
vidcap = cv2.VideoCapture("video.mp4")
ret,image = vidcap.read()
count = 0
playback_speed = 30 
while True:
    if ret == True:
        cv2.imwrite("C:/Users/hp/Desktop/coding/opencv/frame/imgN%d.jpg"%count,image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidcap.read()
        cv2.imshow("res",image)
        count +=1
        if cv2.waitKey(playback_speed) & 0xFF == ord("d"):
            break
            cv2.destroyAllWindows()
            
vidcap.release()
cv2.destroyAllWindows()
        