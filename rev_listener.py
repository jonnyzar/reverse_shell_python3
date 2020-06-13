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
listener
"""

import socket        



def main():
    LADDR = '127.0.0.1'
    LPORT = 8888
    LHOST = (LADDR, LPORT)
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(LHOST)
    s.listen(5)

    
    while True:
        try:
            client, addr = s.accept() 
        except KeyboardInterrupt:
            s.close()
            break
        else:
            data = client.recv(4096)
            print(data.decode('utf-8'))    
 

            
    return 0

if __name__ == '__main__':
    main()

