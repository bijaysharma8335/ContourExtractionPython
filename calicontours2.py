import cv2
import numpy as np
import os
import glob
 
# Define the dimensions 
checkb = (800 , 800)
 
# stop the iteration when specified
# accuracy, epsilon, is reached or
# specified number of iterations are completed.
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
tpoints = []

twpoints = []
 
 
# 3D points real world coordinates
objectp3d = np.zeros((1, checkb[0] * checkb[1], 3), np.float32)
objectp3d[0, :, :2] = np.mgrid[0:checkb[0], 0:checkb[1]].T.reshape(-1, 2)
prev_img_shape = None
 
 
# Extracting path of individual image stored
# in a given directory. Since no path is
# specified, it will take current directory
# jpg files alone

images = glob.glob('E:\python1\python\Test6.jpg')
 
for filename in images:
    image = cv2.imread(filename)
    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    # Find  corners
    # If desired number of corners are
    # found in the image then ret = true
    ret, corners = cv2.findChessboardCorners(grayColor, checkb, cv2.CALIB_CB_ADAPTIVE_THRESH 
    + cv2.CALIB_CB_FAST_CHECK +cv2.CALIB_CB_NORMALIZE_IMAGE)
 
    # If desired number of corners can be detected then,
    # refine the pixel coordinates and display
    # them on the images 
    if ret == True:
        tpoints.append(objectp3d)
 
        # Refining pixel coordinates
        # for given 2d points.
        corners2 = cv2.cornerSubPix(grayColor, corners, (11, 11), (-1, -1), criteria)
 
        twpoints.append(corners2)
 
        # Draw and display the corners
        image = cv2.drawChessboardCorners(image , checkb , corners2, ret)
 
#resize the image  
scale = 25
width = int(image.shape[1] * scale / 100)
height = int(image.shape[0] * scale / 100)
dim=(width,height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
  
cv2.imshow("Calibrated  Image",resized)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

#Blurring of image
blurred = cv2.medianBlur(gray,5) 
blurred = cv2.bilateralFilter(blurred,9,75,75) 
blurred = cv2.GaussianBlur(blurred, (5,5), 0)
# cv2.imshow("Blurred Image",blurred)

# Find Canny edges
imageCanny = cv2.Canny(blurred, 100, 200, 3)
# cv2.imshow("Canny Image",imageCanny)

edged = cv2.Canny(gray, 50 , 200 )
contours, hierarchy = cv2.findContours(imageCanny, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
cv2.waitKey(0)

#Draw  contours on image
shapePoints=[]
     
for cnt in contours:
        approxPoints=[]
        epsilon = 0.1*cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        cv2.drawContours(resized, [approx], -1, (0, 255, 0), 3)

        # for points in approx:      
        #    approxPoints.append((points[0][0],points[0][1])) 

        # shapePoints.append(approxPoints)
  
    # Draw all contours
    # -1 signifies drawing all contours
cv2.drawContours(resized, contours, -1, (0, 0, 255), 7)

cv2.imshow("Contours " , resized)

cv2.waitKey(0)
 
cv2.destroyAllWindows()
  
# h, w = image.shape[:2] 
# Perform camera calibration by
# passing the value of above found out 3D points (threedpoints)
# and its corresponding pixel coordinates of the
# detected corners (twodpoints)
# ret, matrix, distortion, r_vecs, t_vecs = cv2.calibrateCamera( tpoints, twpoints, grayColor.shape[::-1] , 6 , 5)
 
# # Displaying required output

# print(matrix)