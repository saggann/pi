#!/usr/bin/python

import os.path

from  meteocam.sensors      import pigps
from  meteocam.io           import location_exporter
from  meteocam.config       import config
 

# import configuration
conf = config.Config(os.path.dirname(os.path.realpath(__file__)) + "/meteocam.cfg")
conf.load()


# read configuration
cfg = {}
cfg["gps_timeout"] = conf.mget( "location", "gps_timeout", 10)
cfg["fix_timeout"] = conf.mget( "location", "fix_timeout", 20)
cfg["server_url"] = conf.mget("general", "server_url", "https://meteocam.io")

print cfg

# Read location from GPS sensor
gps_probe  = pigps.PiGPS()

gps_probe.set_gps_timeout(cfg["gps_timeout"])
gps_probe.set_fix_timeout(cfg["fix_timeout"])



if ( gps_probe.probe() ) :
   
    loc = gps_probe.get_location()
    gps_probe.close()
        
    print "latitude : "    + str(loc.get_latitude())
    print "longitude : "   + str(loc.get_longitude())
    print "altitude : "    + str(loc.get_altitude())
    
    # Export Weather to meteocam server
    le = location_exporter.LocationExporter(loc, cfg["server_url"]) 
    response = le.post_json()
    print "json post response : " + str(response)

    
else:
    gps_probe.close()
    print "No GPS FIX"
    





