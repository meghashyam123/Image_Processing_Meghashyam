import cv2
import numpy as np 

cam=cv2.VideoCapture(0)

def mouse(event,x,y,flags,param):
    global points,flag
    if event==cv2.EVENT_LBUTTONDOWN:
        print(display[y,x])

cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse)

while True:
    x,display= cam.read()
    cv2.imshow('img',display)
    if cv2.waitKey(5000) & 0xFF==ord('q'):
        break