import cv2 as cv
import numpy as np

image=cv.imread("E:\python1\python\Test1.jpg")
def image_resize(image, width = None, height = None, inter = cv.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    # if width is None and height is None:
    #     return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv.resize(image , dim , interpolation = inter)

    return resized

resized = image_resize(image, height = 700)

img = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)

ret , thresh1 = cv.threshold(img,150,220,cv.THRESH_BINARY)
ret , thresh2 = cv.threshold(img,150,220,cv.THRESH_BINARY_INV)

ret,thresh3 = cv.threshold(img,150,220,cv.THRESH_TRUNC)

ret,thresh4=cv.threshold(img,150,220,cv.THRESH_OTSU)
ret,thresh5=cv.threshold(img,150,220,cv.THRESH_TRIANGLE)

cv.imshow("Thresh1",thresh1)
cv.waitKey(0)
cv.imshow("Thresh2",thresh2)
cv.waitKey(0)
cv.imshow("Thresh3",thresh3)
cv.waitKey(0)
cv.imshow("Thresh4",thresh4)
cv.imshow("Thresh5",thresh5)


cv.waitKey(0)
cv.destroyAllWindows()