import SimpleXMLRPCServer
import geapplication
 
class GoogleEarthXMLRPCServer(SimpleXMLRPCServer.SimpleXMLRPCServer):
    """
    # Example Server Creation:
    import pygoogleearth
    rpcserver = pygoogleearth.GoogleEarthXMLRPCServer(('localhost', 9500))
    rpcserver.serve_forever()
    # Example Client
    import xmlrpclib
    google_earth = xmlrpclib.ServerProxy('http://localhost:9500')
    google_earth.set_camera_params(50.234392, -94.234343)
    """
    # TODO: what about properties from __getattr__, __setattr__?
    def __init__(self, *args, **kwargs):
        SimpleXMLRPCServer.SimpleXMLRPCServer.__init__(self, *args, allow_none=True, **kwargs)
        self.register_instance(geapplication.GoogleEarth())
    
if __name__ == '__main__':
    print 'Dishing up Google Earth on port 9000'
    server = GoogleEarthXMLRPCServer(('localhost', 9000))
    server.serve_forever()