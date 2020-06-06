  
import cv2 
import time
import math

cam = cv2.VideoCapture(0)
counter = 0

while True :
    counter = counter + 1
    startTime = time.time()
    for i in range(0, 5):
        print(i)
        time.sleep(2)
    endTime = time.time()
    passTime = endTime - startTime
    print("passTime= %s" % passTime)
    x , frame = cam.read()
    flipped = cv2.flip(frame,-1)
    if cv2.waitKey(5) & 0xFF == ord('q') :
        break
    if math.floor(passTime) % counter == 0 :
        cv2.imshow('display',flipped)
    else :
        cv2.imshow('display', frame)