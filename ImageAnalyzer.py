#import PIL from Image
from PIL import Image


class ImageAnalyzer:
    #def __init__(self):

    def openImage(self, img_buffer):
        img = Image.open(img_buffer)
        img = img.convert('L')
        img.save('d:\\ab.jpg')
        img.show()
        
