#-*- encoding: utf-8 -*-
#Xml https client
#@ Author: bulele
#@ Use: python xmlhttps.py 192.168.1.17 9999 /cgi-bin/xmlrpc_server 7201020120.xml

import ssl
import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
uri = sys.argv[3]
xml = sys.argv[4]

with open(xml,'r') as f:
    file = f.read()
    print (file)

length=len(file)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_TLSv1_2)

msg='POST '+uri+' HTTP/1.1\r\nContent-Type: text/xml\r\nContent-Length: '+str(length)+'\r\nConnection: close\r\nhost: '+str(ip)+'\r\n\r\n'+file

s.sendall(msg.encode())    # the python3 send message as bytes, so need to encode str to byte

while True:

    new = s.recv(4096)
    if not new:
      s.close()
      break
    print (new.decode())   # decode bytes, so can display it orderly
