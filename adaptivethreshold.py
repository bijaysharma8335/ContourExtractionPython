import cv2 as cv
# import numpy as np

image=cv.imread("E:\python1\python\sampleOne.jpg")

img = cv.cvtColor(image , cv.COLOR_BGR2GRAY)

thresh1  = cv.adaptiveThreshold(img , 255 , cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,  199 , 5)

cv.imshow("Adaptive Threshold" , thresh1)

cv.waitKey(0)

cv.destroyAllWindows()

