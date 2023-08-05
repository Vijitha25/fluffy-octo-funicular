import numpy as np
import cv2

def sump(height,width,img1,img2):
    matrix = np.empty([width,height])
    for y in range(0,height):
        for x in range(0,width):
            if img1[x,y] == img2[x,y]:
                matrix[x,y]=0
            else:
                matrix[x,y]=1
    psum=0
    for y in range(0,height):
        for x in range(0,width):
            psum=matrix[x,y]+psum
    return psum

def npcr(img1,img2):
    height = img1.shape[0]
    width = img2.shape[1]
    npcrv=((sump(height,width,img1,img2)/(height*width))*100)
    return npcrv

img1 = cv2.imread('madrill1.png',0)
img2 = cv2.imread('madrill2.png',0)
print('NPCR:',npcr(img1,img2))
