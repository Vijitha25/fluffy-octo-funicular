import cv2
def uaci(img1,img2):
    height,width=img1.shape
    value=0
    for y in range(height):
        for x in range(width):
            value+=(abs(int(img1[x,y])-int(img2[x,y])))
    value=value*100/(width*height*255)
    return value
enimg1 = cv2.imread('madrill1.png',0)
enimg2 = cv2.imread('madrill2.png',0)
print('UACI:',uaci(enimg1,enimg2))
