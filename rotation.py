<<<<<<< HEAD
import cv2 as cv
img = cv.imread('C:/Users/Dhruv/Desktop/MT/gg.jpg',0)
rows,cols = img.shape

M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
















dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
=======
import cv2 as cv
img = cv.imread('C:/Users/Dhruv/Desktop/MT/gg.jpg',0)
rows,cols = img.shape

M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
















dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
>>>>>>> 801f948b6fa33b50240548b038e1863411ac6685
