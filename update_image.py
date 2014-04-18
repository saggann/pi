#!/usr/bin/python

import time
import os
import locale


from  meteocam.sensors       import mypicamera
from  meteocam.io            import image_exporter
from  meteocam.config        import config
 


# import configuration
conf = config.Config(os.path.dirname(os.path.realpath(__file__)) + "/meteocam.cfg")
conf.load()


# read configuration
cfg = {}
cfg["width"]    = conf.mget( "image", "width",     800)
cfg["height"]   = conf.mget( "image", "height",    600)
cfg["rotation"] = conf.mget( "image", "rotation",  270)
cfg["image_correction"] = conf.mget("image", "image_correction", 2)
cfg["server_url"] = conf.mget("general", "server_url", "https://meteocam.io")

print cfg


# Read Weather from BPM085
filename = "/tmp/image.jpg"




# Try to connect to camera and shoot temp image
try:
    cam = mypicamera.MyPiCamera()
    
    cam.set_h(cfg["height"])
    cam.set_w(cfg["width"])
    cam.set_rot(cfg["rotation"])
    cam.set_capture_delay(cfg["image_correction"] )
    
    
    cam.shot(filename)
    
except IOError:
    print "Camera sensor not detected"
    os._exit(1)
    
    

# get picture and print base64 encoding
pic =   cam.get_image()


os.environ['TZ'] = 'Europe/Paris'
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

time.tzset()
pic.date_image(time.strftime("%c"))


print "filename : " +     pic.get_filename()



# Export Image to meteocam server
ie = image_exporter.ImageExporter(pic, cfg["server_url"])
response = ie.post_json()
print "json post response : " + str(response)
