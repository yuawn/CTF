#!/usr/bin/env python3
#from pwn import *
import re

# hitcon{M0mmy_I_n0w_kN0w_h0w_t0_d0_9x9_em0j1_Pr0gr4mM!ng}

'''
1  🈳: nop
2  ➕: +
3  ➖: -
4  ❌: *
5  ❓: %
6  ❎: ^
7  👫: &
8  💀: <
9  💯: ==
10 🚀: jmp
11 🈶: jmp if true
12 🈚: jmp if false
13 ⏬: push back
14 🔝: pop top
15 📤: load?
16 📥: store?
17 🆕: malloc (at most 10) [size, malloc(size)]
18 🆓: free
19 📄: read
20 📝: write
21 🔡: write until nullbyte
22 🔢: cout
23 🛑: exit
'''

'''
store [i] [j] [top]
load  top = mem[i][j]
'''

num = [ '😀' , '😁', '😂' , '🤣' , '😜' , '😄' , '😅' , '😆' , '😉' , '😊' , '😍' ]

def push( n ):
    if n <= 10:
        return '⏬' + num[n]
    else:
        return  mul( n // 10 , 10 ) + add( n % 10 , -1 )

def add( a , b , top = False ):
    if b < 0:
        return push( a ) + '➕'
    else:
        return push( b ) + push( a ) + '➕'

def sub( a , b ):
    if b == -1:
        return push( b ) + push( a ) + '➖'
    return push( b ) + push( a ) + '➖'

def mul( a , b ):
    if b == -1:
        return push( a ) + '❌'
    return push( b ) + push( a ) + '❌'

def store( i , j , v ):
    if v == -1:
        return push(j) + push(i) + '📥'
    if type(v) == type('y'):
        v = ord( v )
    return push(v) + push(j) + push(i) + '📥'

def load( i , j ):
    return push(j) + push(i) + '📤'

now = '\0' * 10

def store_str( i , s ):
    p = ''
    for j in range( len( s ) ):
        if now[j] == s[j]:
            continue
        p += store( i , j , s[j] )
    return p

def wri( i ):
    return push( i ) + '📝'

p = ''
p += ( push( 10 ) + '🆕' ) * 4
p += store_str( 3 , '\n\0' )
p += store_str( 2 , '\0' * 10 )
p += store_str( 1 , '1 * 1 = \0\0' ) # 0 4 8
p += store( 0 , 0 , 1 )

loop = len(p)

p += load( 0 , 0 )
p += add( 0x30 , -1 )
p += store( 1 , 0 , -1 )

for i in range( 1 , 10 ):
    p += push( i )
    p += add( 0x30 , -1 )
    p += store( 1 , 4 , -1 )

    p += load( 0 , 0 )
    p += mul( i , -1 )

    p += wri( 1 )
    p += '🔢'
    p += wri( 3 )

p += load( 0 , 0 ) # i
p += add( 1 , -1 )
p += push(0) + push(0) + '📥' # store i + 1

p += load( 0 , 0 ) 
p += push( 9 )
p += '💀' # 9 < i ?
p += push( loop )
p += '🈚' # jump if false
p += '🛑'

print( len( p ) )

o = open( 'payload' , 'w+' )
o.write( p )
o.close()