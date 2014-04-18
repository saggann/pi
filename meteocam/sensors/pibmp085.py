'''
Created on 10 avr. 2014

@author: nicolas
'''

import  Adafruit_BMP085
            
from    meteocam.weather      import weather

class PiBMP085(object):
    '''
    classdocs
    '''

    __weather = None
    __bmp = None

    def __init__(self, address=0x77, mode=2 ):
        self.__bmp = Adafruit_BMP085.BMP085(address, mode)
     
    
    def probe(self):
        try:
            t = self.__bmp.readTemperature() + 273.15
            p = self.__bmp.readPressure()/100.0
            self.__weather = weather.Weather(t, p )
            return True
        except AttributeError:
            print "can't read sensor"
            return False
    
    def get_weather(self):
        return self.__weather
    
        
    def get_pressure(self):
        return self.__weather.getPressure()
    
    
    def get_temperature(self):
        return self.__weather.getTemperature()