import os
import cv2
p=0
cam=cv2.VideoCapture("C:/Users/Dhruv/Desktop/MT/p.m4v")
x=0
while x<5:
    x+=1
    p+=5000
    cam.set(cv2.CAP_PROP_POS_MSEC,p)
    ret,frame= cam.read()
    cv2.imwrite("C:/Users/Dhruv/Desktop/MT/p"+str(x)+".jpg",frame)
cv2.destroyAllWindows()
