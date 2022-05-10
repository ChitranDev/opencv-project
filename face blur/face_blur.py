import cv2
import numpy as np
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    success,img = cap.read()
    faces = faceCascade.detectMultiScale(img)
    for (x,y,w,h) in faces:
        # to make a face blurred
        ROI = img[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(ROI, (91,91),0)
        # insert ROI back into image
        img[y:y+h, x:x+w] = blur
    if faces ==():
        cv2.putText(img,'no faces found!',(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    cv2.imshow('Face Blur', img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
# turn off camera
cap.release()
cv2.destroyAllWindows()



