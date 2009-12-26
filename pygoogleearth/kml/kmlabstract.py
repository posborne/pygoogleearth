class KMLMetaClass(type):
    """Metaclass for all KML objects"""
    
    def __new__(cls, name, bases, dct):
        type.__new__(cls, name, bases, dct)
    
    def __init__(cls, name, bases, dct):
        type.__init__(name, bases, dct)
        parent_attrs = getattr(super(KMLMetaClass, cls), 'ATTRS', [])
        my_attrs = getattr(cls, 'ATTRS', [])
        cls.ATTRS = my_attrs + parent_attrs
        
class KMLObject(object):
    """This is an abstract base class and cannot be used directly in a 
    KML file attritribute, which allows unique identification 
    of a KML element, and the targetId attribute, which is used to 
    reference objects that e alredy been loaded into Google Earth. 
    The id attribute must be assined if the <Update> mechanism is to be used.
    """
    __metaclass__ = KMLMetaClass

class KMLStyleFeature(KMLObject):
    pass

class KMLAbstractView(KMLObject):
    pass

class KMLSubStyle(KMLObject):
    pass

class KMLLOD(KMLObject):
    pass

class KMLLatLonBox(KMLObject):
    pass

class KMLLatLonAltBox(KMLObject):
    pass

