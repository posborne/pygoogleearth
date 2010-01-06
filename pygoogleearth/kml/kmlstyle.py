from kml.kmlabstract import KMLObject

class KMLStyleSelector(KMLObject):
    TAGNAME = 'StyleSelector'

class KMLStyle(KMLStyleSelector):
    TAGNAME = 'Style'

class KMLStyleMap(KMLStyleSelector):
    TAGNAME = 'StyleMap'

