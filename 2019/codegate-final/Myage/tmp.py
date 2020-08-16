#!/usr/bin/env python
from ctypes import *
from z3 import *
ans , a , b = 0 , 0 , 0


def sub_4008B4():
    global ans , a , b
    a += 1
    b += 1
    ans += 990774

def sub_4008DC():
    global ans , a , b
    a += 1
    b -= 1
    ans += 830394

def sub_400904():
    global ans , a , b
    a += 1
    b += 1
    ans -= 766285

def sub_40092C():
    global ans , a , b
    a += 1
    b -= 1
    ans += 431312

def sub_400954():
    global ans , a , b
    a += 1
    b += 1
    ans -= 361043

def sub_40097C():
    global ans , a , b
    a += 1
    b += 1
    ans -= 889022

def sub_4009A4():
    global ans , a , b
    a += 1
    b -= 1
    ans -= 858812

def sub_4009CC():
    global ans , a , b
    a += 1
    b += 1
    ans -= 379113

def sub_4009F4():
    global ans , a , b
    a += 1
    b -= 1
    ans += 645262

def sub_400A1C():
    global ans , a , b
    a += 1
    b += 1
    ans -= 825172

def sub_400A44():
    global ans , a , b
    a += 1
    b -= 1
    ans -= 692799

def sub_400A6C():
    global ans , a , b
    a += 1
    b += 1
    ans -= 348226

def sub_400A94():
    global ans , a , b
    a += 1
    b -= 1
    ans -= 366485

def sub_400ABC():
    global ans , a , b
    a += 1
    b += 1
    ans += 968595

def sub_400AE4():
    global ans , a , b
    a += 1
    b += 1
    ans += 725726

def sub_400B0C():
    global ans , a , b
    a += 1
    b -= 1
    ans += 80148

def sub_400B34():
    global ans , a , b
    a += 1
    b -= 1
    ans += 844528

def sub_400B5C():
    global ans , a , b
    a += 1
    b -= 1
    ans += 145334

def sub_400B84():
    global ans , a , b
    a += 1
    b -= 1
    ans -= 580196

def sub_400BAC():
    global ans , a , b
    a += 1
    b += 1
    ans += 784875

v = [11, 5, 5, 13, 13, 3, 9, 18, 13, 10, 14, 14, 13, 1, 11, 3, 14, 18, 6, 12]

for i in v:

    if i == 1:
        sub_400BAC()
    
    if i == 2:
        sub_400B84()
    
    if i == 3:
        sub_400B5C()
    
    if i == 4:
        sub_400B34()
    
    if i == 5:
        sub_400B0C()
    
    if i == 6:
        sub_400AE4()
    
    if i == 7:
        sub_400ABC()
    
    if i == 8:
        sub_400A94()
    
    if i == 9:
        sub_400A6C()
    
    if i == 10:
        sub_400A44()
    
    if i == 11:
        sub_400A1C()
    
    if i == 12:
        sub_4009F4()
    
    if i == 13:
        sub_4009CC()
    
    if i == 14:
        sub_4009A4()
    
    if i == 15:
        sub_40097C()
    
    if i == 16:
        sub_400954()
    
    if i == 17:
        sub_40092C()
    
    if i == 18:
        sub_400904()
    
    if i == 19:
        sub_4008DC()
    
    if i == 20:
        sub_4008B4()
    
final = c_int( 0x2b75781a ).value
print a , b , ans
print ( final - ans ) % 20

n1 = BitVec("num1",32)
n2 = BitVec("num2",32)

s = Solver()

s.add( n1 * a + n2 * b + ans == final )

print s.check()

print s.model()[n1].as_long()
print s.model()[n2].as_long()

