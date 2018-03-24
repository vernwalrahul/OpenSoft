
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import cv2
import scipy
import math  



# image=cv2.imread("image21.jpg")
# final_block=[]


# In[2]:



def dist(x1,y1,x2,y2):  
    ans = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return int(ans)  


# In[3]:


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
        return int((y1 - y2b)/1.2)
    elif top:
        return int((y2 - y1b)/1.2)
    else:             # rectangles intersect
        return 0


# In[4]:


def can_merge(t1,t2):
    if rect_distance(t1,t2)<10:
        return 1
    return 0
    


# In[5]:



 
#import image
def block_detector(image,final_block):
    # nimage = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    #grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #gray = cv2.cvtColor(nimage,cv2.COLOR_BGR2GRAY)
    imgw=image.shape[0]
    imgh=image.shape[1]

    #binary
    # ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    thresh = cv2.Canny(gray,100,200)

    #dilation
    kernel = np.ones((2,8), np.uint8)
    kernel1= np.ones((2,8),np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=2)
    img_dilation = cv2.erode(img_dilation,kernel1,iterations=0)
    img_dilation = cv2.erode(img_dilation,kernel1,iterations=1)

    #find contours
    im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

    rect_ = []
    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)

        if w < imgw*0.02 or h < imgh*0.01  or w>imgw*0.6 or h>imgh*0.6: continue
        rect_.append((x,y,w,h)) 
        # Getting ROI1
        roi = image[y:y+h, x:x+w]

        # show ROI
        #cv2.imshow('segment no:'+str(i),roi)
        #cv2.rectangle(image,(x,y),( x + w, y + h ),(0,255,0),3)
        #cv2.waitKey(0)
    
    ims=image
    #cv2.imshow('marked_areas', ims)
    #qcv2.imwrite("marked_areas.jpg", ims)


            # cv2.imwrite('output/{}.jpg'.format(i), roi)

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
                if (j<=i or mark[i]==1 or mark[j]==1):
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
        lis=set(lis)
        lis=list(lis)
        rect1.append(list(lis))
        #print(len(lis))
    z=99
    finallist=[]
    for i in range(len(rect1[z])):
        x=rect1[z][i][0]
        y=rect1[z][i][1]
        w=rect1[z][i][2]
        h=rect1[z][i][3]
#         final_block=line_extract(rect1[z][i],final_block)
        finallist.append(list(line_extract(rect1[z][i],final_block,image)))
        # cv2.rectangle(image,(x,y),( x + w, y + h ),(255,0,0),3)
    #print(len(rect1[1]))
    #print(len(rect_))

    
    return final_block


# In[6]:





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
def line_extract(coord,final_block,image):
    startx = coord[0]
    endx = startx+coord[2]
    starty = coord[1]
    endy = starty+coord[3]
    img = image[starty:endy , startx:endx]
#     cv2.imwrite("block.jpg",img)
    gray_img=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    _,th1=cv2.threshold(gray_img , 127 , 255 , cv2.THRESH_BINARY)
    _,th2=cv2.threshold(gray_img , 0 , 255 , cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    blur1=cv2.GaussianBlur(gray_img , (5,5),0,0)
    _,ret=cv2.threshold(blur1 , 0 , 255 , cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    edge=cv2.Canny(ret,50,150,3)
    vHisto=mareHistogram(edge)
    st=False
    beg=0
    list1= []
    for i in range(vHisto.shape[0]):
        for j in range(vHisto.shape[1]):
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
    listofwords=[]
    for i in range(len(list1)):
        #print (list1[i])
#         final_block=main(list1[i][0],list1[i][1],img,starty,startx,final_block)
        listofwords.append(list(main(list1[i][0],list1[i][1],img,starty,startx,final_block,image)))
       
    
#cv2.namedWindow("Gray Image" , WINDOW_AUTOSIZE);
#     cv2.imshow("abc" , vHisto)
#     cv2.imshow("Gray Image",edge)
#     cv2.imshow("abc2",vHisto)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    return listofwords


# In[7]:


#import image
#image = cv2.imread('image20.jpg');
def main(ystart,yend,imge,starty,startx,final_block,image):
    #image=cv2.imread('a.png')
    # nimage = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    imagee = image[starty+ystart:starty+yend,startx:startx+imge.shape[1]]
#     cv2.rectangle(image,(startx,starty+ystart),( startx + imge.shape[1], starty + yend ),(0,0,255),3)
#     implt(image)
    #grayscale
#     cv2.imwrite("new.jpg",imagee)
    gray = cv2.cvtColor(imagee,cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(nimage,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray)
    # cv2.waitKey(0)
     
    #binary
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    # cv2.imshow('second', thresh)
    # cv2.waitKey(0)
     
    #dilation
    kernel = np.ones((2,8), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    #cv2.imshow('dilated', img_dilation)
    #cv2.waitKey(0)

    #find contours
    im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     
    #sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    list1=[]
#     print(len(sorted_ctrs))
    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)

        if w < 0.03*imagee.shape[1] or h < 0.02*imagee.shape[0]: 
            continue
     
        # Getting ROI
        roi = image[y:y+h, x:x+w]
     
        # show ROI
        #cv2.imshow('segment no:'+str(i),roi)
        list1.append((startx+x,starty+ystart+y,w,h))
        final_block.append((startx+x,starty+ystart+y,startx+x+w,starty+ystart+y+h))
        
        #image = imge[ystart:yend,0:imge.shape[0]-1]
#         cv2.rectangle(image,(startx+x,starty+ystart+y),( startx+x+w, starty+ystart+y+h ),(0,255,0),3)
        
        #cv2.waitKey(0)
     
            # cv2.imwrite('output/{}.jpg'.format(i), roi)

    #cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    #ims = cv2.resize(image, (480, 560))
    #cv2.imwrite("words00.jpg", ims)
    return list1


# In[8]:


def finalwords():
    for i in (final_block):
        startx = i[0]
        endx = startx+i[2]
        starty = i[1]
        endy = starty+ i[3]
#         print(startx,endx,starty,endy)
        img = image[starty:endy , startx:endx]
#         cv2.rectangle(image,(startx,starty),( endx, endy ),(0,0,255),3)
#         ims = cv2.resize(img, (480, 560))
        print(i)
    print (len(final_block))


# In[9]:




# In[10]:


# finalwords()

