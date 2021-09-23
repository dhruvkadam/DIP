import cv2

img=cv2.imread("C:/Users/Dhruv/Desktop/MT/mark.jpg")

print(type(img))
cv2.imshow('Original Image',img)

cv2.waitKey(0)

