import cv2 
import random
  

img = cv2.imread('C:\Git\Image_Processing_Meghashyam\HW ASSIGNMENT DAY 3\tiger.jpg')
s = img.shape
x = s[0] / 7
y = s[1] / 7

 
for i in range(1, 8):
    i1 = int(y * (i-1))
    i2= int(y* i)

    for j in range(1, 8):
        j1 = int(x* (j-1))
        j2 = int(x * j)

        img[ i1:i2,j1:j2 ] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

cv2.imshow('display', img)
cv2.waitKey(0)