import cv2
import numpy as np
cam=cv2.VideoCapture(0)
count = 0
while True:
    count = count + 1
    x,frame=cam.read()
    horizontalflip1 = np.rot90(frame)
    horizontalflip2=cv2.flip(horizontalflip1,-1)
    if(count%2==0):
        cv2.imshow("img",horizontalflip1)
    else:
        cv2.imshow("img",horizontalflip2)
    key=cv2.waitKey(5000)
    if key==ord('q'):
        break
    

   