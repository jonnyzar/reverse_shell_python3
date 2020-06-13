#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is client side which is gonna be controlled by means of 
reverse shell.
Once client is created, he connects to the listener, which controls 
the reverse shell.
"""
import socket


class Connection_Mgr:
    
    def __init__(self):
        self.c = None    
    

    def establish_conn(self,RHOST):
        """
        this function is to establish a connection to remote listener
        it runs in loops until it finds connection
        once found it returns connection object 
        """
        
        while 1:            
            #connection lifecycle loop
            self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                           
            try:
                self.c.connect(RHOST)  
                print (f"Successful connection at {RHOST}") 
                return self.c
                break
            except ConnectionRefusedError:
            #if connection refused then wait and retry
                print ("Connection refused... lets try to reconnect")
            except KeyboardInterrupt:
                self.c.close()
                print ("Excited gracefully")
                break
                 
        

def main():
    RADDR = '127.0.0.1'
    RPORT = 8888
    RHOST = (RADDR,RPORT)
    client_mgr = Connection_Mgr()
    c = None
    
    while 1:
        #client lifecycle loop     
        #establish connection with RHOST
        try:            
            c = client_mgr.establish_conn(RHOST) 
            if c != None:                    
                c.sendall(b'BIG HI') 
                resp = c.recv(1024)   
                print ('Received: ', repr(data)) 
        except KeyboardInterrupt:
            if c != None:
                c.close()
            print ("Excited gracefully")
            break
            
 
    return 0

if __name__ == '__main__':
    main()
