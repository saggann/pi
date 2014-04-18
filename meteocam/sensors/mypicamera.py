'''
Created on 10 avr. 2014

@author: nicolas
'''

import picamera
import io
import time

from PIL import Image

from   meteocam.camera  import picture
from   meteocam.sensors import pisystem

class MyPiCamera(object):
    '''
    classdocs
    '''


    # EXIF data
    __sys = None
    __lat=[0,"N"]
    __lon=[0,"W"]
    __alt=[0,0]
    
    # Image
    __image = None
    
    #piCamera
    __camera = None
    __w     = 800
    __h     = 600
    __rot   = 270
    __capture_delay = 2
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__sys = pisystem.PiSystem()
        
        # Generate picamera
        try:
            self.__camera = picamera.PiCamera()
        
            # Default EXIF Tags
            self.__camera.exif_tags['IFD0.Model'] = self.__sys.get_uid()
        
        except picamera.exc.PiCameraMMALError:
            raise IOError("Camera module not found")

    def get_capture_delay(self):
        return self.__capture_delay


    def set_capture_delay(self, value):
        self.__capture_delay = value


    def get_w(self):
        return self.__w


    def get_h(self):
        return self.__h


    def get_rot(self):
        return self.__rot


    def set_w(self, value):
        self.__w = value


    def set_h(self, value):
        self.__h = value


    def set_rot(self, value):
        self.__rot = value

    
    def shot(self, filename):
        
                
        try:
            
            # Set camera options for image capture
            self.__camera.resolution = (self.__w,self.__h)
            self.__camera.rotation = self.__rot
            
            # start stream
            stream = io.BytesIO()
            
            # Capture image
            self.__camera.start_preview()
            time.sleep(self.__capture_delay)
            self.__camera.capture(stream, format="jpeg")
            stream.seek(0)
            
            self.__image = picture.Picture(Image.open(stream), filename)
            stream.close()
            
           
        except OSError:
            print "Camera error"
        
        finally:
            self.__camera.close()
            return self
       
    
    
    def get_image(self):
        return self.__image
    
    
    def generateExif(self):
        
        self._exif = ""

        self._exif += " -x GPS.GPSLatitude="     + str(self._lat[0])
        self._exif += " -x GPS.GPSLatitudeRef="  + str(self._lat[1])
    
        self._exif += " -x GPS.GPSLongitude="    + str(self._lon[0])
        self._exif += " -x GPS.GPSLongitudeRef=" + str(self._lon[1])
    
        self._exif += " -x GPS.GPSAltitude="     + str(self._alt[0])
        self._exif += " -x GPS.GPSAltitudeRef="  + str(self._alt[1])

