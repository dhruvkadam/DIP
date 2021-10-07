<<<<<<< HEAD
import cv2 as cv
img = cv.imread('C:/Users/Dhruv/Desktop/MT/gg.jpg')
img.shape
height, width, channel = img.shape
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', res)
cv.imwrite('C:/Users/Dhruv/Desktop/MT/gg.jpg',res)
cv.waitKey(0) 
cv.destroyAllWindows()
=======
import cv2 as cv
img = cv.imread('C:/Users/Dhruv/Desktop/MT/gg.jpg')
img.shape
height, width, channel = img.shape
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', res)
cv.imwrite('C:/Users/Dhruv/Desktop/MT/gg.jpg',res)
cv.waitKey(0) 
cv.destroyAllWindows()
>>>>>>> 801f948b6fa33b50240548b038e1863411ac6685
