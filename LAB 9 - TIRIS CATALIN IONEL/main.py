import cv2

face_cascade = cv2.CascadeClassifier('D:\Inteligenta Artificiala\LAB-uri\LAB 9 - TIRIS CATALIN IONEL/text.xml')
img = cv2.imread(r'D:\Inteligenta Artificiala\LAB-uri\LAB 9 - TIRIS CATALIN IONEL/fata.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,00), 2)

    cv2.imshow('Imagine: ', img)
    cv2.waitKey()