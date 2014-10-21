from ImageGetter import *
from ImageAnalyzer import *
from WeiboPoster import *

if __name__ == "__main__":
    
    imgGet = ImageGetter()
    imgAnalyzer = ImageAnalyzer()
    weibo = WeiboPoster()
    #weibo.postWeibo("Hello World Again")
    imgData = imgGet.getRadarImg("http://www.nmc.gov.cn/publish/radar/qingpu.htm")
    #print imgData
    imgAnalyzer.openImage(imgData)

    
