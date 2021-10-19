import cv2
import numpy as np 

image = cv2.imread('E:\python1\python\Test6.jpg')

cv2.waitKey(0)

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image , dim , interpolation = inter)

    # return the resized image
    return resized

#resized original image
resized = image_resize(image, height = 800)
  
# Grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# blurred = cv2.medianBlur(gray,5) 
# blurred = cv2.bilateralFilter(blurred,9,75,75) 
# blurred = cv2.GaussianBlur(blurred, (5,5), 0)
# cv2.imshow("Blurred Image",blurred)
  
# Find Canny edges
edged = cv2.Canny(gray, 50 , 200 )

cv2.waitKey(0) 
  
# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image

# contours,hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

contours , hierarchy = cv2.findContours(edged ,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
  
# cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)
  
  
# Draw all contours
# -1 signifies drawing all contours
# contour = max(contours,key = cv2.contourArea)
# print("hhh",contour)
cv2.drawContours(resized, contours, -1, (0 , 0 , 255), 2)
# contour = max(contours,key = cv2.contourArea)
# cv2.imshow("Largest Contour",contour)
cv2.waitKey(0)

font = cv2.FONT_HERSHEY_COMPLEX

# print(contours)

for cnt in contours :
    
    pixel_array = []
    pixel_length = 0
    epsilon = 0.009 * cv2.arcLength(cnt,True) 
    approx = cv2.approxPolyDP(cnt, epsilon , True)
    print("--------")
    print(approx)
    print("-----------")
    
    n = approx.ravel() 
    i = 0
    # print("n",n)
    # for i in n:
    #     x1=n[i]
    #     y1=n[i+1]

    #     x2=n[i+2]
    #     y2=n[i+3]

    for j in n :
    #   if i==0:
    #   print("J",j)
      x1 = n[0]
      y1 = n[1]
      x2 = n[2]
      y2 = n[3]
         
      pixel_length = np.sqrt((x2- x1) **2 + (y2- y1)**2)
    #   print(pixel_length)
      pixel_array.append(pixel_length)
      new_length = int(pixel_length)
      x=int((x1 + x2) / 2)
      y=int((y1 + y2) / 2)
      cv2.putText(resized,"{}".format(new_length) + "px", (x , y), cv2.FONT_HERSHEY_COMPLEX , 
       0.53, (0,0,0), 1)
    # print(new_length)
       
    # print("x1 y1", x1 , y1)
    # print("x2,y2",x2 , y2)
    
    #new x1,y1 x2,y2
    x1 = x2
    y1 = y2
    # print("x1,y1",x1,y1)
    i = i + 1
    # x1 = x2
    # y1 = y2 
    
      
    x2 = n[i+3]
    y2 = n[i+4]
    # print("x2,y2",x2,y2)
    if i == j-1:
       x2 = n[0]
       y2 = n[1]
    x = int((x1 + x2) / 2)
    y = int((y1 + y2) / 2)   
    pixel_length = np.sqrt((x2- x1) **2 + (y2- y1)**2)
    #   print(pixel_length)
    pixel_array.append(pixel_length)
    new_length = int(pixel_length)
    cv2.putText(resized,"{}".format(new_length) + "px", (x , y), cv2.FONT_HERSHEY_COMPLEX , 
       0.53, (0,0,0), 1)
cv2.imshow('Contours' , resized)

cv2.waitKey(0)
cv2.destroyAllWindows()   