#!/usr/bin/python

from  meteocam.sensors      import pibmp085
from  meteocam.io           import weather_exporter
from  meteocam.config       import config

import os

# import configuration
conf = config.Config(os.path.dirname(os.path.realpath(__file__)) + "/meteocam.cfg")
conf.load()


# read configuration
cfg = {}
cfg["bmp085_mode"]    = conf.mget( "weather", "bmp085_mode", 2)
cfg["server_url"] = conf.mget("general", "server_url", "https://meteocam.io")

print cfg

# Read Weather from BPM085
try:
    bmp = pibmp085.PiBMP085(0x77, cfg["bmp085_mode"])

except IOError:
    print "Weather sensor not detected"
    os._exit(1)
    
if bmp.probe():
    
    w =   bmp.get_weather()

    print "pressure : " +    str(w.get_pressure())
    print "temperature : " + str(w.get_temperature())
    
    # Export Weather to meteocam server
    wo = weather_exporter.WeatherExporter(w, cfg["server_url"] )
    response = wo.post_json()
    print "json post response : " + str(response)

