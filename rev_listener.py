#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is server side or so called "listener".
Once client is activated it connects to listener that
can issue commands to client.
"""


import socket

"""
#for use of with statement
from contextlib import contextmanager

@contextmanager
def socketcontext(*args, **kw):
    s = socket.socket(*args, **kw)
    try:
        yield s
    finally:
        s.close()

with socketcontext(socket.AF_INET, socket.SOCK_DGRAM) as s:
"""


def main(args):
    
    #SOCK_STREAM: TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #bind server socket to ip and port
    s.bind(('127.0.0.1',8888))
    result = s.recv(1024)
    print ('Message: ',   result.decode('utf-8'))
    s.close()
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
