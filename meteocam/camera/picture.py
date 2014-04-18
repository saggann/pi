'''
Created on 11 avr. 2014

@author: nicolas
'''


from StringIO import StringIO

from PIL import ImageFont
from PIL import ImageDraw 

class Picture(object):
    '''
    classdocs
    '''

    __filename   = ""
    __img64  = ""
    __image = None

    def __init__(self, image, filename):
        '''
        Constructor
        '''
        
        # Set the PIL Image
        self.__image = image

        # Uptate filename
        self.__filename  = '/tmp/image.jpg'

        # Update base64
        self.update_base64()
            


    def update_base64(self):
        # generate base64 encoded string of the PIL Image
        buff  = StringIO()
        self.__image.save(buff, "JPEG")
        self.__img64 = buff.getvalue().encode("base64")
        buff.close()
        
     
        
    def date_image(self, time):
        draw = ImageDraw.Draw(self.__image)
        font = ImageFont.truetype("/opt/build/pi/fonts/DejaVuSans.ttf", 16)
        text = "Meteocam - " + time
        draw.text((0, 0), text ,(255,0,0),font=font)
        self.update_base64()
        self.__image.save(self.__filename)
        


    def get_img64(self):
        return self.__img64
    
    
    
    def get_filename(self):
        return self.__filename
    
       
    
    