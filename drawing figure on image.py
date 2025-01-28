import cv2
import numpy as np 

img  = cv2.imread("C:/Users/hp/Desktop/coding/opencv/image2.webp")
img = cv2.resize(img,(600,500))

# creating a blank image 
img = np.zeros([512,512,3],np.uint8)*225 #black image 

img = np.ones([512,512,3],np.uint8)*225 #white image
 
img = cv2.line(img,(0,250),(600,250),(100,0,0),100)
img = cv2.arrowedLine(img,(0,250),(600,250),(100,100,100),10)
img = cv2.rectangle(img,(0,250),(600,250),(100,100,100),50)
img = cv2.circle(img,(250,250),56,(100,100,100),50)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'thor',(100,500),font,4,(0,0,100),10,cv2.LINE_AA)
img = cv2.ellipse(img,(400,300),(100,50),50,0,100,155,5)
cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()