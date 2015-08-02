#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__version__ = '0.3'
__author__ = 'Matthew (matthewgao@gmail.com)'

from src.ImageGetter import *
from src.ImageAnalyzer import *
from src.WeiboPoster import *
import time

if __name__ == "__main__":

    status = "Clear"
    imgGet = ImageGetter()
    imgAnalyzer = ImageAnalyzer()
    
    while True:
        try:
            imgData = imgGet.getRadarImg("http://www.nmc.cn/publish/radar/qingpu.html")

            imgAnalyzer.setRegion((235,185,330,274))
            croppedImg = imgAnalyzer.cropImage(imgData)

            imgAnalyzer.setRegion((37,32,46,37))
            croppedImg2 = imgAnalyzer.cropImage(croppedImg)

            result = imgAnalyzer.analysisImage(croppedImg2)
            print ("Check result: " + result)

            if status != result:
                string = "#AutoWeatherPoster# "
                string = string + "The weather at Jiangqiao is " + result
                string = string + ", Right Now"
                weibo = WeiboPoster()
                #weibo.postWeibo(string)
                weibo.postWeiboWithImage(string,imgGet.convertTobBinaryFileStream(imgData,"jpg"))
                status = result
                
            time.sleep(600)
    
        except Exception , e:
            print (Exception,":",e)
            continue
   
