import socket, sys

def test_camera_server(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect(('localhost', port))
    lat, lon, range = 40.826, -101.0, 700000
    client.send(','.join(map(str, [lat, lon, range])))
    
if __name__ == '__main__':
    print 'Testing camera server'
    test_camera_server(int(sys.argv[1]))