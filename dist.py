import numpy as np
import cv2 as cv
dst = cv.imread("C:Users/Dhruv/Desktop/MT/valorant.jpg",0)
sobely = cv.Sobel(dst,-1,0,1,ksize=3)
cv.imwrite('C:Users/Dhruv/Desktop/MT/valorant.jpg',sobely)
sobely
arr = []
count = 0
for row in range(0,sobely.shape[0]):
    for col in range(0,sobely.shape[1]):
        if sobely[row][col] == 255:
            count += 1
            arr.append(row)
count1 = 0
count2 = 0
count3 = 0
for i in arr:
    if i == 73:
        count1 += 1
    if i == 117:
        count2 += 1
    if i == 162:
        count3 += 1
            
print(count1)
print(count2)
print(count3)
print('The longest horizontal line :-')
print(max(count1,count2,count3))
print(arr)