import cv2
import numpy as np
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    out.write(frame)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows() 
