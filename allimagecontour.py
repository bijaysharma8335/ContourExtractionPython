import cv2
import numpy as np 

image = cv2.imread('E:\python1\python\Test.jpg')

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

blurred=cv2.medianBlur(gray,5) 
blurred=cv2.bilateralFilter(blurred,9,75,75) 
blurred = cv2.GaussianBlur(blurred, (5,5), 0)
# cv2.imshow("Blurred Image",blurred)
  
# Find Canny edges
edged = cv2.Canny(blurred, 50 , 200 )

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
cv2.drawContours(resized, contours, -1, (0 , 0 , 255), 2)

font = cv2.FONT_HERSHEY_COMPLEX

# print(contours)

for cnt in contours :
    
    epsilon = 0.009 * cv2.arcLength(cnt,True) 
    approx = cv2.approxPolyDP(cnt, epsilon , True)
    print("--------")
    print(approx)
    print("-----------")
    # peri = cv2.arcLength(cnt , True)
    # print(peri)
    # print(approx)
  
    # draws boundary of contours.
    # cv2.drawContours(resized, [approx], 0, (0, 0, 255), 1) 
  
    # Used to flatted the array containing
    # the co-ordinates of the vertices.
    # n = approx.ravel() 
    # i = 0
  
    # for j in n :
    #    if(i % 2 == 0):
    #     x = n[i]
    #     y = n[i + 1]
  
    # #         # String containing the co-ordinates.
    #    string = str(x)  + str(y) 
  
    #    if(i == 0):
    # #             # text on topmost co-ordinate.
    #         cv2.putText(resized," ", (x, y), font, 0.5, (255,0,0)) 
    #    else:
            
    # #             # text on remaining co-ordinates.
    #           cv2.putText(resized, string, (x, y), font, 0.5, (0, 255, 0)) 

    # #         # print(x,y) 


    #    i = i + 1

            # def arc_length(x, y):
            #     npts = len(x)
            #     arc = np.sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2)
            #     for k in range(1, npts):
            #         arc = arc + np.sqrt((x[k] - x[k-1])**2 + (y[k] - y[k-1])**2)

            #     return arc

    # print("Number of Contours edges = " + len(x))

# print(cv2.arcLength(cnt[1] , True))         
base = cv2.HoughLinesP(edged, 1, np.pi/180, 80 , minLineLength = 1, maxLineGap = 2)    
# base = cv2.HoughLinesP(edged, 1, np.pi / 180 , 50 , 1 , 5)

pixel_array = []
pixel_length = 0
if base is not None:
   for line in base:
       x1, y1, x2, y2 = line[0]
       
       cv2.line(resized , (x1 , y1), (x2 , y2), (0 , 0 , 255) , 2)
       
       pixel_length = np.sqrt((x2 - x1) **2 + (y2 - y1) **2)

       pixel_array.append(pixel_length)
       new_length = int(pixel_length)
       print("Line points :", line)

       print("Length of line :{}".format(new_length))
    #    cv2.line(resized,(x1,y1),(x2,y2),(0,0,255),3)
    #    cv2.line(resized,(x2,y2),(x1,y1),(0,255,0),2)
    #    cv2.line(resized,x1,y1,(0,0,255),1)
       cv2.putText(resized,"Length :{}".format(new_length) + "px", (x1+15,y1+15), cv2.FONT_HERSHEY_COMPLEX , 
       0.5, (0,0,0), 1)
       cv2.putText(resized," ",(x1+20,y1+20), cv2.FONT_HERSHEY_COMPLEX ,0.5, (0,0,0), 1)

       print("-------------------------------------")
       
    
#    cv2.imshow(" img " , resized) 

# cv2.imwrite("hough_img.png",resized)

   cv2.waitKey(0)
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# print(thresh)

# Find contours, obtain bounding rect, and draw width
# cnts = cv2.findContours(thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]
# # print(cnts)


cv2.imshow('Contours' , resized)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# for c in cnts:
#     x  , y , w , h  = cv2.boundingRect(c)
#     cv2.putText(resized,"w = {} , h = {} ".format(w,h), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX , 0.9, (36,255,12), 2)
#     # cv2.putText(resized,"x = {} , y = {}, ".format(x,y), (x+3,y+10), cv2.FONT_HERSHEY_SIMPLEX , 0.9, (0,255,12), 1)
#     # cv2.line(resized,(w,h) , (h,w) , (0,255,0) , 2)
#     cv2.rectangle(resized, (x, y), (x + w, y + h), (36,255,12), 2)

#     if w > 8:

#       print(w,h) 
    # peri = cv2.arcLength(c,True)
    # print("peri is",peri)

# cv2.imshow(" img " , resized) 
# print("Average Pixel Length: {:.0f} pixel".format(np.average(pixel_array)))
# print("Total Lines:",base)
# length of countours
