import numpy as np
import cv2 as cv
img=cv.imread("C:Users/Dhruv/Desktop/MicrosoftTeams-image.png",0)
soblex=cv.Sobel(img, -1,1,0,ksize=3)
cv.imwrite("C:Users/Dhruv/Desktop/MicrosoftTeams-image.png",soblex)
cv.imshow("sobelx",soblex)

cv.waitKey(0)
