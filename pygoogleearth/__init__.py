import time
import win32com.client

class AltitudeModes(object):
    RELATIVE_TO_GROUND = 0x1
    ABSOLUTE_ALTITUDE  = 0x2

class InitializationException(Exception):
    pass

class GoogleEarth(object):
    def __init__(self, timeout=None):
        """
        Create a GoogleEarth instance.  This initializer will block until the
        initialization succeeds or a timeout occurs (if one is specified). If
        a timeout does occur an InitializationException will be raised.
        """
        self.ge = win32com.client.Dispatch('GoogleEarth.ApplicationGE')
        starttime = time.clock()
        # Check for initialization every tenth second or so until we succeed
        # or timeout (if a timeout is specified)
        while not self.ge.IsInitialized() :
            if timeout is not None and time.clock() - starttime >= timeout:
                raise InitializationException, "Timeout while creating GoogleEarth wrapper"
            time.sleep(0.1)
    
    def get_camera(self, consider_terrain=False):
        """
        Get a dictionary containing the parameters for the current camera.
        These match the args which set_camera_params takes.
        
        Here's an example:
        >>> ge = GoogleEarth()
        >>> orpos = ge.get_camera() # grab our original position
        >>> ge.set_camera_params(44.9773194, -093.2639111) # move to minneapolis
        >>> time.sleep(5.0) # wait five seconds
        >>> orpos['alt'] = orpos['alt'] + 150000 # zoom out some
        >>> ge.set_camera_params(**orpos) # move back with modified alt (note that params match)
        """
        camera = self.ge.GetCamera(consider_terrain)
        camera_dict = {
            'lat': camera.FocusPointLatitude,
            'lon': camera.FocusPointLongitude,
            'alt': camera.FocusPointAltitude,
            'alt_mode': camera.FocusPointAltitudeMode,
            'range': camera.Range,
            'tilt': camera.Tilt,
            'azimuth': camera.Azimuth,
        }
        return camera_dict
        
    def set_camera_params(self, lat, lon, 
                          alt=300000, alt_mode=AltitudeModes.RELATIVE_TO_GROUND,
                          range=0, tilt=0, azimuth=370, speed=0.5):
        """
        This is an optimized way of setting the camera rather than using 
        SetCamera since it requires a much smaller number of COM calls.

        Parameters:
        lat       Latitude in degrees. Between -90 and 90.
        lon       Longitude in degrees. Between -180 and 180.
        alt       Altitude in meters.
        alt_mode  Altitude mode that defines altitude reference origin.
        range     Distance between focus point and camera in meters.
        tilt      Tilt angle in degrees. Between 0 and 90.
        azimuth   Azimuth angle in degrees.
        speed     Speed factor to use. Overrides autopilot speed. Value must be greater than 0. 
                  If greater than or equal to 5.0, the camera will immediately be set without any 
                  transition. This mode is called 'teleport'.
        """
        self.ge.SetCameraParams (lat, lon, alt, alt_mode, range, tilt, azimuth, speed)
    
    def save_screen_shot(self, filename, quality=90):
        """
        Save a screenshot of the current Google Earth view to the specified filename.
        Quality ranges from 0 to 100 with 100 being the highest quality image.
        """
        self.ge.SaveScreenShot(filename, quality)
        
if __name__ == '__main__':
    ge = GoogleEarth()
    orpos = ge.get_camera()
    ge.set_camera_params(44.9773194, -093.2639111) # move to minneapolis
    time.sleep(5.0) # wait five seconds
    ge.set_camera_params(**orpos) # move back
    print 'All done'