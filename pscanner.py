import socket  # importing library

ip = socket.gethostbyname("hackthissite.org")
try:
    for port in range(1024):
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.settimeout(.25)
        result = serv.connect_ex((ip, port))
        if result == 0:
            print('[OPEN] Port open :', port)
        serv.close()
except socket.error as msg:
    print('[nothing]')