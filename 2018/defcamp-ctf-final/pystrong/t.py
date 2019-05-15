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

# DCTF{34172171917B931AA0EFD8934401AE5BF3D59A5D3681DBD07C643FA99096CCD9}


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


PRIV = 1198041294

'''
for i in xrange( 0x10000 ):
	if (float( i ) * PRIV) % 1337. == 96:
		print i

exit(0)
'''

host , port = 'pystrong.dctf18-finals.def.camp' , 13022
y = remote( host , port )

#a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y

f = 'reduce(getattr(str,min(dir(str))),map(chr,(int(min(inp))--(len((re,))<<len(())),(len((re,))<<len(dinp))--(len((re,))<<len(inp))--(len((re,re,re,re,re,re,re,re,re,re,re,re,re))),int(min(inp))--(len((re,))<<len((re,re,re)))--(len((re,))<<len((re,re)))--len((re,re,re)),int(min(inp))--(len((re,))<<len(inp)),int(min(inp))--(len((re,))<<len((re,re)))--len((re,)),int(min(inp))--(len((re,))<<len((re,re,re)))--(len((re,))<<len((re,re)))--len((re,re)),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len(())),(len((re,))<<len(dinp))--(len((re,))<<len((re,re)))--(len((re,re,re))),int(min(inp))--(len((re,))<<len(inp)),int(min(inp))--(len((re,))<<len(inp))--(len((re,))<<len((re,re,re)))--len((re,)),int(min(inp))--(len((re,))<<len(inp))--(len((re,))<<len((re,)))--len((re,)),int(min(inp))--(len((re,))<<len(inp))--(len((re,))<<len((re,re))),int(min(inp))--(len((re,))<<len(inp))--(len((re,))<<len((re,))),int(min(inp))--(len((re,))<<len((re,re,re)))--(len((re,))<<len((re,re)))--len((re,re,re)),int(min(inp))--(len((re,))<<len((re,re,re)))--(len((re,))<<len((re,re)))--len((re,re)),int(min(inp))--(len((re,))<<len((re,re)))--(len((re,))<<len((re,)))--len((re,)),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len((re,re,re,re,re,re))),int(min(inp))--(len((re,))<<len(inp)),int(min(inp))--(len((re,))<<len(inp))--(len((re,))<<len((re,re,re)))--len((re,)),(len((re,))<<len(dinp))--(len((re,))<<len((re,re)))--(len((re,re,re))),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len((re,))),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len((re,re,re,re,re,re))),int(min(inp))--(len((re,))<<len(inp))--(len((re,))<<len((re,))),int(min(inp))--(len((re,))<<len((re,re)))--len((re,)),int(min(inp))--(len((re,))<<len(())),int(min(inp))--(len((re,))<<len((re,re))),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len(())),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len((re,))))))'
f = 'reduce(getattr(str,min(dir(str))),map(chr,(int(min(inp))--(len((re,))<<len(())),(len((re,))<<len(dinp))--(len((re,))<<len(inp))--(len((re,re,re,re,re,re,re,re,re,re,re,re,re))),int(min(inp))--(len((re,))<<len((re,re,re)))--(len((re,))<<len((re,re)))--len((re,re,re)),int(min(inp))--(len((re,))<<len(inp)),int(min(inp))--(len((re,))<<len((re,re)))--len((re,)),int(min(inp))--(len((re,))<<len((re,re,re)))--(len((re,))<<len((re,re)))--len((re,re)),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len(())),(len((re,))<<len(dinp))--(len((re,))<<len((re,re)))--(len((re,re,re))),int(min(inp))--(len((re,))<<len((re,re)))--(len((re,))<<len((re,))),int(min(inp))--(len((re,))<<len((re,re,re)))--(len((re,))<<len((re,re))),int(min(inp))--(len((re,))<<len(())),int(min(inp))--(len((re,))<<len((re,re)))--(len((re,))<<len((re,)))--len((re,)),(len((re,))<<len(dinp))--(len((re,))<<len((re,re)))--(len((re,re,re))),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len((re,))),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len((re,re,re,re,re,re))),int(min(inp))--(len((re,))<<len(inp))--(len((re,))<<len((re,))),int(min(inp))--(len((re,))<<len((re,re)))--len((re,)),int(min(inp))--(len((re,))<<len(())),int(min(inp))--(len((re,))<<len((re,re))),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len(())),(len((re,))<<len(dinp))--(len((re,))<<len((re,re,re)))--(len((re,))))))'

p = [ '2018' , '12' , '12' , '0' , '0' , '1337' , '1210' , '950' , '950' , '730' , 'a=str(min(inp))' ]
p[10] = f
p = ' '.join( _ for _ in p )
print p
data = p.split( ' ' )
dinp = [int(x) for x in data[:5]]

date = datetime(dinp[0], dinp[1], dinp[2], dinp[3], dinp[4]).time()

print str( date )

inp    = (np.array([float(data[6]), float(data[7]), float(data[8]), float(data[9])])*PRIV)%int(data[5])
test   = np.array([float(559), float(661), float(661), float(522)])
solved = np.empty([], dtype=np.float)
			 
for i in range(len(inp)):
	if inp[i] == test[i]: 
		solved = np.append(solved, test[i])


def fuck( c ):
	n = ord( c )
	a = n
	t = 0
	while a :
		t += 1
		a /= 2
	print 1<<t
	return 0

y.send( p )

print len(p)

y.interactive()