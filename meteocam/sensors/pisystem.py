'''
Created on 10 avr. 2014

@author: nicolas
'''

import hashlib


class PiSystem(object):
    '''
    classdocs
    '''
    __serial = ""
    __uid = ""
    __token = ""

    def __init__(self):
        # Get CPU Serial
        try:
            f = open('/proc/cpuinfo','r')
            for line in f:
                if line[0:6]=='Serial':  
                    self.__serial =  line[10:26] 
                    self.__uid    =  hashlib.sha224(line[10:26]).hexdigest()
            f.close()
        except:
            self.__serial = "ERROR"
            self.__uid =    "ERROR"
             
             
        # Get token in scdard boot partition
        try:
            with open('/boot/token', 'r') as f:
                self.__token = f.readline().strip()
  
            f.close()
        except:
            self.__token = "ERROR"
   
             
             
    def get_uid(self):
        return self.__uid
 
 
    def get_token(self):
        return self.__token
      
