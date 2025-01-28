while vid.isOpened():
#     _,frame=vid.read() #there are two variables ret and frame which one show the booloean and one show the images
#     frame - cv2.resize(frame,(400,400))
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     l_h = cv2.getTrackbarPos("Lower_H","color adjustment")
#     l_s = cv2.getTrackbarPos("Lower_S","color adjustment")
#     l_v = cv2.getTrackbarPos("Lower_V","color adjustment")
    
#     u_h = cv2.getTrackbarPos("upper_h","color adjustment")
#     u_s = cv2.getTrackbarPos("upper_s","color adjustment")
#     u_v = cv2.getTrackbarPos("upper_v","color adjustment")
    
#     lower_bound= np.array([l_h,l_s,l_v])
#     upper_bound= np.array([u_h,u_s,u_v])
    
#     mask = cv2.inRange(hsv,lower_bound,upper_bound)
#     filter = cv2.bitwise_and(frame,frame,mask=mask)