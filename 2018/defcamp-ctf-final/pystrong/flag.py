#!/usr/bin/env python
from pwn import *
import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 
from datetime import datetime
import md5
import numpy as np
import hashlib, binascii
import re

host , port = 'pystrong.dctf18-finals.def.camp' , 13022
#y = remote( host , port )


def square(x):
	try:
	    sum_so_far = 0
	    for _ in range(x):
	        sum_so_far += x
		return sum_so_far
	except Exception(e):
		print e
	finally:
		return sum_so_far

def get_key(x):
	nr = 1337
	try:
		for value in range(1,x):
			nr = nr * value
		return nr
	except Exception(e):
		print e
	finally:
		return nr

def hash(inp):
	return hashlib.sha256(str(inp) + "DCTF2018_BUCHAREST").hexdigest()


'''
dinp[0] 1 ~ 9999
dinp[1] 1 ~ 12
dinp[2] 1 ~ 31
dinp[3] 0 ~ 23
dinp[4] 0 ~ 59
'''
PRIV = 1198041294


p = [ '2018' , '12' , '12' , '0' , '0' , '6' , '7' , '8' , '9' , '0' , '' ]
p[5] = str( square(get_key(p[0])) )
p[7] = str( 950 )
p[8] = str( 950 )
p[9] = str( 730 )
p = ' '.join( _ for _ in p )
print p


data = p.split( ' ' )
dinp = [int(x) for x in data[:5]]

date = datetime(dinp[0], dinp[1], dinp[2], dinp[3], dinp[4]).time()
#print date

try:
    dinp = [int(x) for x in data[:5]]
    if (dinp[0] > 9999 or dinp[0] < 1 or dinp[1] < 1 or dinp[1] > 12 or 
	    dinp[2] < 1 or dinp[2] > 31 or dinp[3] < 0 or dinp[3] > 23 or 
	    dinp[4] < 0 or dinp[4] > 59):
        print 'err 1'

    date = datetime(dinp[0], dinp[1], dinp[2], dinp[3], dinp[4]).time()
    if date:
        print "Tried until #2"
except:
    print "Tried until #3"

if int(data[5]) != square(get_key(data[0])):
    print "Tried until #4"

inp    = (np.array([float(data[6]), float(data[7]), float(data[8]), float(data[9])])*PRIV)%int(data[5])
test   = np.array([float(559), float(661), float(661), float(522)])
solved = np.empty([], dtype=np.float)
#print PRIV * 1337
#print int(data[5])
print 'solved->' , solved

for i in range( len( inp ) ):
    print inp[i] , test[i]
    if inp[i] == test[i]:
        solved = np.append( solved , test[i] )
        
print 'solved->' , solved
			
if len(solved) != 4:
    print "Tried until #5"

#print solved
#print np.sum(solved)
#print hash( ( 1337. + 522. + 661. + 661. ) *PRIV)
if hash(np.sum(solved)*PRIV) != 'fe79a0ee1fc2a52fc9af8592d8c0570a73d9542ec1d4ec2ae6e9d03991cb0459':
    print "Tried until #6"
