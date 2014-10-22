from PIL import Image
import os
from pylab import *

im = array(Image.open('all.bmp').convert('L'))
imc = array(Image.open('Shanghai_calbirate.bmp'))
print im.shape, im.dtype

im2 = 255 - im 

im3 = (100.0/255) * im + 100 

im4 = 255.0 * (im/255.0)**2
pil_im = Image.fromarray(uint8(im4))
pil_im.save("test.bmp")
imshow(im4)
show()
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
figure()
imshow(im[:,:,0])
show()
figure()
imshow(im[:,:,1])
show()
figure()
imshow(im[:,:,2])
show()
'''
#figure()
#hist(im.flatten(),128)
#show()

#img = Image.open('d:\\ab1.bmp')
#img.show()
#r,g,b = (Image)(img).split()
#print r
