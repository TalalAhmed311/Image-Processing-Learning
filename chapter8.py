import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:

            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            print('Peri: ', peri)

            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))

            app = len(approx)

            x, y, w, h = cv2.boundingRect(approx)
            if app == 3:
                objType = 'Tri'
            else:
                objType = 'None'

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.putText(imgContour,objType,
            #             (x+(w//2)-10), (y+(h//2)-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

path = 'Resources/shape.png'
img = cv2.imread(path)
# print(img.shape)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

imgContour = img.copy()
getContours(imgCanny)

cv2.imshow("Shapes", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("ContourImage", imgContour)

cv2.waitKey(0)
