#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
#  AUTHOR IS NOT RESPONSIBLE FOR ANY CONSEQUENCES CAUSED BY USE
#  OF THIS PROGRAM
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

