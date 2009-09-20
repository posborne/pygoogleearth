class CameraInfo(object):
    def __init__(self, comobject):
        self.ge_ci = comobject
    
    def __getattr__(self, name):
        if name == 'focus_point_latitude':
            return self.ge_ci.FocusPointLatitude
        elif name == 'focus_point_longitude':
            return self.ge_ci.FocusPointLongitude
        elif name == 'focus_point_altitude':
            return self.ge_ci.FocusPointAltitude
        elif name == 'focus_point_altitude_mode':
            return self.ge_ci.FocusPointAltitudeMode
        elif name == 'range':
            return self.ge_ci.Range
        elif name == 'tilt':
            return self.ge_ci.Tilt
        elif name == 'azimuth':
            return self.ge_ci.Azimuth
        else:
            raise AttributeError
    
    def __setattr__(self, name, value):
        if name == 'focus_point_latitude':
            self.ge_ci.FocusPointLatitude = value
        elif name == 'focus_point_longitude':
            self.ge_ci.FocusPointLongitude = value
        elif name == 'focus_point_altitude':
            self.ge_ci.FocusPointAltitude = value
        elif name == 'focus_point_altitude_mode':
            self.ge_ci.FocusPointAltitudeMode = value
        elif name == 'range':
            self.ge_ci.Range = value
        elif name == 'tilt':
            self.ge_ci.Tilt = value
        elif name == 'azimuth':
            self.ge_ci.Azimuth = value
        else:
            raise AttributeError
    