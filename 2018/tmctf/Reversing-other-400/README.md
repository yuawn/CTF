# Trend Micro CTF - Reversing other 400
* TMCTF{SlytherinPastTheReverser}
* Stupid way :P
* Create a function `verify_flag` which has same `verify_flag.__code__.co_consts` , `verify_flag.__code__.co_varnames` , `verify_flag.__code__.co_names` and the same length of `verify_flag.__code__.co_code` in `fake.py`.
```python
#!/usr/bin/env python


def verify_flag( inval ):
    inval
    c = 0
    l = 'TMCTF{'
    s = '}'
    sdl = 1
    x = -1
    ROFL = 7
    KYRYK = 5
    QQRTQ = 'ReadEaring'
    KYRYJ = 'adEa'
    QQRTW = 'dHer'
    KYRYH = 24
    QQRTE = 9
    KYRYG = 'h'
    QQRTR = 255
    KYRYF = 8
    QQRTY = 32
    i = ''
    j = 'R) +6'
    ary = 'l1:C('
    c = ' RP%A'
    c = 236
    c = 108
    c = 102
    c = 169
    c = 93
    c = ' L30Z'
    c = 'X2'
    c = ' j36~'
    c = 's2'
    c = ' M2S+'
    c = 'X3'
    c = '4e\x9c{E'
    c = 'S3'
    c = '6!2$D'
    c = 'X4'
    c = ']PaSs'
    c = 'S4'
    c = 10
    c,c,c,c,c = 236, 108, 102, 169, 93
    c = True
    c = ''.title()
    len(c)
    c = False
    c = ''.startswith( '' )
    c = ''.endswith( '' )
    c = ''.replace( 'h' , '' )
    c = ''.split()
    c = ''.rsplit()
    AssertionError
    c = map( ord , '' )
    c = sum( [] )
    c = chr( 10 )
    c = list( '' )
    c = reversed( '' )
    c = xrange( 10 )
    c = ''.join( [] )
    ValueError
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    c = tuple()
    len(c)
    len(c)
    return

print verify_flag.__code__.co_consts
print verify_flag.__code__.co_varnames
print verify_flag.__code__.co_names
print len( verify_flag.__code__.co_code )

o = open( 'bc_fake' , 'w+' )
o.write( verify_flag.__code__.co_code )
o.close()
```
* Compile the `fake.py`, got `fake.pyc`.
* Overwrite the `verify_flag.__code__.co_code` in fake.pyc with the one of `parseltongue.py`, got `new.pyc`.
* Use `uncompyle2` to decompile `new.pyc`:
```python
#Embedded file name: fake.py


def verify_flag(inval):
    try:
        inval + 0
    except:
        for c in inval:
            c += c
        else:
            del c

    else:
        while True:
            inval += inval
        else:
            del inval

    try:
        title
    except:
        pass

    if len(inval) == 0 or False:
        return False
    if not inval.startswith('TMCTF{'):
        return False
    if not inval.endswith('}'):
        return False
        inval = inval.replace('TMCTF{')
    else:
        l = len(inval)
        inval = inval.split('TMCTF{', 1)[-1].rsplit('}', 1)[0]
        try:
            assert len(inval) + 7 == l
        except:
            return False

        10
    if inval == 'ReadEaring'.replace('adEa', 'dHer'):
        return False
    inval = map(ord, inval)
    l = len(inval)
    if l != 24:
        return False
    s = sum(inval)
    if s % l != 9:
        return False
    sdl = s / l
    if chr(sdl) != 'h':
        return False
    inval = [ x ^ sdl for x in inval ]
    ROFL = list(reversed(inval))
    KYRYK = [0] * 5
    QQRTQ = [0] * 5
    KYRYJ = [0] * 5
    QQRTW = [0] * 5
    KYRYH = [0] * 5
    QQRTE = [0] * 5
    KYRYG = [0] * 5
    QQRTR = [0] * 5
    KYRYF = [0] * 5
    QQRTY = [0] * 5
    for i in xrange(len(KYRYK)):
        for j in xrange(len(QQRTQ) - 1):
            KYRYK[i] ^= inval[i + j]
            if QQRTQ[i] + inval[i + j] > 255:
                return False
            QQRTQ[i] += inval[i + j]
            KYRYJ[i] ^= inval[i * j]
            if QQRTW[i] + inval[i * j] > 255:
                return False
            QQRTW[i] += inval[i * j]
            KYRYH[i] ^= inval[8 + i * j]
            if QQRTE[i] + inval[8 + i * j] > 255:
                return False
            QQRTE[i] += inval[8 + i * j]
            KYRYG[i] ^= ROFL[8 + i * j]
            if QQRTR[i] + ROFL[8 + i * j] > 255:
                return False
            QQRTR[i] += ROFL[8 + i * j]
            KYRYF[i] ^= ROFL[i + j]
            if QQRTY[i] + ROFL[i + j] > 255:
                return False
            QQRTY[i] += ROFL[i + j]

        KYRYK[i] += 32
        KYRYJ[i] += 32
        KYRYH[i] += 32
        KYRYG[i] += 32
        KYRYF[i] += 32
        QQRTE[i] += 8
        QQRTY[i] += 1

    for ary in [KYRYK,
     KYRYJ,
     KYRYH,
     KYRYG,
     KYRYF,
     QQRTW,
     QQRTE,
     QQRTR,
     QQRTY]:
        for x in ary:
            if x > 255:
                return False

    if ''.join(map(chr, KYRYK)) != 'R) +6':
        return False
    try:
        if ''.join(map(chr, QQRTQ)) != 'l1:C(':
            return False
    except ValueError:
        return False

    if ''.join(map(chr, KYRYJ)) != ' RP%A':
        return False
    if tuple(QQRTW) != (236, 108, 102, 169, 93):
        return False
    if ''.join(map(chr, KYRYH)) != ' L30Z':
        print 'X2',
        print
        return False
    if ''.join(map(chr, QQRTE)) != ' j36~':
        print 's2'
        return False
    if ''.join(map(chr, KYRYG)) != ' M2S+':
        print 'X3'
        return False
    if ''.join(map(chr, QQRTR)) != '4e\x9c{E':
        print 'S3',
        print
        return False
    if ''.join(map(chr, KYRYF)) != '6!2$D':
        print 'X4'
        return False
    if ''.join(map(chr, QQRTY)) != ']PaSs':
        print 'S4'
        return False
    return True


print verify_flag.__code__.co_consts
print verify_flag.__code__.co_varnames
print verify_flag.__code__.co_names
print len(verify_flag.__code__.co_code)
o = open('bc_fake', 'w+')
o.write(verify_flag.__code__.co_code)
o.close()
#+++ okay decompyling ./new.pyc
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed#
```
* Use `z3` to solve it:
```python
#!/usr/bin/env python
from z3 import *

# TMCTF{SlytherinPastTheReverser}

s=[ BitVec('vec%d' % i , 8) for i in range(24) ]
rs = list( reversed( s ) )
solver = Solver()

def m32( i ):
    return ord( i ) - 32

def m8( i ):
    return ord( i ) - 8

def m1( i ):
    return ord( i ) - 1


v0 = map( m32 , 'R) +6' )
v1 = map( ord , 'l1:C(' )
v2 = map( m32 , ' RP%A' )
v3 = [ 236, 108, 102, 169, 93 ]
v4 = map( m32 , ' L30Z' )
v5 = map( m8 , ' j36~' )
v6 = map( m32 , ' M2S+' )
v7 = map( ord , '4e\x9c{E' )
v8 = map( m32 , '6!2$D' )
v9 = map( m1 , ']PaSs' )

solver.add( s[0] != 187 )
solver.add( s[0+0] ^ s[0+1] ^ s[0+2] ^ s[0+3] == v0[0] )
solver.add( s[0+0] + s[0+1] + s[0+2] + s[0+3] == v1[0] )
solver.add( s[0*0] ^ s[0*1] ^ s[0*2] ^ s[0*3] == v2[0] )
solver.add( s[0*0] + s[0*1] + s[0*2] + s[0*3] == v3[0] )
solver.add( s[8+0*0] ^ s[8+0*1] ^ s[8+0*2] ^ s[8+0*3] == v4[0] )
solver.add( s[8+0*0] + s[8+0*1] + s[8+0*2] + s[8+0*3] == v5[0] )
solver.add( rs[8+0*0] ^ rs[8+0*1] ^ rs[8+0*2] ^ rs[8+0*3] == v6[0] )
solver.add( rs[8+0*0] + rs[8+0*1] + rs[8+0*2] + rs[8+0*3] == v7[0] )
solver.add( rs[0+0] ^ rs[0+1] ^ rs[0+2] ^ rs[0+3] == v8[0] )
solver.add( rs[0+0] + rs[0+1] + rs[0+2] + rs[0+3] == v9[0] )
solver.add( s[1+0] ^ s[1+1] ^ s[1+2] ^ s[1+3] == v0[1] )
solver.add( s[1+0] + s[1+1] + s[1+2] + s[1+3] == v1[1] )
solver.add( s[1*0] ^ s[1*1] ^ s[1*2] ^ s[1*3] == v2[1] )
solver.add( s[1*0] + s[1*1] + s[1*2] + s[1*3] == v3[1] )
solver.add( s[8+1*0] ^ s[8+1*1] ^ s[8+1*2] ^ s[8+1*3] == v4[1] )
solver.add( s[8+1*0] + s[8+1*1] + s[8+1*2] + s[8+1*3] == v5[1] )
solver.add( rs[8+1*0] ^ rs[8+1*1] ^ rs[8+1*2] ^ rs[8+1*3] == v6[1] )
solver.add( rs[8+1*0] + rs[8+1*1] + rs[8+1*2] + rs[8+1*3] == v7[1] )
solver.add( rs[1+0] ^ rs[1+1] ^ rs[1+2] ^ rs[1+3] == v8[1] )
solver.add( rs[1+0] + rs[1+1] + rs[1+2] + rs[1+3] == v9[1] )
solver.add( s[2+0] ^ s[2+1] ^ s[2+2] ^ s[2+3] == v0[2] )
solver.add( s[2+0] + s[2+1] + s[2+2] + s[2+3] == v1[2] )
solver.add( s[2*0] ^ s[2*1] ^ s[2*2] ^ s[2*3] == v2[2] )
solver.add( s[2*0] + s[2*1] + s[2*2] + s[2*3] == v3[2] )
solver.add( s[8+2*0] ^ s[8+2*1] ^ s[8+2*2] ^ s[8+2*3] == v4[2] )
solver.add( s[8+2*0] + s[8+2*1] + s[8+2*2] + s[8+2*3] == v5[2] )
solver.add( rs[8+2*0] ^ rs[8+2*1] ^ rs[8+2*2] ^ rs[8+2*3] == v6[2] )
solver.add( rs[8+2*0] + rs[8+2*1] + rs[8+2*2] + rs[8+2*3] == v7[2] )
solver.add( rs[2+0] ^ rs[2+1] ^ rs[2+2] ^ rs[2+3] == v8[2] )
solver.add( rs[2+0] + rs[2+1] + rs[2+2] + rs[2+3] == v9[2] )
solver.add( s[3+0] ^ s[3+1] ^ s[3+2] ^ s[3+3] == v0[3] )
solver.add( s[3+0] + s[3+1] + s[3+2] + s[3+3] == v1[3] )
solver.add( s[3*0] ^ s[3*1] ^ s[3*2] ^ s[3*3] == v2[3] )
solver.add( s[3*0] + s[3*1] + s[3*2] + s[3*3] == v3[3] )
solver.add( s[8+3*0] ^ s[8+3*1] ^ s[8+3*2] ^ s[8+3*3] == v4[3] )
solver.add( s[8+3*0] + s[8+3*1] + s[8+3*2] + s[8+3*3] == v5[3] )
solver.add( rs[8+3*0] ^ rs[8+3*1] ^ rs[8+3*2] ^ rs[8+3*3] == v6[3] )
solver.add( rs[8+3*0] + rs[8+3*1] + rs[8+3*2] + rs[8+3*3] == v7[3] )
solver.add( rs[3+0] ^ rs[3+1] ^ rs[3+2] ^ rs[3+3] == v8[3] )
solver.add( rs[3+0] + rs[3+1] + rs[3+2] + rs[3+3] == v9[3] )
solver.add( s[4+0] ^ s[4+1] ^ s[4+2] ^ s[4+3] == v0[4] )
solver.add( s[4+0] + s[4+1] + s[4+2] + s[4+3] == v1[4] )
solver.add( s[4*0] ^ s[4*1] ^ s[4*2] ^ s[4*3] == v2[4] )
solver.add( s[4*0] + s[4*1] + s[4*2] + s[4*3] == v3[4] )
solver.add( s[8+4*0] ^ s[8+4*1] ^ s[8+4*2] ^ s[8+4*3] == v4[4] )
solver.add( s[8+4*0] + s[8+4*1] + s[8+4*2] + s[8+4*3] == v5[4] )
solver.add( rs[8+4*0] ^ rs[8+4*1] ^ rs[8+4*2] ^ rs[8+4*3] == v6[4] )
solver.add( rs[8+4*0] + rs[8+4*1] + rs[8+4*2] + rs[8+4*3] == v7[4] )
solver.add( rs[4+0] ^ rs[4+1] ^ rs[4+2] ^ rs[4+3] == v8[4] )
solver.add( rs[4+0] + rs[4+1] + rs[4+2] + rs[4+3] == v9[4] )

print solver.check()
ans = solver.model()
flag = ''.join( chr( ans[ _ ].as_long() ^ ord( 'h' ) ) for _ in s )
print 'TMCTF{%s}' % flag
```