import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread(r'D:\Inteligenta Artificiala\LAB-uri\LAB 6 - TIRIS CATALIN IONEL\numar_inmatriculare.jpg')
img =cv2.resize(img,(800,600))
cv2.imshow('IMAGINE REDIMENSIONATA' ,img)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('IMAGINE CU FILTRU GRI', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()