from kml.kmlabstract import KMLObject

class KMLGeometry(KMLObject):
    """
    This is an abstract element and cannot be used directly in a KML file. 
    It provides a placeholder object for all derived Geometry objects.
    """
    TAGNAME = 'Geometry'

class KMLPoint(KMLGeometry):
    TAGNAME = 'Point'

class KMLLineString(KMLGeometry):
    TAGNAME = 'LineString'

class KMLLinearRing(KMLGeometry):
    TAGNAME = 'LinearRing'

class KMLPolygon(KMLGeometry):
    TAGNAME = 'Polygon'

class KMLMultiGeometry(KMLGeometry):
    TAGNAME = 'MultiGeometry'

class KMLModel(KMLGeometry):
    TAGNAME = 'Model'

