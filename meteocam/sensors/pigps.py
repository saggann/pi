'''
Created on 10 avr. 2014

@author: nicolas
'''

from meteocam.location import  location

import gps
import time

class PiGPS(object):
    '''
    classdocs
    '''
    
    # GPS Session
    __session = None
    
    # GPS sensor timeout in seconds
    __gps_timeout = 10
    __fix_timeout = 20
    
    # Location
    __loc = None
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__loc = location.Location()        
        self.__session = gps.gps("localhost", "2947")
        self.__session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


    def get_gps_timeout(self):
        return self.__gps_timeout


    def get_fix_timeout(self):
        return self.__fix_timeout


    def set_gps_timeout(self, value):
        self.__gps_timeout = value


    def set_fix_timeout(self, value):
        self.__fix_timeout = value



        
    
    def probe(self):
        
        stop   = int(round(time.time() )) + self.__fix_timeout
    
        while True:
                try:
                        # FIX Timeout
                        now = int(round(time.time() ))
                        
                        if now > stop :
                            self.__loc = None
                            print "fix timeout"
                            return False
                         
                        # GPS Timeout
                        if not self.__session.waiting(self.__gps_timeout  ):
                            self.__loc = None
                            print "gps timeout"
                            return False
        
             
                        report =  self.__session.next()

                        # Wait for a 'TPV' report and display the current time
                        if   report['class'] == 'TPV' :
                                      
                                if hasattr(report, 'mode')  and report.mode == 3 :
                                        if  hasattr(report, 'lat'):    self.__loc.set_latitude(  report.lat)
                                        if  hasattr(report, 'lon'):    self.__loc.set_longitude( report.lon)
                                        if  hasattr(report, 'alt'):    self.__loc.set_altitude(report.alt)
                                        if  hasattr(report, 'epx'):    self.__loc.set_lon_err(report.epx)
                                        if  hasattr(report, 'epy'):    self.__loc.set_lat_err(   report.epy)
                                        if  hasattr(report, 'epv'):    self.__loc.set_alt_err ( report.epv)

                                        return True
                
                except StopIteration:
                    return False
                
                except KeyboardInterrupt:
                    return False
            
        return True
        
     
        
    def get_location(self):
        return self.__loc
    
    def close(self):
        self.__session.close()
        
    
    def decimalDegrees2DMS(self,value,t):
        degrees = int(value)
        submin = abs( (value - int(value) ) * 60)
        minutes = int(submin)
        submilliseconds = int(abs( 100000 *  (submin-int(submin)) * 60))
        direction = ""
        if t == "Longitude":
            if degrees < 0:
                direction = "W"
            elif degrees > 0:
                direction = "E"
            else:
                direction = ""
        elif t == "Latitude":
            if degrees < 0:
                direction = "S"
            elif degrees > 0:
                direction = "N"
            else:
                direction = "" 
        degrees = abs(degrees)
        notation = str(degrees) + "/1," + str(minutes) + "/1," +\
                   str( submilliseconds) + "/100000" 
        return [notation, direction]
 

    def get_latitude(self, dms=False):
        if(dms):
            return self.decimalDegrees2DMS(self._lat, "Latitude")
        else:
            return self._lat
        

    def get_longitude(self, dms=False):
        if(dms):
            return self.decimalDegrees2DMS(self._lon, "Longitude")
        else:
            return self._lon
        
        
    def get_altitude( self, exif=False):
        if(exif):
            absalt = int(abs(self._alt))
            ref = 1 if self._alt < 0  else 0
            return [absalt, ref] 
        else:
            return self._alt       
