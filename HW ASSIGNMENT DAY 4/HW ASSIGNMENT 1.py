import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

def mouse(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(display[y,x])

cv2.namedWindow('cam')
cv2.setMouseCallback('cam',mouse)

while True:
    x,display= cap.read()
    cv2.imshow('cam',display)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
