'''
Created on 10 avr. 2014

@author: nicolas
'''

class Weather(object):
    '''
    classdocs
    '''
    __temperature  = 0
    __pressure = 0

    def __init__(self, temp=0, press=0):
        '''
        Constructor
        '''
        self.__temperature = temp
        self.__pressure = press


    def get_temperature(self):
        return self.__temperature


    def get_pressure(self):
        return self.__pressure


    def set_temperature(self, value):
        self.__temperature = value


    def set_pressure(self, value):
        self.__pressure = value


    def del_temperature(self):
        del self.__temperature


    def del_pressure(self):
        del self.__pressure



    