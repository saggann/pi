'''
Created on 10 avr. 2014

@author: nicolas
'''

class Location(object):
    '''
    classdocs
    '''
    # Location values
    __latitude = 0
    __longitude = 0
    __altitude = 0
    
    # Mesurement errors
    __lat_err = 0
    __lon_err = 0
    __alt_err = 0  


    def __init__(self):
        '''
        Constructor
        '''

    def get_latitude(self):
        return self.__latitude


    def get_longitude(self):
        return self.__longitude


    def get_altitude(self):
        return self.__altitude


    def get_lat_err(self):
        return self.__lat_err


    def get_lon_err(self):
        return self.__lon_err


    def get_alt_err(self):
        return self.__alt_err


    def set_latitude(self, value):
        self.__latitude = value


    def set_longitude(self, value):
        self.__longitude = value


    def set_altitude(self, value):
        self.__altitude = value


    def set_lat_err(self, value):
        self.__lat_err = value


    def set_lon_err(self, value):
        self.__lon_err = value


    def set_alt_err(self, value):
        self.__alt_err = value


    def del_latitude(self):
        del self.__latitude


    def del_longitude(self):
        del self.__longitude


    def del_altitude(self):
        del self.__altitude


    def del_lat_err(self):
        del self.__lat_err


    def del_lon_err(self):
        del self.__lon_err


    def del_alt_err(self):
        del self.__alt_err

    