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
    img_get = ImageGetter()
    img_analyzer = ImageAnalyzer()
    
    while True:
        try:
            img_data = img_get.get_radar_img("http://www.nmc.cn/publish/radar/qingpu.html")

            img_analyzer.set_region((235,185,330,274))
            cropped_img = img_analyzer.crop_image(img_data)

            img_analyzer.set_region((37,32,46,37))
            cropped_img2 = img_analyzer.crop_image(cropped_img)

            result = img_analyzer.analysis_image(cropped_img2)
            print ("Check result: " + result)

            if status != result:
                string = "#AutoWeatherPoster# "
                string = string + "The weather at Jiangqiao is " + result
                string = string + ", Right Now"
                weibo = WeiboPoster()
                #weibo.post_weibo(string)
                weibo.post_weibo_with_image(string,img_get.convert_to_binary_file_stream(img_data,"jpg"))
                status = result
                
            time.sleep(600)
    
        except Exception , e:
            print (Exception,":",e)
            continue
   
