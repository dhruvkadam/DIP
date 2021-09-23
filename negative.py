import cv2

img9=cv2.imread('C:/Users/Dhruv/Desktop/bielsa.jpg')
cv2.imshow('og',img9)

img_neg=255-img9
cv2.imshow('negative' ,img_neg)
cv2.waitKey(0)

