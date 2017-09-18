#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *
from requests import *
import re

# Bugs_Bunny{M4TH_LO0k!_HarD_But_s0_EA5Y}

host , port = '34.253.165.46' , 11223
#host , port = '192.168.78.133' , 4000
y = remote( host , port )
y.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
y.recvline()
#y.recvuntil( ':' )

#y.recvuntil( ':' )
#now = y.recv(1024).split(' ')
#print now
#    if now[3] == '+'

l = {
    'New Hampshire': 'Concord',
    'Colorado': 'Denver',
    'Georgia': 'Atlanta',
    'Tennessee': 'Nashville',
    'Florida': 'Tallahassee',
    'Montana': 'Helena',
    'Alabama': 'Montgomery',
    'Oregon': 'Salem',
    'California': 'Sacramento',
    'Connecticut': 'Hartford',
    'Kentucky': 'Frankfort',
}

URL = 'https://en.wikipedia.org/wiki/'

#o = get( URL + 'Florida' )
#o2 = o.text[ o.text.find( 'Capital</a>' ) : ]
#o2 = o2.split('\n')[1]
#print o2.split('\n')[0]
#print o2[ o2.find("\">") + 2 : o2.find("</a>") ]
#print o2.split('\n')[2]

i = 1

while True:
    print i
    i = i + 1
    try:
        ot = y.recvuntil(':')
        print ot
    except:
        print y.recvall()
    now = y.recvline().split(' ')
    print now
    if len( now[1] ) > 1:
        state = ' '.join( i for i in now[1:] ).strip()
        print state
        state = state.replace( 'New York' , 'New_York_(state)' )
        state = state.replace( 'Georgia' , 'Georgia_(U.S._state)' )
        print state
        if state == 'Connecticut':
            y.sendline( 'Hartford' )
            continue
        elif state == 'Washington':
            y.sendline( 'Olympia' )
            continue
        try:
            o = get( (URL + state).strip() )
            #print URL + state
            #print o.text
            o2 = o.text[ o.text.find( 'Capital</a>' ) : ]
            o2 = o2.split('\n')
            if '</a></td>' not in o2[1]:
                o2 = o2[2]
            else:
                o2 = o2[1] 
            ans = o2[ o2.find("\">") + 2 : o2.find("</a>") ]
            print ans
            y.sendline( o2[ o2.find("\">") + 2 : o2.find("</a>") ] )
            #y.interactive()
        except:
            print 'Ohh'
            print y.recvall()

    elif now[2] == '+':
        y.sendline( str( int( now[5] ) - int( now[3] ) ) )
    elif now[2] == '-':
        y.sendline( str( int( now[5] ) + int( now[3] ) ) )
    elif now[2] == '*':
        y.sendline( str( int( now[5] ) / int( now[3] ) ) )
    else:
        y.sendline( str( int( now[5] ) * int( now[3] ) ) )


#y.interactive()