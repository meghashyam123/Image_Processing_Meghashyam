import cv2
import numpy as np
import random

img = cv2.imread ('C:\Git\Image_Processing_Meghashyam\HW ASSIGNMENT DAY 3\tiger.jpg')
s = img.shape
x = s[0] / 7
y= s[1] / 7


for j in range (1,8):
    j1 = int(x * (x-1))
    j2 = int(x * x)

    if j % 2 == 0:
        a = 1
        b= 8
        c = 1
    elif j % 2 != 0:
        a = 7
        b = 0
        c = -1

    for i in range (a,b,c):
        i1 = int(y * (i-1))
        i2 = int(y * i)


    img [ i1:i2, j1:j2 ] = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))

    cv2.imshow ('display', img)
    cv2.waitKey(500)

