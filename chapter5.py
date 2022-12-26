import cv2
import numpy as np

img = cv2.imread('Resources/Card.jpg')

width,height=250,350

pt1=np.float32([[111,219],[287,188],[154,482],[352,440]])
pt2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pt1,pt2)
img2 = cv2.warpPerspective(img,matrix,(width,height))
print(img.shape)

cv2.imshow("Image",img)
cv2.imshow("Out",img2)
cv2.waitKey(0)