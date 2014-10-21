#import PIL from Image
from PIL import Image


class ImageAnalyzer:
    #def __init__(self):

    def openImage(self, img_buffer):
        img = Image.open(img_buffer)
        img = img.convert('L')
        img = img.crop((235,185,330,274))
        img.save('d:\\ab1.jpg')
        img.show()
        
