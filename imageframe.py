import os
import cv2
k=0
cam=cv2.VideoCapture("C:/Users/Dhruv/Desktop/MT/k.avi")
x=0
while x<5:
    x+=1
    k+=5000
    cam.set(cv2.CAP_PROP_POS_MSEC,k)
    ret,frame= cam.read()
    cv2.imwrite("C:/Users/Dhruv/Desktop/MT/k"+str(x)+".jpg",frame)
cv2.destroyAllWindows()
