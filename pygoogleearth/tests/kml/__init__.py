from pygoogleearth.kml import KMLDocument
from pygoogleearth.kml import KMLObject

if __name__ == '__main__':
    KMLTextNode = KMLLookAt = KMLLineString = KMLObject
    coords = """146.825,12.233,400
           146.820,12.222,400
           146.812,12.212,400
           146.796,12.209,400
           146.788,12.205,400"""
    
    kml = KMLDocument(id='testing')
    kml.append(KMLTextNode('name', 'gx:altitudeMode Example')
       .append(KMLLookAt().append(KMLTextNode('longitude', '146.806'))
                          .append(KMLTextNode('latitude', '12.219'))
                          .append(KMLTextNode('heading', '-60'))
                          .append(KMLTextNode('tilt', '70'))
                          .append(KMLTextNode('range', '6300'))
                          .append(KMLTextNode('gx:altitudeMode', 'relativeToSeaFloor')))
       .append(KMLLineString().append(KMLTextNode('extrude', '1'))
                              .append(KMLTextNode('gx:altitudeMode', 'relativeToSeaFloor'))
                              .append(KMLTextNode('coordinates', coords))))
    
    
    dom = kml.dom_view()
    print kml.pretty_xml_view()
    

# EXAMPLE KML
#<?xml version="1.0" encoding="UTF-8"?>
#<kml xmlns="http://www.opengis.net/kml/2.2"
# xmlns:gx="http://www.google.com/kml/ext/2.2">   <!-- required when using gx-prefixed elements -->
#
#<Placemark>
#  <name>gx:altitudeMode Example</name>
#  <LookAt>
#    <longitude>146.806</longitude>
#    <latitude>12.219</latitude>
#    <heading>-60</heading>
#    <tilt>70</tilt>
#    <range>6300</range>
#    <gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
#  </LookAt>
#  <LineString>
#    <extrude>1</extrude>
#    <gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
#    <coordinates>
#      146.825,12.233,400
#      146.820,12.222,400
#      146.812,12.212,400
#      146.796,12.209,400
#      146.788,12.205,400
#    </coordinates>
#  </LineString>
#</Placemark>
#
#</kml>
