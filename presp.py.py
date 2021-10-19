import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mplt

img = cv.imread("E:\python1\python\Test6.jpg")

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

resized = image_resize(img, height = 700)


imgcpy = cv.cvtColor(resized , cv.COLOR_BGR2RGB)

# ax = plt.subplot(imgcpy)
# cv2.imshow("" ,ax)
# print(ax)
cv.waitKey(0)  

# cv2.destroyAllWindows()
i = 1
pt1 = np.float32([[0,0],[700,0],[0,600],[600,700]])
pt2 = np.float32([[0,0],[800,0],[0,700],[700,800]])
# pt2 = np.float32([[0,0],[700,0],[0,600],[700,700]])
 
while i == 1:
  i = i + 1

  matrix = cv.getPerspectiveTransform(pt1,pt2)

  res = cv.warpPerspective(imgcpy, matrix , (900 , 800))

  cv.imshow("Image",res)

  cv.waitKey(0)
              
  cv.destroyAllWindows() 