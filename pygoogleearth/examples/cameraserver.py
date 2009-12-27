import pygoogleearth
import socket
import select
ge = pygoogleearth.GoogleEarth()

def camera_server(port):
    print 'Running camera server on port ', port
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('', port))
    while True:
        data = server.recv(1024)
        if not data: break
        [lat, lon, range] = map(float, data.split(','))
        print "Received: ", [lat, lon, range]
        ge.set_camera_params(lat, lon, range=range)

if __name__ == '__main__':
    import sys
    camera_server(int(sys.argv[1]))
    import time
    time.sleep(3.0)
    print 'Sending data to server over UDP'
    test_camera_server(int(sys.argv[1]))
