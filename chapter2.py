import numpy as np
import cv2


img = cv2.imread('Resources/image.jpg')
kernel = np.ones((5,5),np.uint8)
# Gray Image
imgG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur Image
imgB = cv2.GaussianBlur(imgG, (9, 9), 0)

# Canny Image
imgC = cv2.Canny(imgG,150,200)

# Dialation
imgD = cv2.dilate(imgC,kernel, iterations=1)

#Erosion
imgE = cv2.erode(imgD,kernel, iterations=1)


cv2.imshow("Gray Image", imgG)
cv2.imshow("Blur Image", imgB)
cv2.imshow("Canny Image", imgC)
cv2.imshow("Dialation Image", imgD)
cv2.imshow("Eroded Image", imgE)

cv2.waitKey(0)