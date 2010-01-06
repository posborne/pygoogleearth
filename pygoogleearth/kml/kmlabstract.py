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
    
    def __init__(self, *args, **kwargs):
        self.attributes = {}
        for attribute in kwargs.keys():
            if attribute in self.ALLOWABLE_ATTRS:
                self.attributes[attribute] = kwargs[attribute]
        self.children = []
    
    def __setattr__(self, name, value):
        if name in self.ALLOWABLE_ATTRS:
            self.attributes[name] = value
        else:
            # Add the item to the dictionary as usual
            self.__dict__[name] = value
    
    def append(self, element):
        """Append the given element and return it for chaining
        
        We append the provided KMLObject to the list of elements for
        this KMLObject.  In the case that we do not receive a KMLObject
        or that object has the wrong type, we raise TypeError.
        
        It should be noted that the current element is always
        returned upon successful append.  This allows us to chain together
        operations as follows:
        >>> from pygoogleearth.kml import *
        >>> doc = KMLDocument()
        >>> # add a photo overlay and point to doc
        >>> (doc.append(KMLPhotoOverlay())
                .append(KMLPoint()))
        <<KMLDocument at ...>>
        """
        #if not isinstance(element, KMLObject):
        #    raise TypeError, "Value must be a KMLObject, not a %s" % type(element)
        if element.TAGNAME in self.ALLOWABLE_ELEMENTS or True:
            self.children.append(element)
            return element
        else:
            raise TypeError, "That element is not allowed for this KML object"
    
    def get_dom_node(self):
        """Get a DOM representation of this node"""
        element = minidom.Element(tagName=self.TAGNAME)
        
        # attributes
        attributes = getattr(self, 'attributes', {})
        for attr_key in attributes.keys():
            element.setAttribute(attr_key, attributes[attr_key])
            
        # children elements (we add recursivly)
        for encapsulated_element in self.children:
            element.appendChild(encapsulated_element.get_dom_node())
        
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

