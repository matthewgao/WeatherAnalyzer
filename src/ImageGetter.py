#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2'
__author__ = 'Matthew (matthewgao@gmail.com)'

import urllib,re
import StringIO
from PIL import Image

class ImageGetter:
    #def __init__(self):
        

    def getRadarImg(self,url):
        data = urllib.urlopen(url).read()
        imgurl = re.findall('img id="img_path" src="(.*?)"',data)
        print imgurl[0]
        data = urllib.urlopen(imgurl[0]).read()
        img_buffer = StringIO.StringIO(data)
        return Image.open(img_buffer)


 
