#import PIL from Image
from PIL import Image
from pylab import *

class ImageAnalyzer:
    def __init__(self):
        self.region = (0,0,0,0)
        self.filename = 1

    def openImage(self,img_buffer):
        return Image.open(img_buffer)


    def cropImage(self, img):
        #img = Image.open(img_buffer)
        img = img.convert('RGB')
        if self.region == (0,0,0,0):
            print "Please set the region."
        img = img.crop(self.region)
        filename = "d:\\" + str(self.filename) + ".bmp"
        print filename
        img.save(filename)
        self.filename = self.filename + 1

        return img
        #imshow(img)
        #img.show()
        
    def setRegion(self, region):
        self.region = region

    def imgAver(self,img):
        

        r = img[:,:,0]
        g = img[:,:,1]
        b = img[:,:,2]
        (height,weight) = r.shape
        
        sumR = 0
        sumG = 0
        sumB = 0
        skipCount = 0
        for i in range(0,height):
            for j in range(0,weight):
                if r[i,j] == 218 and r[i,j] == g[i,j]:
                    skipCount = skipCount + 1
                    continue
                sumR = sumR + r[i,j]
                sumG = sumG + g[i,j]
                sumB = sumB + b[i,j]

        rAver = sumR/((height*weight)-skipCount)
        gAver = sumG/((height*weight)-skipCount)
        bAver = sumB/((height*weight)-skipCount)
        return (rAver,gAver,bAver)

    def analysisImage(self,img):
        im = array(img)

        (rAver,gAver,bAver) = self.imgAver(im)

        print "rAver:" +str(rAver)
        print "gAver:" +str(gAver)
        print "bAver:" +str(bAver) 

        if bAver < 10 and rAver >= 2:
            return "big"

        if rAver < 10 and bAver >= 2:
            return "clear"

        return "possible"



    
