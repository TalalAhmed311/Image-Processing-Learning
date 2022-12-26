import cv2
from pytesseract import pytesseract

Cascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_russian_plate_number.xml")
img = cv2.imread('Resources/plate1.jpg')


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
numberPlate=Cascade.detectMultiScale(imgGray,1.1,10)

for (x,y,w,h) in numberPlate:
    if w*h > 200:
        print(x,y)
        cv2.rectangle(img,(x,y),(x+w,y+h),(24,161,255),2)
        cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_PLAIN
                    ,1,(255,29,92),2)
        imgRoi = img[y:y + h, x:x + w]
        cv2.imshow("ROI", imgRoi)


cv2.imshow("Car", img)
# cv2.imshow("GrayImage", imgGray)
# imgRoi = img[y:y + h, x:x + w]
# cv2.imshow("ROI", imgRoi)

# path = r'C:\Users\Dell\anaconda3\Lib\site-packages\pytesseract'
# text = pytesseract.image_to_string(imgRoi)

cv2.waitKey(0)
