from kml.kmlabstract import KMLObject

class KMLGeometry(KMLObject):
    """
    This is an abstract element and cannot be used directly in a KML file. 
    It provides a placeholder object for all derived Geometry objects.
    """

class KMLPoint(KMLGeometry):
    pass

class KMLLineString(KMLGeometry):
    pass

class KMLLinearRing(KMLGeometry):
    pass

class KMLPolygon(KMLGeometry):
    pass

class KMLMultiGeometry(KMLGeometry):
    pass

class KMLModel(KMLGeometry):
    pass

