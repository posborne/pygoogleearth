from pygoogleearth.kml.kmlabstract import KMLObject

class KMLStyleSelector(KMLObject):
    """
    This is an abstract element and cannot be used directly in a KML file. 
    It is the base type for the <Style> and <StyleMap> elements. The 
    StyleMap element selects a style based on the current mode of the 
    Placemark. An element derived from StyleSelector is uniquely 
    identified by its id and its url.
    """
    TAGNAME = 'StyleSelector'

class KMLStyle(KMLStyleSelector):
    """A Style defines an addressable style group that can be referenced by StyleMaps and Features. 
    
    Styles affect how Geometry is presented in 
    the 3D viewer and how Features appear in the Places panel of the List 
    view. Shared styles are collected in a <Document> and must have an 
    id defined for them so that they can be referenced by the individual 
    Features that use them.
    
    Use an id to refer to the style from a <styleUrl>.
    """
    TAGNAME = 'Style'

class KMLStyleMap(KMLStyleSelector):
    """A <StyleMap> maps between two different Styles. 
    
    Typically a <StyleMap> element is used to provide separate normal 
    and highlighted styles for a placemark, so that the highlighted 
    version appears when the user mouses over the icon in Google Earth.
    """
    TAGNAME = 'StyleMap'
    
