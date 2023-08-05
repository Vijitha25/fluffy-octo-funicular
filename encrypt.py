import numpy as np
from PIL import Image
from numpy import asarray
import galois
import random
import hashlib


imgg = Image.open("mandrill.png")
img=imgg.convert('L')
 # getting the number of channels
channel_count = len(img.getbands())
#print(channel_count)
img_arr = np.reshape(img, (img.height, img.width, channel_count))
 # splitting up channels
channels = [img_arr[:,:,x] for x in range(channel_count)]
 # setting up a shuffling order for rows
random_perm = np.random.permutation(img.height)
 # reordering the rows with respect to the permutation
 #shuffled_img_arr = np.dstack([x[random_perm, :] for x in channels]).astype(np.uint8)
shuffled_img_arr = np.dstack([x[random_perm, :] for x in channels]).astype(np.uint8)
 # creating the Image from the shuffled array
if(channel_count==1):
    shuf=np.squeeze(shuffled_img_arr,axis=2)
    shuffled_img=Image.fromarray((shuf))
else:
    shuffled_img=Image.fromarray((shuffled_img_arr))
 # saving the shuffled file
 #shuffled_img.save("spepper.jpg")
 #print(shuffled_img)
 #Matrix multiplication using galois field
GF256 = galois.GF(2**8)
A= GF256(asarray(shuffled_img))
B = GF256(asarray(img))
C = A*B
f=np.array(C)
#print(f)
#print(f.shape)
 #f=Image.fromarray(C).show()
 #f=Image.fromarray(C)
 #f.save("f_im.jpg")




n=1
res=[]
coun=img.width*img.height*channel_count
while(n<=coun):

    x= round(random.uniform(-2.00,0.47),8)
    y= round(random.uniform(-1.12,1.12),8)
     #x= random.uniform(-2.00,0.47)
     #y= random.uniform(-1.12,1.12)
    a=complex(x,y)
    def get_iter(c, thresh, max_steps) -> int:

        z=c
        i=1
        while i<max_steps and (z*z.conjugate()).real<thresh:
            z=z*z +c
            i+=1
        return i
     #print(a)
    re=get_iter(a,thresh =4, max_steps=25)
     #print(re)
    if(re == 25):
        b=round(abs(a),10)
        c=int(str(b-int(b))[-3:])
        hash=(hashlib.sha1(str(c).encode()))
        h=hash.hexdigest()
         #print(h[-2:])
        res.append(int(h[-2:],16))
    else:
        b=round(abs(a),10)
        c1=int(str(b-int(b))[-2:])
        hash1=(hashlib.sha1(str(c1).encode()))
        h1=hash1.hexdigest()
         #print(h1[-2:])
        res.append(int(h1[-2:],16))
    n+=1
 #print(res)
x=np.array(res)
if(channel_count==1):
    shape=(img.height,img.width)
else:
    shape=(img.height,img.width,channel_count)
v=x.reshape(shape)
#print(v)
#print("****")
xp=np.bitwise_xor(f,v)
#print(xp)
#vv=Image.fromarray((xp*255).astype(np.uint8)).show()
vv=Image.fromarray((xp*255).astype(np.uint8))
vv.save('madrill2.png')
