
"""import cv2
import numpy as np


image = cv2.imread('image20.jpg',0)


retval, img = cv2.threshold(image,170,255,cv2.THRESH_BINARY_INV)


painty = np.zeros(img.shape,np.uint8)
cv2.Zero(cv2.fromarray(painty))
h = [0]*image.shape[0]
for y in range(image.shape[0]):
	for x in range(image.shape[1]):
		s = cv2.Get2D(cv2.cv.fromarray(img),y,x)
		if s[0] == 0:
			h[y] += 1
for y in range(image.shape(0)):
	for x in range(h[y]):
		cv2.Set2D(cv2.fromarray(painty),y,x,(255,255,255,0))
cv2.imshow('painty',painty)
cv2.waitKey(0)"""
import scipy
import numpy as np
import cv2
import matplotlib.pyplot as plt
def mareHistogram(img):
	#//col or row histogram?=
    sz=img.shape[0]
    mhist = np.zeros([1, sz], dtype="uint8")
    maxi=-1
    inn=-1
    for i in range(sz):
        data=img[i,:]
        v=cv2.countNonZero(data)
        mhist[0,i]=v
        if(v>maxi):
            maxi=v
            inn=i
    
        #data=np.array([1,sz[i]])
        
	histo=np.zeros((sz , maxi),dtype="uint8")
	#plt.imshow(histo,aspect="auto")
	#plt.show()
	for i in range(sz):
		for j in range(mhist[0,i]):
			histo[i,j]=(255)
    return histo






img=cv2.imread('images/image20.jpg')
cv2.imshow("Display_Window" , img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
gray_img=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
_,th1=cv2.threshold(gray_img , 127 , 255 , cv2.THRESH_BINARY)
_,th2=cv2.threshold(gray_img , 0 , 255 , cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur1=cv2.GaussianBlur(gray_img , (5,5),0,0)
_,ret=cv2.threshold(blur1 , 0 , 255 , cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cdst = np.array(ret.shape[0], ret.shape[1],cv2.CV_8UC3) #problem
#for k in range(ret.shape[0]):
 #   for l in range(ret.shape[1]):
  #      cdst[k,l,0]=255;
   #     cdst[k,l,1]=255;
    #    cdst[k,l,2]=255;

edge=cv2.Canny(ret,50,150,3)
vHisto=mareHistogram(edge)
st=False
beg=0
count=0
list1= []
for i in range(vHisto.shape[0]):
    for j in range(vHisto.shape[1]):
        count+=1
        pixel=vHisto[i,j]
        if(pixel==0):
            if(st==False):
                if(j>15):
                    st=True
                    beg=i
                    tup1 = (beg,)
                else:
                    break
            else:
                if(j<15):
                    end=i
                    if((end - beg)>10):
                    	tup2 = (end,)
                    	tup3 = tup1 + tup2
                    	list1.append(tup3)
                    st=False
                    break
for i in range(len(list1)):
	print (list1[i])
    
#cv2.namedWindow("Gray Image" , WINDOW_AUTOSIZE);
cv2.imshow("abc" , vHisto)
cv2.imshow("Gray Image",edge)
cv2.imshow("abc2",vHisto)
cv2.waitKey(0)
cv2.destroyAllWindows()