#!/usr/bin/env python
from pwn import *
import re


bcd = {
    ' ' : 0x00,     '~' : 0x10,     '-' : 0x20, '&' : 0x30,
    '1' : 0x01,     '/' : 0x11,     'J' : 0x21, 'A' : 0x31,
    '2' : 0x02,     'S' : 0x12,     'K' : 0x22, 'B' : 0x32,
    '3' : 0x03,     'T' : 0x13,     'L' : 0x23, 'C' : 0x33 ,
    '4' : 0x04,     'U' : 0x14,     'M' : 0x24, 'D' : 0x34,
    '5' : 0x05,     'V' : 0x15,     'N' : 0x25, 'E' : 0x35 ,
    '6' : 0x06,     'W' : 0x16,     'O' : 0x26, 'F' : 0x36 ,
    '7' : 0x07,     'X' : 0x17,     'P' : 0x27, 'G' : 0x37,
    '8' : 0x08,     'Y' : 0x18,     'Q' : 0x28, 'H' : 0x38,
    '9' : 0x09,     'Z' : 0x19,     'R' : 0x29, 'I' : 0x39 ,
    '0' : 0x0a,     '~' : 0x1a,     '!' : 0x2a, '?' : 0x3a ,
    '#' : 0x0b,     ',' : 0x1b,     '$' : 0x2b, '.' : 0x3b,
    '@' : 0x0c,     '%' : 0x1c,     '*' : 0x2c, '~' : 0x3c,
    ':' : 0x0d,     '=' : 0x1d,     ')' : 0x2d, '(' : 0x3d,
    '>' : 0x0e,     '\'': 0x1e,     ';' : 0x2e, '<' : 0x3e,
    '~' : 0x0f,     '"' : 0x1f,     '~' : 0x2f, '~' : 0x3f,
}

def chunk_str(s, chunksize):
	return [ s[i:i+chunksize] for i in range(0, len(s), chunksize) ]

op = ',008015,022029,036043,050054,055062,063065,069080/333/M0792502F1.065HELLO WORLD'
#op = ',008015,022029,036043,050054,055062,063065,069080/333/M9122502F1.065'
op = ',008015,022029,036043,050080,084085,092093,095099W080080                       /333/M9122502F1.065'
#op = ',008022W080080       ,029036,043050,057064,068069,076077,079083/333/M9122502F1.065'
#op = '/333/M0792502F1.065                                                 HELLO WORLD'
#op += '/M0792502F1.065'
#op = ',008015,022029,036043,050054,055062,063070,074085/333/M0842502F1NNNNN.070HELLO WORLD'


flag = 'OOO7777777'
for i , c in enumerate( re.findall( '.' , flag ) , start = 900 ):
    print( 'd %d %s' % ( i , oct( bcd[c] )[1:].rjust( 3 , '0' ) ) )


p = 0
i = 0
for c in re.findall( '.' , op ):
    i += 1
    t = bcd[c]
    if c in [',','/','M','F','.','V','W']:
        print( 'd %d %s' % ( i , oct( t | ( 1 << 6 ) )[1:].rjust( 3 , '0' ) ) )
    else:
        print( 'd %d %s' % ( i , oct( t )[1:].rjust( 3 , '0' ) ) )
    p = 0


print 'att lpt /dev/stdout'

op = ',008300W200200'

bits = ''

for c in re.findall( '.' , op ):
    if c in [',','/','M','F','.']:
        bits += bin( bcd[c] | (1 << 6) )[2:].rjust( 7 , '0' )
    else:
        bits += bin( bcd[c] )[2:].rjust( 7 , '0' )

bits = bits.ljust( (( len( bits ) / 8 ) + 1) * 8 , '0' )

print len(bits)
print bits

print ''.join( '\\x' + hex( int( i , 2 ) )[2:].rjust( 2 , '0' ) for i in re.findall( '........' , bits ) )
