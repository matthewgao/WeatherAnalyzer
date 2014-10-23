from PIL import Image
import os
from pylab import *

im = array(Image.open('ab1.bmp').convert('RGB'))
imc = array(Image.open('Shanghai_calbirate.bmp'))
print im.shape, im.dtype

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
r[4,8] =11
sumAll = 0
for i in range(0,height):
    for j in range(0,weight):
        sumAll = sumAll + r[i,j]
average = sumAll/(height*weight)
print sumAll
print average
#pil_im = Image.fromarray(uint8(im4))
#pil_im.save("test.bmp")

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
