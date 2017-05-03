import numpy as np
import cv2

stop_sign_cascade = cv2.CascadeClassifier('stopsign_classifier.xml')
img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

stop_sign = stop_sign_cascade.detectMultiScale(gray, 1.3, 5)
print stop_sign
for(x,y,w,h) in stop_sign:
    img = cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0), 2)
    

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
