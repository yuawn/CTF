#!/usr/bin/env python2
from pwn import *

'''
AIS3{A XOR B XOR A EQUALS B}
'''

a = [ 964600246 , 1376627084 , 1208859320 , 1482862807 , 1326295511 , 1181531558 , 2003814564 ]

c = u32( 'AIS3' ) ^ 964600246

flag = ''

for i in range( 7 ): flag += p32( a[i] ^ c )

log.success( flag )