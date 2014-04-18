'''
Created on 10 avr. 2014

@author: nicolas
'''

import json
import urllib2

from meteocam.sensors import  pisystem

class LocationExporter(object):
    '''
    classdocs
    '''
    
    __urlRoot = "https://beta.meteocam.io"
    
    __sys = None
    __l   = None

    def __init__(self, location, server_url="https://beta.meteocam.io"):
        '''
        Constructor
        '''
        self.__l   = location        
        self.__sys = pisystem.PiSystem()
        self.__urlRoot = server_url

    def post_json(self):
        
        json_data = {
        'lat':      self.__l.get_latitude(),
        'lon':      self.__l.get_longitude(),
        'alt':      self.__l.get_altitude(),
        }

                             
        # Export data to local tmp file
        f = open('/tmp/location.json','w')
        f.write(json.dumps(json_data)) 
        f.close()
        
        # Add uid and token to json data
        json_data.update({        
                          'uid':       self.__sys.get_uid(),
                          'token':     self.__sys.get_token()
                        })
        
                                
        post_json_url = self.__urlRoot + "/api/v1/devices/" + self.__sys.get_uid() + "/locations"

        
        try:
            req = urllib2.Request(post_json_url)
            req.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(req, json.dumps(json_data))
            return response.getcode()
        
         
        except urllib2.URLError:
            req = None
            return 404   
        
        

        
    