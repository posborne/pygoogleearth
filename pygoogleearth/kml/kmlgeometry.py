from pygoogleearth.kml.kmlabstract import KMLObject
from pygoogleearth.kml.kmlfields import KMLBooleanField, KMLEnumeration,\
    KMLCoordinateTupleList

class KMLGeometry(KMLObject):
    """
    This is an abstract element and cannot be used directly in a KML file. 
    It provides a placeholder object for all derived Geometry objects.
    """
    TAGNAME = 'Geometry'

class KMLPoint(KMLGeometry):
    TAGNAME = 'Point'

class KMLLineString(KMLGeometry):
    """
    Defines a connected set of line segments.
    
    Use <LineStyle> to specify the color, color mode, and width 
    of the line. When a LineString is extruded, the line is extended 
    to the ground, forming a polygon that looks somewhat like a wall 
    or fence. For extruded LineStrings, the line itself uses the 
    current LineStyle, and the extrusion uses the current PolyStyle. 
    See the KML Tutorial for examples of LineStrings (or paths).
    """
    TAGNAME = 'LineString'
    ALLOWABLE_ELEMENTS = [KMLBooleanField('extrude'), 
                          KMLBooleanField('tessellate'), 
                          KMLEnumeration('altitudeMode', ['clampToGround',
                                                          'relativeToGround',
                                                          'absolute']),
                          KMLCoordinateTupleList('coordinates')]
    

class KMLLinearRing(KMLGeometry):
    TAGNAME = 'LinearRing'

class KMLPolygon(KMLGeometry):
    TAGNAME = 'Polygon'

class KMLMultiGeometry(KMLGeometry):
    TAGNAME = 'MultiGeometry'

class KMLModel(KMLGeometry):
    TAGNAME = 'Model'

