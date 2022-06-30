import cv2
import numpy as np

img = cv2.imread("C:\\Users\\ADMIN\\Downloads\\eagle.jpg")
cv2.imshow("input-1",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray-2", gray)

gray = cv2.medianBlur(gray,3)
cv2.imshow("blur-3", gray)

edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow("edges-4",edges)

color = cv2.bilateralFilter(img,2,250,250)
cv2.imshow("bilateral-5",color)

cartoon = cv2.bitwise_and(color,color,mask=edges)
cv2.imshow("output-6",cartoon)


cv2.waitKey(0)
cv2.destroyAllWindows()