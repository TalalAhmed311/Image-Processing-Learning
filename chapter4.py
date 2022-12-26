import cv2
import numpy as np

img =  np.zeros((512,512,3),np.uint8)
print(img.shape)

# To give color
# for full image

# img[:]= 0,250,0

# img[200:300, 400:500] = 124,254,0

# Drawings on images

cv2.line(img,(0,0),(200,500),(125,200,123),2)
cv2.rectangle(img,(100,200), (300,400),(0,255,255),3)
cv2.circle(img,(350,400),20, (121,0,124),2)
cv2.putText(img,"Hello to OpenCV",(300,200),cv2.FONT_ITALIC,0,(0,150,0),1)

cv2.imshow("Image", img)
cv2.waitKey(0)
