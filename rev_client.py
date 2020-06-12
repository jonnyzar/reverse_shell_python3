#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is client side which is gonna be controlled by means of 
reverse shell.
Once client is created, he connects to the listener, which controls 
the reverse shell.
"""



import socket



def main(args):
    
    #SOCK_STREAM: TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b'MESSAGA', ('127.0.0.1',8888))
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
