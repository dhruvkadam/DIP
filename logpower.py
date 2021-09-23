import cv2
import numpy as np



image = cv2.imread('C:/Users/Dhruv/Desktop/bielsa.jpg')


c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))


#log_image = np.array(log_image, dtype = np.uint8)


cv2.imshow(image)
cv2.show()
cv2.imshow(log_image)
cv2.show()
