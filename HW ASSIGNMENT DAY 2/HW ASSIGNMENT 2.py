import cv2
cam= cv2.VideoCapture (0)
count = 1
pathFormat =('C:\Git\Image_Processing_Meghashyam\HW ASSIGNMENT DAY 2\tiger.jpg')
while count<=100:
    x,frame=cam.read()
    path=pathFormat.format(count)
    cv2.imwrite(path,frame)
    count = count + 1
print(x)