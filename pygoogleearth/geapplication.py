import time
from animationcontroller import AnimationController
from camerainfo import CameraInfo
from featurecollection import FeatureCollection
from tourcontroller import TourController
from searchcontroller import SearchController
from viewextents import ViewExtents

try:
    import win32com.client
except ImportError, e:
    print 'You may not have win32com installed.  win32com is included in pywin32'
    print 'which can be found here: http://sourceforge.net/projects/pywin32/'
    raise e

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
    
    def __getattr__(self, name):
        if name == 'streaming_progress_percentage': 
            return self.ge.StreamingProgressPercentage
        elif name == 'auto_pilot_speed': 
            return self.ge.StreamingProgressPercentage
        elif name == 'view_extents': 
            return ViewExtents(self.ge.ViewExtents)
        elif name == 'version_major': 
            return self.ge.VersionMajor
        elif name == 'version_minor': 
            return self.ge.VersionMinor
        elif name == 'version_build': 
            return self.ge.VersionBuild
        elif name == 'version_app_type': 
            return self.ge.VersionAppType
        elif name == 'elevation_exaggeration': 
            return self.ge.ElevationExaggeration
        elif name == 'tour_controller': 
            return TourController(self.ge.TourController)
        elif name == 'search_controller': 
            return SearchController(self.ge.SearchController)
        elif name == 'animation_controller': 
            return AnimationController(self.ge.AnimationController)
        else:
            raise AttributeError
        
    def __setattr__(self, name, value):
        if name == 'streaming_progress_percentage': 
            self.ge.StreamingProgressPercentage = value
        elif name == 'auto_pilot_speed': 
            self.ge.StreamingProgressPercentage = value
        elif name == 'view_extents': 
            self.ge.ViewExtents = value.ge_ve
        elif name == 'version_major': 
            self.ge.VersionMajor = value
        elif name == 'version_minor': 
            self.ge.VersionMinor = value
        elif name == 'version_build': 
            self.ge.VersionBuild = value
        elif name == 'version_app_type': 
            self.ge.VersionAppType = value
        elif name == 'elevation_exaggeration': 
            self.ge.ElevationExaggeration = value
        elif name == 'tour_controller': 
            self.ge.TourController = value.ge_tc
        elif name == 'search_controller': 
            self.ge.SearchController = value.ge_sc
        elif name == 'animation_controller': 
            self.ge.AnimationController = value.ge_ac
        else:
            self.__dict__[name] = value

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
    
    def get_feature_by_href(self, href):
        """
        Returns the feature with a given href.
        Searches for feature in the Places and Layers panels and returns it as a IFeatureGE.
        
        href is case sensitive and uses forward slashes '/' as the directory delimiter.
        href is in the format: FileName#FeatureID
        
        For example, if you have a KML file C:/simple.kml, with the following placemark:
        <Placemark id="SomeID">
        
        then the corresponding href would be:
        C:/simple.kml#SomeID
        
        Although not all features have hrefs, an href is a unique identifier (unlike a name).
        
        Parameters:
                href     String that identifies feature as explained above.
                pFeature     Output feature matching given href. If no feature is found 
                             matching href, then it is set to NULL.
        """
        self.ge.GetFeatureByHref(href)
        
    def get_feature_by_name(self, name):
        """
        Retrieves a feature matching a given name.

        Returns the first feature with the given name by searching in the "Search Results", 
        "Places", and "Layers" panels and returning it as a IFeatureGE.
        
        Note:
            A name is not necessarily unique, so another option is to use 
            GetFeatureByHref, which some features support.
        
        Parameters:
        name       Feature name to be retrieved
        pFeature   Output feature. If there is more than one feature with given name, 
                   returns first instance. If no features exist with given name, returns NULL.
        """
        self.ge.GetFeatureByName(name)
        
    def get_highlighted_feature(self):
        """
        Retrieves currently highlighted feature (i.e. with focus).
        
        If there is no currently selected feature, this method returns None.

        Parameters:
        pFeature     Output highlighted feature. If no feature is highlighted, this is set to NULL.
        """
        highlighted = self.ge.GetHighlightedFeature()
        
    def get_layers_database(self):
        pass
    
    def get_main_hwnd(self):
        pass
    
    def get_render_hwnd(self):
        pass
    
    def get_my_places(self):
        """
        Retrieves My Places folder.
        
        Parameters:
        pMyPlaces     Output feature for My Places folder. If folder is unavailable, this is set to NULL.
        """
        pass
    
    def get_temporary_places(self):
        """
        Retrieves Temporary Places folder.
        
        Parameters:
        pTemporaryPlaces     Output feature for Temporary Places. folder. If folder is unavailable, this is set to NULL.
        """
        pass
        
    def get_point_on_terrain_from_screen_coords(self, screen_x, screen_y):
        """
        Returns point on terrain from screen coordinates.

        This method allows an external application to query the geolocation and terrain altitude 
        of a point in the 3D viewpoint identified by its normalized screen coordinates 
        (screen_x, screen_y), ranging from (-1, -1) to (+1, +1) inclusive.
        
        Here are some examples:
            * (-1, -1) - bottom left hand corner of the screen.
            * (0,0) - center of the screen.
            * (1, 1) - top right hand corner of the screen.
        
        To convert from pixel coordinates to these normalized screen coordinates, it may be helpful 
        to use GetRenderHwnd and retrieve the render window's position and dimensions for these computations.
        
        The coordinates of the point on terrain are returned in as a IPointOnTerrainGE.
        If the input screen coordinates do not intersect with the globe, then this function returns 
        the projected point on the globe's horizon and with the 
        IPointOnTerrainGE::ProjectedOntoGlobe set to true.
        
        The IPointOnTerrainGE::Altitude is set in the following way:
            * if ElevationExaggeration is non-zero, then IPointOnTerrainGE::Altitude is set to be the terrain's 
              true altitude and IPointOnTerrainGE::ZeroElevationExaggeration is set to false, or
            * if ElevationExaggeration is zero, then IPointOnTerrainGE::Altitude is set to zero and 
              IPointOnTerrainGE::ZeroElevationExaggeration is set to true.
        
        Parameters:
        screen_x   Normalized screen position along the x axis. Valid range is from -1 
                   (left hand side of the screen) to +1 (right hand side of the screen). 
                   Values outside the valid range are clamped.
        screen_y   Normalized screen position along the y axis. Valid range is from -1
                   (bottom of the screen) to +1 (top of the screen). Values outside the
                   valid range are clamped.
        """
        terrain_point = self.ge.GetPointOnTerrainFromScreenCoords(screen_x, screen_y)
        return gehelper.point_dict_from_terrain_point(terrain_point)

    def hide_description_balloons(self):
        """
        Hides all visible description balloons.
        
        Turns off any visible description balloons for all features.
        """
        self.ge.HideDescriptionBalloons()

    def is_online(self):
        """
        Returns whether the application is connected to the data server or not.
        
        If the application is connected to the server, then Google Earth uses the server's Layers databases. 
        Otherwise, it uses local cached Layers databases.
        
        Parameters:
        isOnline     Output status.
        """
        return self.ge.IsOnline()

    def load_kml_data(self, kml_data):
        """
        Loads KML into Google Earth.
        This loads KML data from a string as opposed to loading from a file.
        
        Parameters:
        kml_data     String containing KML data. This must contain valid KML data.
        """
        self.ge.LoadKmlData(kml_data)
        
    def open_km_file(self, filename, suppress_messages=False):
        """
        Schedules a KML file to be loaded in Google Earth.

        Parameters:
        filename          The full path name of the file to be loaded, with forward slashes '/'
                          as the directory delimiter character. If possible, the application will 
                          fly to the view of the feature(s) that were created after opening that file.
        suppress_messages If true, ignores all common KML loading dialog boxes warnings and errors, and 
                          chooses the default option for each one. For example, this function ignores 
                          confirmations to reload a previously loaded KML file and losing unsaved changes. 
                          This function will not ignore dialog boxes with critical errors such as 
                          when core libraries cannot be loaded.
        """
        self.ge.OpenKmlFile(filename, suppress_messages)


    def save_screen_shot(self, filename, quality=90):
        """
        Save a screenshot of the current Google Earth view to the specified filename.
        Quality ranges from 0 to 100 with 100 being the highest quality image.
        """
        self.ge.SaveScreenShot(filename, quality)

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
        self.ge.SetCameraParams(lat, lon, alt, alt_mode, range, tilt, azimuth, speed)

    def set_feature_view(self, feature_view, speed=0.0):
        """
        Flies to the view of the given feature at the specified speed.
        This method fails if the specified feature has no view.
        """
        retval = self.ge.SetFeatureView(feature_view, speed)
        # TODO: handle return values
        
    def show_feature_balloon(self, feature):
        """
        Displays the description balloon for a given feature.

        Shows the description balloon for a feature that has a view. 
        This method fails if the specified feature has no view.
        
        Note:
        Turning on the description balloon for a feature may turn off the 
        description balloons for other features.
        """
        self.ge.ShowFeatureBalloon(feature)
        