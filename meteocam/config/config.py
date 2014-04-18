'''
Created on 14 avr. 2014

@author: nicolas
'''

import ConfigParser
import os.path

__cfg =     None
__filename = ""

class Config(ConfigParser.ConfigParser):
    '''
    classdocs
    '''


    def __init__(self, filename=""):
        '''
        Constructor
        '''
        ConfigParser.ConfigParser.__init__(self)
        self.__filename = filename
        
        if os.path.isfile(filename):
            self.__filename = filename
        
    
    
    def load(self):
        if os.path.isfile(self.__filename):
            self.read(self.__filename)
            return True
        else:
            return False

    
    
    def save(self):
            with open( self.__filename, 'wb') as configfile:
                    self.write(configfile)
                    return True
            return False

    # Meteocam version of ConfigParser.get
    def mget(self, section, option, default=None):
        try:
            return  self.getint(section, option)            
        
        except ValueError:
            try:
                return self.getfloat(section, option)            
            except ValueError:
                try:
                    return self.getboolean(section, option)
                
                except ValueError:
                    return self.get(section, option)
        
        except ConfigParser.NoOptionError:
            return default
        
        except ConfigParser.NoSectionError:
            return default
        