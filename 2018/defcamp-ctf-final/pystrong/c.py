#!/usr/bin/env python
import re

def nu( n ):
    if not n:
        return 'len(())'
    elif n == 4:
        return 'len(inp)'
    elif n == 5:
        return 'len(dinp)'
    elif n == 7:
        return 'len(dinp)--len((re,re))'
    p = 'len(('
    for i in xrange( n ):
        p += 're,'
    if p[-1] == ',' and n > 1:
        p = p[:-1]
    return p + '))'


def gg2( c ):
    n = ord( c )
    if n == 32:
        return 'len((re,))<<len(dinp)'
    t = 0
    t2 = 0
    a = n
    while a:
        if a / 2 == 0:
            break
        a /= 2
        t += 1

    b = n - (1 << t)

    while b:
        if b / 2 == 0:
            break
        b /= 2
        t2 += 1
    p = '(%s<<%s)--(%s<<%s)--(%s)' % ( nu(1) , nu(t) , nu(1) , nu(t2) , nu(n - ( (1<<t) + (1<<t2) )) )
    return p



def gg( c ):
    if ord(c) < 96:
        return gg2( c )
    n = ord( c ) - 96
    print n
    t = 0
    t2 = 0
    a = n
    while a:
        if a / 2 == 0:
            break
        a /= 2
        t += 1

    b = n - (1 << t)

    while b:
        if b / 2 == 0:
            break
        b /= 2
        t2 += 1

    
    print n , t , t2 , (1<<t) , (1<<t2) ,  n - ( (1<<t) + (1<<t2) )

    pp = 0
    for i in xrange( 10 ):
        if 1 << i == n:
            return 'int(min(inp))--(len((re,))<<%s)' % nu( i )

    if n - ( (1<<t) + (1<<t2) ) <= 0:
        if t2 == 0:
            p = 'int(min(inp))--(%s<<%s)--%s' % ( nu(1) , nu(t) , nu(1) )
        else:
            p = 'int(min(inp))--(%s<<%s)--(%s<<%s)' % ( nu(1) , nu(t) , nu(1) , nu(t2) )
    else:
        p = 'int(min(inp))--(%s<<%s)--(%s<<%s)--%s' % ( nu(1) , nu(t) , nu(1) , nu(t2) , nu(n - ( (1<<t) + (1<<t2) )) )
    print chr( eval( p ) ) , p
    #print len(p)
    return p



inp = [661,661,522,96]
dinp = [1,2,3,4,5]
#o = gg( 'p' )
#print o
#print eval( o )

#for i in xrange( 0x61 , 0x7f ):
#    print len( gg( chr( i ) ) )

# reduce(getattr(str,min(dir(str))),map(chr,(0x61,0x61)))


p = "a=open('flag').read()"
#p = "a=open('pystrong.py').read()"
#p = "a=str(__import__('os').listdir()))"
#p = "import os;a=str(os.listdir('.'))"

p = map( gg , p )
p = '(%s)' % ( ','.join( p ) )
print p
print len(p)
#print map( chr , eval( p ) )

#o = gg( 'a' )
#print o
#print eval( o )

f = 'reduce(getattr(str,min(dir(str))),map(chr,%s))' % p

print '-' * 0x70
print f
print len( f )
print eval( f )
