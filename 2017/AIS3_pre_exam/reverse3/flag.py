#!/usr/bin/env python2

import itertools
from random import randint
from subprocess import Popen, PIPE, STDOUT

#a = range( 256 )

#for a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17 in itertools.product( a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a )

while True:
    a = ''
    for i in range( 17 ):
        a += str( randint( 0 , 256 ) ) + ' '

    p = Popen( ['./rev3_64'] , stdout=PIPE, stdin=PIPE, stderr=STDOUT )
    o = p.communicate( input = a + '\n' )[0]
    if len( o ) > 1:
        print a





