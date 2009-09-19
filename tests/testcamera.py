import pygoogleearth

def test_camera_params():
    print 'Verify the camera goes to minneapolis'
    ge = pygoogleearth.GoogleEarth()
    lat, lon = 44.9773194, -093.2639111
    ge.set_camera_params(lat, lon)
    
if __name__ == '__main__':
    test_camera_params()