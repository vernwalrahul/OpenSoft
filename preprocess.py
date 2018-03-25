import cv2
import numpy as np
import math
import submodule
import pages
 
img_original =  cv2.imread('images/image21.jpg');
####### 
gray_original = cv2.cvtColor(img_original,cv2.COLOR_BGR2GRAY)
img_copy = np.zeros((gray_original.shape[0], gray_original.shape[1]), dtype="uint8")
np.copyto(img_copy, gray_original)
img = pages.detection(img_copy)    
#######

#import image & remove noise
img = cv2.imread('images/image21.jpg');
img1 = cv2.imread('images/image21.jpg');
cv2.imshow("orig", img)

gray = submodule.denoise_then_gray(img)
cv2.imshow("gray", gray)
print("grayscale done")

edge = submodule.Threshold_and_Canny(gray)
cv2.imshow("edge",edge)
print("edge done")

line_list = submodule.get_lines_list(edge)
print("line_list = ",line_list)
print("line_list[0] = ",line_list[0])

image = submodule.copy_required_blocks(img1, line_list)
cv2.imshow("here ", image)
cv2.waitKey(0)








# image = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
# # cv2.imshow("orig", img)
# # cv2.imshow("final", image)
# # cv2.waitKey(0)

# #BGR2GRAY
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imwrite("gray_areas.jpg", gray)

# #Gradient and Thresholding
# imgw=image.shape[0]
# imgh=image.shape[1]
# threshold = (imgh+imgw)/2*0.005

# thresh = cv2.Canny(gray,100,200)
# kernel = np.ones((3,3), np.uint8)
# kernel1= np.ones((2,2),np.uint8)
# img_dilation = cv2.dilate(thresh, kernel, iterations=1)
# img_dilation = cv2.erode(img_dilation,kernel1,iterations=0)
# cv2.imshow("dilated",img_dilation)

# img_dilation = cv2.erode(img_dilation,kernel1,iterations=0)
# cv2.imshow('dilated', img_dilation)
# cv2.waitKey(0)

############ MAKE BOUNDING BOX #################

################################################

