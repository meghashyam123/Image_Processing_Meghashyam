import cv2
import numpy as np
cam=cv2.VideoCapture(0)
count = 0
while True:
    count = count + 1
    x,frame=cam.read()
    verticalflip1 = np.rot90(frame)
    verticalflip2=cv2.flip(verticalflip1,-1)
    if(count%2==0):
        cv2.imshow("img",verticalflip1)
    else:
        cv2.imshow("img",verticalflip2)
    key=cv2.waitKey(5000)
    if key==ord('q'):
        break
    

   
