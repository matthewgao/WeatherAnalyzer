from PIL import Image
import os
from pylab import *
from src.WeiboPoster import *
from src.ImageGetter import *

im = array(Image.open('radar_image\\115.bmp').convert('RGB'))
#imc = array(Image.open('radar_image\Shanghai_calbirate.bmp'))
print im.shape, im.dtype
weibo = WeiboPoster()
pil_im = Image.fromarray(uint8(im))
pil_im.save("test.jpg")
imgGet = ImageGetter()
weibo.postWeiboWithImage("test with a pic",imgGet.convertTobBinaryFileStream(pil_im,"jpg"))
r = im[:,:,0]
g = im[:,:,1]
b = im[:,:,2]
figure()
imshow(r)
show()
figure()
imshow(g)
show()
figure()
imshow(b)
show()

print r
print g
print b
(height,weight) = r.shape
#r[4,8] =11
sumAll = 0
for i in range(0,height):
    for j in range(0,weight):
        if (r[i,j] == 218 and r[i,j] == g[i,j]) \
            or ((r[i,j]==0 and g[i,j]==0 and b[i,j]==170)) \
            or ((r[i,j]==0 and g[i,j]==0 and b[i,j]==85)) \
            or ((r[i,j]==36 and g[i,j]==72 and b[i,j]==85))\
            or ((r[i,j]==36 and g[i,j]==109 and b[i,j]==85))\
            or ((r[i,j]==0 and g[i,j]==145 and b[i,j]==255))\
            or ((r[i,j]==36 and g[i,j]==109 and b[i,j]==170)):
            im[i,j,0]=im[i,j,1]=im[i,j,2]=0
            continue
        
print sumAll
print average
pil_im = Image.fromarray(uint8(im))
pil_im.save("test.bmp")

'''
imshow(im)
show()
figure()
imshow(imc)
show()
i=imc -im
imshow(abs(i))
show()
'''
'''
print i[:,:,0]
print i[:,:,1]
print i[:,:,2]

'''
#figure()
#hist(im.flatten(),128)
#show()

#img = Image.open('d:\\ab1.bmp')
#img.show()
#r,g,b = (Image)(img).split()
#print r
