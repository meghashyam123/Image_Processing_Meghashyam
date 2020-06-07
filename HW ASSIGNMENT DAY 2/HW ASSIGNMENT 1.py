import cv2
path= ("C:\Git\Image_Processing_Meghashyam\HW ASSIGNMENT DAY 2/tiger.jpg")
img=cv2.imread(path)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,255),10)
cv2.imshow("frame",img)
cv2.waitKey(0)