import urllib,re
import StringIO

class ImageGetter:
    #def __init__(self):
        

    def getRadarImg(self,url):
        data = urllib.urlopen(url).read()
        imgurl = re.findall('img id="img_path" src="(.*?)"',data)
        print imgurl[0]
        data = urllib.urlopen(imgurl[0]).read()
        img_buffer = StringIO.StringIO(data)
        return img_buffer


 
