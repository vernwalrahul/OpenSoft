import cv2
import numpy as np
import math

##SUBMODULES##
def dist(x1,y1,x2,y2):  
    ans = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return int(ans) 

def rect_distance(t1,t2):
    x1=t1[0]
    y1=t1[1]
    x1b=t1[2]+t1[0]
    y1b=t1[3]+t1[1]
    x2=t2[0]
    y2=t2[1]
    x2b=t2[2]+t2[0]
    y2b=t2[3]+t2[1]
    left = x2b < x1
    right = x1b < x2
    bottom = y2b < y1
    top = y1b < y2
    if top and left:
        return dist(x1, y1b, x2b, y2)
    elif left and bottom:
        return dist(x1, y1, x2b, y2b)
    elif bottom and right:
        return dist(x1b, y1, x2, y2b)
    elif right and top:
        return dist(x1b, y1b, x2, y2)
    elif left:
        return x1 - x2b
    elif right:
        return x2 - x1b
    elif bottom:
        return int((y1 - y2b)/1.3)
    elif top:
        return int((y2 - y1b)/1.3)
    else:             # rectangles intersect
        return 0.

def can_merge(t1,t2):
    if rect_distance(t1,t2)<15:
        return 1
    return 0

def find_if_close(cnt1,cnt2):
    row1,row2 = cnt1.shape[0],cnt2.shape[0]
    for i in range(row1):
        for j in range(row2):
            dist = np.linalg.norm(cnt1[i]-cnt2[j])
            if abs(dist) < 15 :
                return True
            elif i==row1-1 and j==row2-1:
                return False    
##END OF SUBMODULES##

#import image & remove noise
img = cv2.imread('images/image22.jpg');
image = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
# cv2.imshow("orig", img)
# cv2.imshow("final", image)
# cv2.waitKey(0)

#BGR2GRAY
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_areas.jpg", gray)

#Gradient and Thresholding
imgw=image.shape[0]
imgh=image.shape[1]
threshold = (imgh+imgw)/2*0.005

thresh = cv2.Canny(gray,100,200)
kernel = np.ones((2,8), np.uint8)
kernel1= np.ones((2,2),np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=2)
img_dilation = cv2.erode(img_dilation,kernel1,iterations=1)
cv2.imshow("dilated",img_dilation)

img_dilation = cv2.erode(img_dilation,kernel1,iterations=1)
cv2.imshow('dilated', img_dilation)

#Find Contours
im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

#Draw Bounding Boxes
rect_ = []
for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    
    if w < imgw*0.01 or h < imgh*0.01  or w>imgw*0.6 or h>imgh*0.6: continue
    rect_.append((x,y,w,h)) 
    # Getting ROI
    roi = image[y:y+h, x:x+w]
 
    # show ROI
    #cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(image,(x,y),( x + w, y + h ),(0,255,0),3)



#Merge Bounding boxes and contours
ims=image
#cv2.imshow('marked_areas', ims)
cv2.imwrite("marked_areas.jpg", ims)

rect1=[]
rec=[]
for i in range(len(rect_)):
    var=0
    for j in range(len(rect_)):
        if (j<=i ):
            continue
        if can_merge(rect_[i],rect_[j])==1:
            var=1
            x=min(rect_[i][0],rect_[j][0])
            y=min(rect_[i][1],rect_[j][1])
            a=max(rect_[i][2]+rect_[i][0],rect_[j][2]+rect_[j][0])
            b=max(rect_[i][3]+rect_[i][1],rect_[j][3]+rect_[j][1])
            rec.append((x,y,a-x,b-y))
    if var==0:
        rec.append(rect_[i])
rect1.append(list(rec))
for k in range(100):
    if k==0:
        continue
    lis=[]
    mark=np.zeros(2000)
    for i in range(len(rect1[k-1])):
        var=0
        for j in range(len(rect1[k-1])):
            if (j<=i or mark[i]==1):
                continue
            if can_merge(rect1[k-1][i],rect1[k-1][j])==1:
                var=1
                mark[j]=1
                x=min(rect1[k-1][i][0],rect1[k-1][j][0])
                y=min(rect1[k-1][i][1],rect1[k-1][j][1])
                a=max(rect1[k-1][i][2]+rect1[k-1][i][0],rect1[k-1][j][2]+rect1[k-1][j][0])
                b=max(rect1[k-1][i][3]+rect1[k-1][i][1],rect1[k-1][j][3]+rect1[k-1][j][1])
                lis.append((x,y,a-x,b-y))
        if (var==0 and mark[i]==0):
            lis.append(rect1[k-1][i])
    rect1.append(list(lis))
    print(len(lis))
z=99
for i in range(len(rect1[z])):
    x=rect1[z][i][0]
    y=rect1[z][i][1]
    w=rect1[z][i][2]
    h=rect1[z][i][3]
    cv2.rectangle(image,(x,y),( x + w, y + h ),(255,0,0),3)
print(len(rect1[1]))
print(len(rect_))
ims = cv2.resize(image, (480, 560))
cv2.imshow('marked_areas', ims)
cv2.waitKey(0)