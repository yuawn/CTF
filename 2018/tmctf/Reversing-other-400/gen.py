#!/usr/bin/env python
from z3 import *
import py_compile

a = open( './bc_fake' ).read()
b = open( './bc_origin' ).read()

py_compile.compile("fake.py")

f = open( 'fake.pyc' ).read()
o = open( 'new.pyc' , 'w+' )
o.write( f[ : f.find( a ) ] + b + f[ f.find( a ) + len( a ) : ] )
o.close()

