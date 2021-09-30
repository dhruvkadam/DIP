import cv2 as cv
import numpy as np
img = cv.imread('C:/Users/Dhruv/Desktop/MT/gg.jpg')
rows,cols, channel = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
