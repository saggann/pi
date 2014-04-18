'''
Created on 10 avr. 2014

@author: nicolas
'''

import json
import urllib2
import os

from meteocam.sensors import  pisystem

class ImageExporter(object):
    '''
    classdocs
    '''
    
    __urlRoot = "https://beta.meteocam.io"
    
    __sys   = None
    __img   = None

    def __init__(self, image, server_url="https://beta.meteocam.io"):
        '''
        Constructor
        '''
        self.__img = image        
        self.__sys = pisystem.PiSystem()
        self.__urlRoot = server_url

    def post_json(self):
        

        json_data = {
           "picture":{
            "picture_path":{
              "file":               self.__img.get_img64(),
              "original_filename":  self.__img.get_filename(),
              "filename":           self.__img.get_filename()
            }
          }
        }

        # Export data to local tmp file
        f = open('/tmp/image.json','w')
        f.write(json.dumps(json_data)) 
        f.close()
        
        #chown image
        os.chown('/tmp/image.json', 1000,1000)
        
        # Add uid and token to json data
        json_data.update({        
                          'uid':       self.__sys.get_uid(),
                          'token':     self.__sys.get_token()
                        })
        
        
        post_json_url = self.__urlRoot  + "/api/v1/devices/" + self.__sys.get_uid() + "/camera_pictures"

        try:
            req = urllib2.Request(post_json_url)
            req.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(req, json.dumps(json_data))
            return response.getcode()
        
         
        except urllib2.URLError:
            req = None
            return 404   
        
        

        
    