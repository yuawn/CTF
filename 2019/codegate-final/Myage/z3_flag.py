#!/usr/bin/env python
from z3 import *
import re

#s = Solver()

#a = BitVec("num1",32)
#b = BitVec("num2",32)

a = 0
b = 1

ans = 0

ar = '''
  v3 = 12;
  v4 = 17;
  v5 = 4;
  v6 = 18;
  v7 = 10;
  v8 = 18;
  v9 = 4;
  v10 = 5;
  v11 = 19;
  v12 = 3;
  v13 = 17;
  v14 = 15;
  v15 = 9;
  v16 = 1;
  v17 = 3;
  v18 = 1;
  v19 = 15;
  v20 = 19;
  v21 = 20;
  v22 = 7;
'''
ar = map( int , re.findall( '= ([0-9]+);' , ar ) )
print ar

def check( a , b ):
    ans = 0
    b = 0

    for v in ar:
        if v == 1:
            b += 1
            ans += 901131
        elif v == 2:
            b -= 1
            ans += -972713
        elif v == 3:
            b -= 1
            ans += 231467
        elif v == 4:
            b -= 1
            ans += 432027
        elif v == 5:
            b -= 1
            ans += 331917
        elif v == 6:
            b += 1
            ans += 819291
        elif v == 7:
            b += 1
            ans += 333057
        elif v == 8:
            b -= 1
            ans += - 825875
        elif v == 9:
            b += 1
            ans += - 310801
        elif v == 10:
            b -= 1
            ans += - 698799
        elif v == 11:
            b += 1
            ans += - 197607
        elif v == 12:
            b -= 1
            ans += 923326
        elif v == 13:
            b += 1
            ans += - 876272
        elif v == 14:
            b -= 1
            ans += - 749297
        elif v == 15:
            b += 1
            ans += - 443892
        elif v == 16:
            b += 1
            ans +=  - 984718
        elif v == 17:
            b -= 1
            ans += 123755
        elif v == 18:
            b += 1
            ans += - 854261
        elif v == 19:
            b -= 1
            ans += 833576
        elif v == 20:
            b += 1
            ans += 1015081

    return a , b , ans

a , b , sm = check( 0 , 0 )
print a , b , sm

print ( 0x8F79AFC4 - sm ) / b

'''
for i in xrange( 0x100000000 ):
    if check( 0 , i ) == 0x8F79AFC4:
        print i
'''

#s.add( ans == -1887850556 )
#print( s.check() )
#print s.model()[a].as_long()
#print s.model()[b].as_long()