import pygoogleearth

def construct_triangle_kml(lat, lon, size=0.02, name='triangle.kml'):
    """Given a lat, lon pair create a triangle at that point"""
    kml_template = """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>%(name)s</name>
        <open>0</open>
        <Placemark>
            <name>Triangle</name>
            <!--
            <Point id="X">
                 <extrude>0</extrude>
                 <altitudeMode>clampToGround</altitudeMode>
                 <coordinates>%(pt0)s</coordinates>
            </Point>
            -->
            <Polygon>
              <extrude>1</extrude>
              <outerBoundaryIs>
                <LinearRing>
                  <coordinates>
                    %(pt0)s
                    %(pt1)s
                    %(pt2)s
                  </coordinates>
                </LinearRing>
              </outerBoundaryIs>
            </Polygon>
        </Placemark>
    </Document>
    </kml>
    """
    kml = kml_template  % {'name': name,
                           'pt0': "%s,%s,0" % (lon, lat + size), # front
                           'pt1': "%s,%s,0" % (lon + size, lat - size), # top
                           'pt2': "%s,%s,0" % (lon - size, lat) # bottom
                           }
    return kml

if __name__ == '__main__':
    ge = pygoogleearth.GoogleEarth()
    for i in xrange(100):
        
        kml = r"""<?xml version="1.0" encoding="UTF-8"?>
        <kml xmlns="http://www.opengis.net/kml/2.2">
        <Document>
          <name>box.kml</name>
          <open>0</open>
          <Placemark>
            <name>hollow box</name>
            <Polygon>
              <extrude>1</extrude>
              <altitudeMode>relativeToGround</altitudeMode>
              <outerBoundaryIs>
                <LinearRing>
                  <coordinates>
                    -122.366278,37.818844,30
                    -122.365248,37.819267,30
                    -122.365640,37.819861,30
                    -122.366669,37.819429,30
                    -122.366278,37.818844,30
                  </coordinates>
                </LinearRing>
              </outerBoundaryIs>
              <innerBoundaryIs>
                <LinearRing>
                  <coordinates>
                    -122.366212,37.818977,30
                    -122.365424,37.819294,30
                    -122.365704,37.819731,30
                    -122.366488,37.819402,30
                    -122.366212,37.818977,30
                  </coordinates>
                </LinearRing>
              </innerBoundaryIs>
            </Polygon>
          </Placemark>
        </Document>
        </kml>"""
        
        ge.load_kml_data(kml)
    print 'KML Data Loaded'
