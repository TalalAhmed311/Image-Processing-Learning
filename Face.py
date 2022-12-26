import cv2

webCam = cv2.VideoCapture(0)
webCam.set(3,640)
webCam.set(4,480)
webCam.set(10, 100)

faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")


# while True:
#     success, img = cap.read()
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
#     for (x, y, w, h) in numberPlates:
#         area = w*h
#         if area >minArea:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
#             cv2.putText(img,"Number Plate",(x,y-5),
#                         cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
#             imgRoi = img[y:y+h,x:x+w]
#             cv2.imshow("ROI", imgRoi)
#
#     cv2.imshow("Result", img)


while True:
    success, img=webCam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(img, 1.1,20)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "Talal", (x, y-40), cv2.FONT_HERSHEY_PLAIN
                , 1, (255, 0, 255), 2)
#
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break