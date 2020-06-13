#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is server side or so called "listener".
Once client is activated it connects to listener that
can issue commands to client.
"""


import socket


def main():
    LHOST = '127.0.0.1'
    LPORT = 8888

    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((LHOST,LPORT))
        s.listen(5) #server can work with maximum 5 clients
        
        
        #result = s.recv(1024)
        #print ('Message: ',   result.decode('utf-8'))
  
    
    return 0

if __name__ == '__main__':
    main()

