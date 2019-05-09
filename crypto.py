import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def get_ip():
    aiya = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        aiya.connect(('10.255.255.255',1))
        IP = aiya.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        aiya.close()
    return IP

server_address = (get_ip(), 8888)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)