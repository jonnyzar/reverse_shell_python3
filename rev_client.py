#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is client side which is gonna be controlled by means of 
reverse shell.
Once client is created, he connects to the listener, which controls 
the reverse shell.
"""



import socket



def main():
    RHOST = '127.0.0.1'
    RPORT = 8888

    #DGRAM : UDP, STREAM: DGRAM
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as c:
        c.connect((RHOST,RPORT)) 
        c.sendall(b'BIG HI') 
        resp = c.recv(1024)
    
    
    print ('Received: ', repr(data)) 
 
    
    return 0

if __name__ == '__main__':
    main()
