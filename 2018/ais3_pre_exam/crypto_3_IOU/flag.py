#!/usr/bin/env python
from pwn import *
from hashlib import sha256
import random , string

# AIS3{D0cT0R StRaNG3 - F0rgERy ATTaCk Ag4InsT RSa DIgital SigNatUrE}

# (m,s) s ^ e mod n = m

host , port = '104.199.235.135' , 20002
y = remote( host , port )


y.recvuntil( '== \'' )
a = y.recv( 6 )
print a
y.recvuntil( '== \'' )
b = y.recv( 6 )
print b

p = range(48,58) + range(65,91) + range(97,123)
sol = ''

for i in xrange( 0x100000000 ):
    sol = a + str( i )
    if sha256( sol ).hexdigest().startswith( b ):
        break

y.sendlineafter( '=' , sol )

y.recvuntil( 'n = ' )
n = int( y.recvline().strip() )
y.recvuntil( 'e = ' )
e = int( y.recvline().strip() )
print n
print e

s = 0



print 'trying.......'

for ss in xrange( 0xfffffff ):
    m = hex( pow( ss , e , n ) )[2:]
    if len(m) % 2:
        m = '0' + m
    m = ''.join( chr( int( i , 16 ) ) for i in re.findall( '..' , m ) )
    if len( m.split() ) > 3:
        try:
            if int( m.split()[3] ) > 10:
                s = ss
                print 'win!' , s
                break
        except:
            pass

y.sendlineafter( '=' , str( pow( s , e , n ) ) )

y.sendlineafter( '=' , str( s ) )

y.interactive()