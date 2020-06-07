  
import cv2
import time
start_time=time.time()
cam= cv2.VideoCapture(0)
while True:
        x, display= cam.read()
        flipped= cv2.flip(display,-1) 
        end_time=time.time()
        diff=int(end_time-start_time)
        if diff%5==0:
            cv2.imshow("display",flipped)
        else:
            cv2.imshow("display",display)
         
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break 