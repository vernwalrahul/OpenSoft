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

def denoise_then_gray(img):
    image = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray

def Threshold_and_Canny(gray_img):
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

    return edge

def get_lines_list(edge):
    vHisto=mareHistogram(edge)
    cv2.imshow("histogram",vHisto)
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

    return list1    

def is_valid(i, line_list):
    for line in line_list[0:1]:
        if(i>=line[0] and i<=line[1]):
            return 1
    return 0
            
def copy_required_blocks(img, line_list):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray_here = ",gray)
    for i in range(0,gray.shape[0]):
        if(is_valid(i, line_list)):
            continue
        else:
            for j in range(0, gray.shape[1]):
                image[i][j] = 0
                
    return image             

