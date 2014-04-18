'''
Created on 10 avr. 2014

@author: nicolas
'''

import json
import urllib2

from meteocam.sensors import  pisystem

class WeatherExporter(object):
    '''
    classdocs
    '''
    
    __urlRoot = "https://beta.meteocam.io"
    
    __sys = None
    __w   = None

    def __init__(self, weather, server_url="https://beta.meteocam.io"):
        '''
        Constructor
        '''
        self.__w = weather        
        self.__sys = pisystem.PiSystem()
        self.__urlRoot = server_url


    def post_json(self):
        
        # Weather data to json
        json_data = {
        'temp':      self.__w.get_temperature(),
        'pressure':  self.__w.get_pressure()
        }
                
        # Export data to local tmp file
        f = open('/tmp/weather.json','w')
        f.write(json.dumps(json_data)) 
        f.close()
        
        # Add uid and token to json data
        json_data.update({        
                          'uid':       self.__sys.get_uid(),
                          'token':     self.__sys.get_token()
                        })
        
        # Send data to meteocam server
        post_json_url = self.__urlRoot + "/api/v1/devices/" + self.__sys.get_uid() + "/weathers"
        

        req= None
        response = None
        
        try:
            req = urllib2.Request(post_json_url)
            req.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(req, json.dumps(json_data))
            return response.getcode()
        
        except urllib2.HTTPError as e:
            return e.code
         
        except urllib2.URLError:
            req = None
            return 404   
        
        

        
    