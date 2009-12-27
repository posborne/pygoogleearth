from xml.dom import minidom
class KMLMetaClass(type):
    """Metaclass for all KML objects"""
    
    def __new__(cls, name, bases, dct):
        return type.__new__(cls, name, bases, dct)
    
    def __init__(cls, name, bases, dct):
        type.__init__(cls, name, bases, dct)
        
        # Add inheritance of allowable attributes
        parent_attrs = getattr(super(KMLMetaClass, cls), 'ALLOWABLE_ATTRS', [])
        my_attrs = getattr(cls, 'ALLOWABLE_ATTRS', [])
        cls.ALLOWABLE_ATTRS = my_attrs + parent_attrs
        
        # NOTE: allowable elements are not inherited but
        # we do add it in if it does not exist.  Also, we do not
        # want this inherited if not defined (which we want as an option)
        cls.ALLOWABLE_ELEMENTS = getattr(cls, 'ALLOWABLE_ELEMENTS', [])
        
class KMLObject(object):
    """This is an abstract base class and cannot be used directly in a 
    KML file attritribute, which allows unique identification 
    of a KML element, and the targetId attribute, which is used to 
    reference objects that e alredy been loaded into Google Earth. 
    The id attribute must be assined if the <Update> mechanism is to be used.
    """
    __metaclass__ = KMLMetaClass
    
    TAGNAME = 'Object' # Note: Abstract, but provided as reference
    ALLOWABLE_ATTRS = ['id', 'targetId',]
    
    def __init__(self, **kwargs):
        self.attributes = []
        self.children = []
    
    def get_dom_node(self):
        """Get a DOM representation of this node"""
        element = minidom.Element(tagName=self.TAGNAME)
        
        # attributes
        for attr_key, attr_value in getattr(self, 'attributes', {}):
            element.setAttribute(attr_key, attr_value)
            
        # children elements
        for encapsulated_element in self.children:
            element.appendChild(encapsulated_element)
        
        return element

class KMLSchema(KMLObject):
    """
    Specifies a custom KML schema that is used to add custom 
    data to KML Features. The "id" attribute is required and 
    must be unique within the KML file. <Schema> is always a 
    child of <Document>.
    
    A Schema element contains one or more SimpleField elements. 
    In the SimpleField, the Schema declares the type and name 
    of the custom field. It optionally specifies a displayName 
    (the user-friendly form, with spaces and proper punctuation 
    used for display in Google Earth) for this custom field.
    
    <SimpleField type="string" name="string">

    The declaration of the custom field, which must specify both 
    the type and the name of this field. If either the type or 
    the name is omitted, the field is ignored. The type can be 
    one of the following:
    * string
    * int
    * uint
    * short
    * ushort
    * float
    * double
    * bool
    
    <displayName>
    The name, if any, to be used when the field name is displayed 
    to the Google Earth user. Use the [CDATA] element to escape 
    standard HTML markup.
    """
    
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

