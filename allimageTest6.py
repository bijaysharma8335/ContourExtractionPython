import cv2
from matplotlib import pyplot as plt
import numpy as np

path = r'E:\python1\python\Test6.jpg' 

#reading image
img = cv2.imread(path,cv2.IMREAD_COLOR)
# width = 1000 
# height = 800
# dim = (width, height)
 
# resize image

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim  =  None
    (h , w) = image.shape[:2]

    # if width is None and height is None:
    #     return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image , dim , interpolation = inter)

    return resized

resized = image_resize(img , height = 750)
 
# print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)


# cv2.imshow('image',img)

# cv2.waitKey(0)

#greyscale image
# image = cv2.imread(path,0)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale Image",gray)

cv2.waitKey(0)

#Blurring image
blurred=cv2.medianBlur(gray,5) 
blurred=cv2.bilateralFilter(blurred,9,75,75) 
blurred = cv2.GaussianBlur(blurred, (5,5), 0)
cv2.imshow("Blurred Image",blurred)

#Canny image

Canny = cv2.Canny(gray, 100, 200, 3)
cv2.imshow("Canny Image",Canny)

# #countours 
# font = cv2.FONT_HERSHEY_COMPLEX

# # img = cv2.imread(path,cv2.IMREAD_COLOR)

# # img1 = cv2.imread(path ,cv2.IMREAD_GRAYSCALE)

contours, hierarchy = cv2.findContours(Canny  , 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
cv2.waitKey(0)

shapePoints=[]
cv2.drawContours(resized, contours, -1, (0, 0, 255), 2)
cv2.imshow('Contours', resized) 
# print(contours)


    # approx contour----------------
for cnt in contours:
    approxPoints=[]
    epsilon = 0.1 * cv2.arcLength(cnt, True)

    approx = cv2.approxPolyDP(cnt, epsilon, True)
    print(approx)

    cv2.drawContours(resized, [approx], -1, (0, 255, 0), 2)

    for points in approx:      
        approxPoints.append((points[0][0],points[0][1]))       
        shapePoints.append(approxPoints)
  # approx contour ----------------------------------

    # Draw all contours
    # -1 signifies drawing all contours

    
cv2.imshow("Approx Contours",resized)

# base = cv2.HoughLinesP(resized, 1, np.pi/180, 80 , minLineLength = 1, maxLineGap = 3)    
# # # base = cv2.HoughLinesP(edged, 1, np.pi / 180 , 50 , 1 , 5)
# pixel_array = []
# pixel_length = 0
# if base is not None:
#    for line in base:
#     x1, y1, x2, y2 = line[0]
       
#    cv2.line(resized, (x1 , y1), (x2 , y2), (0 , 0 , 255) , 2)
       
#        pixel_length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#        pixel_array.append(pixel_length)  
#     #    cv2.putText(resized,)                                            
       
#        print("Line points :", line)
      

#     #    cv2.putText(line,"",(x, y), font, 0.5, (0, 255, 0))
#        print("Length of line :{}".format(pixel_length))
#        print("-------------------------------------")
#        cv2.waitKey(0)


# # n = approx.ravel()  
# # font = cv2.FONT_HERSHEY_COMPLEX   
# # for j in n :
# #         if(i % 2 == 0):
# #             x = n[i]
# #             y = n[i + 1]
  
# #             # String containing the co-ordinates.
# #             string = str(x)  + str(y) 
  
# #             if(i == 0):
# #                 # text on topmost co-ordinate.
# #                 cv2.putText(resized," ", (x, y), font, 0.5, (255,0,0)) 
# #             else:
            
# #                 # text on remaining co-ordinates.
# #                 cv2.putText(resized, string, (x, y), font, 0.5, (0, 255, 0)) 

# #             # print(x,y) 


# #             i = i + 1
# #    cv2.imshow(" img " , resized) 


cv2.waitKey(0)

cv2.destroyAllWindows()

