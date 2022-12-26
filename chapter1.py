import time

import pandas as pd
import numpy as np
import cv2
import os

# img=cv2.imread('Resources/image.jpg')

# import image
# cv2.imshow('Output',img)
# cv2.waitKey()

# For video
# video = cv2.VideoCapture('Resources/Jane woh kese log.mp4')


# For WebCam

# webCam = cv2.VideoCapture(0)
#
# # 3 width
# webCam.set(3,640)
#
# # 4 height
# webCam.set(4,480)
#
# # 10 Brightness
# webCam.set(10, 100)



import cv2
labels = ['hello']
n_img = 5


path ='F:\Computer vision\Sign_Language_Detection'
for label in labels:
    os.mkdir(os.path.join(path,label))
    webCam = cv2.VideoCapture(0)
    print(label)
    time.sleep(5)

    for n in range(n_img):
        success, img = webCam.read()
        img_name = os.path.join(path,label,label+'{}.jpg'.format(str(n)))
        cv2.imshow('img',img)
        time.sleep(2)
        cv2.imwrite(img_name, img)
        print('done'+' '+str(n))
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    webCam.release()



# webCam = cv2.VideoCapture(0)
# while True:
#     success, img=webCam.read()
#     cv2.imshow('Video',img)
#     if cv2.waitKey(1) & 0xFF == ord('e'):
#         break