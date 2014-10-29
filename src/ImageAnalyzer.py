#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2'
__author__ = 'Matthew (matthewgao@gmail.com)'

from PIL import Image
from pylab import *

class ImageAnalyzer:
    def __init__(self):
        self.region = (0,0,0,0)
        self.filename = 1

    def cropImage(self, img):

        img = img.convert('RGB')
        if self.region == (0,0,0,0):
            print "Please set the region."
        img = img.crop(self.region)
        filename = "d:\\" + str(self.filename) + ".bmp"
        print filename
        img.save(filename)
        self.filename = self.filename + 1
        return img
        
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
                if (r[i,j] == 218 and r[i,j] == g[i,j]) \
                   or ((r[i,j]==0 and g[i,j]==0 and b[i,j]==170)) \
                   or ((r[i,j]==0 and g[i,j]==0 and b[i,j]==85)) \
                   or ((r[i,j]==36 and g[i,j]==72 and b[i,j]==85))\
                   or ((r[i,j]==36 and g[i,j]==109 and b[i,j]==85))\
                   or ((r[i,j]==0 and g[i,j]==145 and b[i,j]==255))\
                   or ((r[i,j]==36 and g[i,j]==109 and b[i,j]==170)):
                    skipCount = skipCount + 1
                    continue
                sumR = sumR + r[i,j]
                sumG = sumG + g[i,j]
                sumB = sumB + b[i,j]
        if ((height*weight)-skipCount) == 0:
            return (0,0,0)
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

        if rAver ==0 and gAver ==0 and bAver ==0:
            return "Clear"
        
        if bAver < 10 and rAver >= 6:
            return "Raining"

        if rAver < 10 and bAver >= 2:
            return "Clear"

        return "Cloudy"



    
