#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is server side or so called "listener".
Once client is activated it connects to listener that
can issue commands to client.

Parameter Description:
c:client
s:server
"""


import socket


def main():
    LHOST = '127.0.0.1'
    LPORT = 8888

    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((LHOST,LPORT))
        s.listen(5) #server can work with maximum 5 clients
        #loop for adding clients on connection
        while 1:
            try:
                c, addr = s.accept()
            except KeyboardInterrupt:
                s.close()
                break
            else:
                #get client message
                c_message = c.recv(1024) 
                print ('Message: ',   c_message.decode('utf-8'))   
            
    return 0

if __name__ == '__main__':
    main()

