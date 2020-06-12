import cv2
import numpy as np


img = cv2.imread('C:\Git\Image_Processing_Meghashyam\HW ASSIGNMENT DAY 4\tiger.jpg')
cv2.imshow('display',img)
pt1=[(203,92),(1054,157),(1216,601),(268,714)]
pt2=[(0,0),(1080,0),(0,720),(1080,720)]
def mouse(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        pt.append((x,y))
        print(x,y)

        if len(points)==2:
            x1,y1=points[0]
            x2,y2=points[1]
            warp=img_cpy[points[0][1]:points[1][1],points[0][0]:points[1][0]]
            cv2.imshow("Warpped",warp)


cv2.namedWindow('display')
cv2.setMouseCallback('display', mouse)

transform = cv2.getPerspectiveTransform(pt1, pt2)
last= cv2.warpPerspective(img, transform, (720, 1080))


cv2.imshow('display', img)
cv2.imshow('Warpped', last)
cv2.waitKey(0)
