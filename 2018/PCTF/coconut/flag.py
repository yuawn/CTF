#!/usr/bin/env python
from pwn import *

# PCTF{Y0u_Just_Imp!em3nt3D_A_LLVM_pass!}

host , port = 'coconut.chal.pwning.xxx' , 6817
y = remote( host , port )

while True:
    try:
        y.recvuntil( '<= ' )
        th = int( y.recvline()[:-1] )
    except:
        y.interactive()

    y.recvuntil( 'ze:' )

    s = y.recvuntil( 'ret' ).split( '\n' )

    y.recvuntil( '>=' )
    a = int( y.recvuntil( ' ' )[:-1] )
    y.recvuntil( '<=' )
    b = int( y.recvuntil( ':' )[:-1] )

    ans = []
    p = []
    p.append( s[b].split( '\t' )[2].split( ', ' )[0] )

    for i in range( b - 1 , a - 1 , -1 ):
        c = s[i].split( '\t' )
        arg = c[2].split( ', ' )

        if c[1] == 'notl':
            if arg[0] not in p:
                ans.append( int( c[0] ) )

        if c[1] == 'notl':
            continue

        if arg[1] in p:
            if c[1] == 'leal':
                l1 , l2 = arg[0][1:-1].split(',')[0].replace( 'r' , 'e' ) , arg[0][1:-1].split(',')[1].replace( 'r' , 'e' )
                if l1 not in p:
                    p.append( l1 )
                if l2 not in p:
                    p.append( l2 )
                if l1 != arg[1] and l2 != arg[1]:
                    del p[ p.index( arg[1] ) ]  

            else:
                if arg[0] not in p:
                    p.append( arg[0] )
                if c[1] == 'movl':
                    try:
                        del p[ p.index( arg[1] ) ]
                    except:
                        pass
        else:
            ans.append( int( c[0] ) )

    ans.sort()

    t = 0
    c = 0
    d = ''

    for i in ans:
        if  i - t > 1 and t:
            d += str( t ) + '\n'
            c = 0
        elif t:
            if not c:
                d += str( t ) + '-'
                c = 1
        t = i

    d += str( ans[-1] ) + '\n'
    y.send( d + '#\n' )

y.interactive()