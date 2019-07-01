#!/usr/bin/env python
import os, subprocess

o = subprocess.check_output( ['ls'] , shell = True )
fs = o.split()

for f in fs:
    s = subprocess.check_output( [ 'cat %s' % f ] , shell = True )
    if 'line number' in s:
        print f

