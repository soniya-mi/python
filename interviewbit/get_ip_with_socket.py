import socket

hname=socket.gethostname()
ip=socket.gethostbyname(hname)

print hname
print ip
