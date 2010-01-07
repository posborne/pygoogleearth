from pygoogleearth.kml.kmlabstract import KMLObject
from xml.dom import minidom

class KMLLeafNode(KMLObject):
    """KML Fields are leaf nodes in the KML tree and 
    contain concrete non-tag values
    
    Note:: This particular node is abstract (not designed 
           to be instantiated directly)
    """
    
    def __init__(self, tagname):
        """Initialize the leaf Node"""
        KMLObject.__init__(self)
        self.tagname = tagname
    
    def get_dom_node(self):
        """Get the DOM representation of the leaf node"""
        element = minidom.Element(tagName=self.tagname)
        text_node = minidom.Text()
        text_node.data = str(self)
        element.appendChild(text_node)
        return element

class KMLStringField(KMLLeafNode):
    def __init__(self, tagname):
        KMLLeafNode.__init__(self, tagname)
        self.value = ''
        
    def set_value(self, value):
        if not isinstance(value, basestring):
            raise TypeError
        self.value = value
        
    def get_value(self):
        return self.value
    
    def __str__(self):
        return self.value

class KMLBooleanField(KMLLeafNode):
    """Boolean KML fields"""
    
    def __init__(self, tagname):
        """Initialize the KML Boolean Field"""
        KMLLeafNode.__init__(self, tagname)
        self.value = None
    
    def set_value(self, value):
        """Handle a reassign of a boolean field"""
        if not isinstance(value, bool):
            raise ValueError, "Boolean fields must be set to bool"
        self.value = value
    
    def get_value(self):
        """Get the raw boolean value of this field"""
        return self.value
    
    def __str__(self):
        return {True: '1', False: '0'}[self.value]

class KMLEnumeration(KMLLeafNode):
    """Representation of KML Enumeration"""
    
    def __init__(self, tagname, enumerated_values):
        """Initialize the enumeration to allow the keys in enumerated_values"""
        KMLLeafNode.__init__(self, tagname)
        self.enumerated_value = set(enumerated_values)
        self.value = None
    
    def set_value(self, value):
        """Set the value of the enumeration.  The value must be in the
        enumerated set"""
        if value in self.enumerated_value:
            self.value = value
        else:
            raise ValueError, "Value given is not in the set %s" % self.enumerated_value
    
    def get_value(self):
        """Get the nodes current value or None if not set"""
        return self.value
    
    def __str__(self):
        return self.value if self.value is not None else ''

class KMLCoordinate(object):
    
    def __init__(self, latitude, longitude, altitude=0.0):
        self._latitude, self._longitude, self._altitude = 0.0, 0.0, 0.0
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        
    def __geattr__(self, name):
        if name == 'latitude':
            return self._latitude
        elif name == 'longitude':
            return self._longitude
        elif name == 'altitude':
            return self._longitude
    
    def __setattr__(self, name, value):
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError, "Must be a float or an integer"
        
        if name == 'latitude':
            if not (-90.0 <= value <= 90.0):
                raise ValueError, "Latitude outside valid range"
            self._latitude = float(value)
        elif name == 'longitude':
            if not (-180.0 <= value <= 180.0):
                raise ValueError, "Longitude outside valid range"
            self._longitude = float(value)
        elif name == 'altitude':
            self._altitude = float(value)
        else:
            raise AttributeError
        
    def __str__(self):
        return "%f,%f,%f" % (self._longitude, self._latitude, self._altitude)

class KMLCoordinateTupleList(KMLLeafNode):

    def __init__(self, tagname):
        KMLLeafNode.__init__(self, tagname)
        self.coordinates = []
    
    def __iter__(self):
        return iter(self.coordinates)
    
    def __getitem__(self, index):
        return self.coordinates[index]
    
    def __setitem__(self, index, value):
        if not isinstance(value, KMLCoordinate):
            raise ValueError, "Provided coordinate must be a KMLCoordinate"
        self.coordinates[index] = value
    
    def append_position(self, coordinate):
        if not isinstance(coordinate, KMLCoordinate):
            raise ValueError, "Provided coordinate must be a KMLCoordinate"
        self.coordinates.append(coordinate)
        
    def __str__(self):
        return '\n'.join([str(x) for x in self.coordinates])

class KMLSnippet(KMLObject):
    pass
    