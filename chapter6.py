import cv2
import numpy as np

img = cv2.imread('Resources/Card.jpg')

imgH = np.hstack((img,img))
imgV = np.vstack((img,img))


cv2.imshow('Image',img)
cv2.imshow('Image Horizontal',imgH)
cv2.imshow('Image Vertical',imgV)


cv2.waitKey(0)