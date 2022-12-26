# Resizing and Cropping

import cv2

img = cv2.imread('Resources/image.jpg')
print(img.shape)

# Params : W, H
imgResize = cv2.resize(img,(600,400))
print(imgResize.shape)

imgCropped = img[0:400, 400:500]

# cv2.imshow("Image", img)
# cv2.imshow("ImageR", imgResize)
cv2.imshow("ImageCropped", imgCropped)


cv2.waitKey(0)