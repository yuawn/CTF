#!/usr/bin/env python
from pwn import *
import time

print int( time.time() / 60 % 60 )

host , port = 'eof-exam3.ais3.org' , 7122
y = remote( host , port )

y.sendlineafter( '>' , '1' )

def wri( idx , code ):
    y.sendlineafter( '>' , '1' )
    y.sendlineafter( ':' , str( idx ) )
    sleep( 0.1 )
    y.sendline( code )

def burn( idx ):
    y.sendlineafter( '>' , '2' )
    y.sendlineafter( ':' , str( idx ) )

def submit( idx , tok = 'zFErzItq' ):
    y.sendlineafter( '>' , '3' )
    y.sendlineafter( ':' , str( idx ) )
    y.sendlineafter( 'token:' , tok )



ans = 'Th1s 1s EOF CTF, 4nd th3 TA is v3ry KIANG!!!'
ans = 'Th1s 1s EOF CTF, 4nd th3 TA is v3ry KIA!G!!!'

add = 'red'
sub = 'blue'
inc = 'yellow'
dec = 'cyan'
pc = 'green'
ora = 'orange'
pin = 'pink'


p = ''
for c in ans[:-4]:
    p += inc * ord( c )
    p += pc
    p += add

wri( 0 , p + 'a' )
burn( 0 )

p = (pc + add) * 0x26 + pc
p += sub
p += inc * ( ord( 'N' ) - ord( 'I' ) )
p += pc
p += add
p += inc * ( ord( 'G' ) - ord( 'A' ) )
p += pc
p += add
p += pc * 3


print len( p )
wri( 1 , p )
#burn( 1 )
submit( 1 )

print y.recvall(timeout=3)
#print y.recvuntil( '+' )
y.close()
#y.interactive()