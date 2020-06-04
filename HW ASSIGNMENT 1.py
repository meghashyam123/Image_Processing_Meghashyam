import cv2 
cap = cv2.VideoCapture(0)
counter = 0
user_input = int(input("Enter the no of frame"))
while True :
    counter = counter + 1
    x , frame = cap.read()
    if cv2.waitKey(1000) & 0xFF == ord('q') :
        break
    flipped = cv2.flip(frame,-1)
    if (counter <= user_input) :
        cv2.imshow("Image",frame)
    else :
        cv2 .imshow("Image",flipped) 