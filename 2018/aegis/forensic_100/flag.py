#!/usr/bin/env python
from pwn import *

# AEGIS{023def88ws5dsu88d85d5dfgf5}

# gf5}u88d85d5dfef88ws5dsAEGIS{023d

'''
0x29436 \x81 g
0x2949c A f
0x294de Y 5
0x2954a n }

0x2b836 y u
0x2b89c E 8
0x2b8de S 8
0x2b94a ` d
0x2b986 \x9e 8
0x2b9bf _ 5
0x2ba28 _ d
0x2ba64 m 5
0x2bab5 q d
0x2bad6 W f

0x2bb36 q e
0x2bb9c E f
0x2bbde V 8
0x2bc4a X 8
0x2bcbf b w
0x2bd28 ^ s
0x2bd64 q 5
0x2bdb5 w d
0x2bdd6 R s

0x2c736 x A
0x2c79c J E
0x2c7de \ G
0x2c84a \ I
0x2c886 Y S
0x2c8bf c {
0x2c928 g 0
0x2c964 o 2
0x2c9b5 \x98 3
0x2c9d6 U d
'''

a , b = open( './Lenna_left.bmp' ).read() , open( './Lenna_right.bmp' ).read()

flag = ''

for i , j in zip( a , b ):
    if i != j:
        flag += j
        print i , j

print flag