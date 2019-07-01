#!/usr/bin/env python
import os, subprocess

o = subprocess.check_output( ['find ../volume-0 | grep \'\\.pe\''] , shell = True )

pes = o.split()

for pe in pes:
    filename = subprocess.check_output( [ 'strings %s | grep \'google\'' % pe ] , shell = True ).split( '/' )[-1]
    print pe
    print filename
    os.system( 'cp %s %s' % ( pe , filename ) )