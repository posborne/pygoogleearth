from kml.kmlabstract import KMLObject
import xml.dom

__all__ = ['KMLFeature', 'KMLOverlay', 'KMLPlacemark', 
           'KMLContainer', 'KMLDocument', 'KMLFolder', 
           'KMLPhotoOverlay', 'KMLGroundOverlay', 'KMLScreenOverlay']

class KMLFeature(KMLObject):
    """
    NOTE:: This is an abstract element and cannot be used directly 
    in a KML file.
    """
    
    def __init__(self, **kwargs):
        KMLObject.__init__(self, **kwargs)
    
class KMLOverlay(KMLFeature):
    """
    NOTE:: This is an abstract element and cannot be used directly 
    in a KML file. 
    
    <Overlay> is the base type for image overlays drawn on the planet 
    surface or on the screen. <Icon> specifies the image to use and 
    can be configured to reload images based on a timer or by camera 
    changes. This element also includes specifications for stacking 
    order of multiple overlays and for adding color and transparency 
    values to the base image.
    """

    ATTRS = ['color', 'drawOrder', 'Icon']
    
    def __init__(self, **kwargs):
        KMLFeature.__init__(self, **kwargs)
    
class KMLPlacemark(KMLFeature):
    """A Placemark is a Feature with associated Geometry. 
    
    In Google Earth, a Placemark appears as a list item in the 
    Places panel. A Placemark with a Point has an icon associated 
    with it that marks a point on the Earth in the 3D viewer. 
    (In the Google Earth 3D viewer, a Point Placemark is the 
    only object you can click or roll over. Other Geometry objects 
    do not have an icon in the 3D viewer. To give the user something 
    to click in the 3D viewer, you would need to create a MultiGeometry 
    object that contains both a Point and the other Geometry object.)
    
    Contained By: KMLDocument, KMLFolder
    """
    
    def __init__(self, **kwargs):
        KMLFeature.__init__(self, **kwargs)
    
class KMLContainer(KMLFeature):
    """A Container element holds one or more Features and allows the creation 
    of nested hierarchies.
    
    NOTE:: This is an abstract element and cannot be used directly 
    in a KML file. 
    """
    
    ATTRS = ['name', 'visibility', 'open', 'address',
             'AddressDetails', 'phoneNumber', 'Snippet',
             'description', 'AbstractView', 'TimePrimitive',
             'styleUrl', 'StyleSelection', 'Region', 'Metadata',]
    
    def __init__(self, **kwargs):
        pass
    
    
class KMLDocument(KMLContainer):
    """
    A Document is a container for features and styles. This element 
    is required if your KML file uses shared styles. It is recommended 
    that you use shared styles, which require the following steps:
    1. Define all Styles in a Document. Assign a unique ID to each Style.
    2. Within a given Feature or StyleMap, reference the Style's ID using 
       a <styleUrl> element.
    
    Note:: shared styles are not inherited by the Features
           in the Document.
    """
    
    def __init__(self, **kwargs):
        KMLContainer.__init__(self, **kwargs)
    
class KMLFolder(KMLContainer):
    """
    A Folder is used to arrange other Features hierarchically 
    (Folders, Placemarks, NetworkLinks, or Overlays). A Feature 
    is visible only if it and all its ancestors are visible.
    """
    
    def __init__(self, **kwargs):
        KMLContainer.__init__(self, **kwargs)
    
    
class KMLPhotoOverlay(KMLOverlay):
    """
    The <PhotoOverlay> element allows you to geographically locate 
    a photograph on the Earth and to specify the placement and 
    orientation of the Camera that views this PhotoOverlay. The 
    PhotoOverlay can be a simple 2D rectangle, a partial or full 
    cylinder, or a sphere (for spherical panoramas). The overlay 
    is placed at the specified location and oriented toward the 
    Camera.
    """
    
    ATTRS = ['rotation', 'ViewVolume', 'ImagePyramid',
             'Point', 'shape', ]

    def __init__(self, **kwargs):
        KMLOverlay.__init__(self, **kwargs)

class KMLScreenOverlay(KMLOverlay):
    """
    This element draws an image overlay fixed to the screen. 
    Sample uses for ScreenOverlays are compasses, logos, and 
    heads-up displays. ScreenOverlay sizing is determined 
    by the <size> element. Positioning of the overlay is 
    handled by mapping a point in the image specified by 
    <overlayXY> to a point on the screen specified by 
    <screenXY>. Then the image is rotated by <rotation> 
    degrees about a point relative to the screen specified by 
    <rotationXY>.
    
    The <href> child of <Icon> specifies the image to be used 
    as the overlay. This file can be either on a local file 
    system or on a web server. If this element is omitted or 
    contains no <href>, a rectangle is drawn using the color 
    and size defined by the screen overlay.
    """
    
    ATTRS = ['overlayXY', 'screenXY', 'rotationXY',
             'size', 'rotation']
    
    def __init__(self, **kwargs):
        KMLOverlay.__init__(self, **kwargs)


class KMLGroundOverlay(KMLOverlay):
    """
    This element draws an image overlay draped onto the terrain. 
    The <href> child of <Icon> specifies the image to be used 
    as the overlay. This file can be either on a local file 
    system or on a web server. If this element is omitted or 
    contains no <href>, a rectangle is drawn using the color 
    and LatLonBox bounds defined by the ground overlay.
    """
    
    ATTRS = ['altitude', 'altitudeMode', 'LatLonBox',]
    
    def __init__(self, **kwargs):
        KMLOverlay.__init__(self, **kwargs)


