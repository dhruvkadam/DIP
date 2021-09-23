import cv2
img = cv2.imread("C:/Users/Dhruv/Desktop/MT/mark.jpg",0)
print(type(img))
cv2.imshow('Original Image',img)
cv2.waitKey(0)
img=cv2.imread("C:/Users/Dhruv/Desktop/MT/mark.jpg",0)
cv2.show('Original Image', img)
img = cv2.imread("C:/Users/Dhruv/Desktop/MT/mark.jpg", -1)
cv2.imshow('Original image', img)
