import math
import time
import random
import pygoogleearth

MIN_LAT = -90.0
MAX_LAT = 90.0
MIN_LON = -180.0
MAX_LON = 180.0
r = random.Random()

def random_camera_jump(google_earth):
    lat = r.random() * (MAX_LAT - MIN_LAT) + MIN_LAT
    lon = r.random() * (MAX_LON - MIN_LON) + MIN_LON
    google_earth.set_camera_params(lat, lon, range=1000000)
    return lat, lon
    
if __name__ == '__main__':
    ge = pygoogleearth.GoogleEarth()
    for i in xrange(5):
        lat, lon = random_camera_jump(ge)
        print "Jumping to %f, %f" % (lat, lon)
        time.sleep(5.0)
