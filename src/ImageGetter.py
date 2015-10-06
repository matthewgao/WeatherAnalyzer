#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2'
__author__ = 'Matthew (matthewgao@gmail.com)'

import urllib,re,os
import StringIO
from PIL import Image

class ImageGetter:
    #def __init__(self):
        
    def get_radar_img(self,url):
        data = urllib.urlopen(url).read()
        imgurl = re.findall('img id="img_path" src="(.*?)"',data)
        print imgurl[0]
        data = urllib.urlopen(imgurl[0]).read()
        img_buffer = StringIO.StringIO(data)
        return Image.open(img_buffer).convert('RGB')

    def convertTobBinaryFileStream(self,img,filetype):
        filename = "radar_image\\tmp."+filetype
        img.save(filename)
        return open(filename,'rb')
 
