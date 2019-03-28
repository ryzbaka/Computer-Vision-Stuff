import cv2
import numpy as np
img=cv2.imread("propic.png",1)

cv2.line(img,(0,0),(150,150),(255,255,255),15)
#cv2.line(image,(start coord),(end coord),(BGR color),thickness)

cv2.rectangle(img,(15,25),(200,150),(0,0,255),5)
#cv2.rectanle(image,(top left coord),(bottom right coord),(BGR color),thickness)

cv2.circle(img,(100,63),55,(0,255,0),3)
#cv2.circle(image,(centre coord),radius,(BGR),thickness)

#Now we'll draw some polygon
#first we'll make a numpy array of the points
pts=np.array([[20,30],[40,70],[80,20],[100,50]],np.int64)
cv2.polylines(img,[pts],True,(0,255,255),3)
#cv2.polylines(image,points,connect first and last point?,BGR color,thickness)

#alright, so we're done with all the drawing so lets write something

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"OPENCV",(0,130),font,1,(200,255,255),2,cv2.LINE_AA)
#cv2.putText(img,text,(start coord),font,size,BGR,thickness,anti aliasing)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
