#!/usr/bin/env python3
from pwn import *

# flag{Hope_you_found_the_problem}

'''

0:   66 66 66 66 90          data16 data16 data16 xchg ax, ax
'''


context.arch = 'amd64'

def ROUND0(a, b, c, d, k, s, t):
    r = f'''
        mov esi, {c}
        add {a}, [rbp+{k*4}]
        xor esi, {d}
        and esi, {b}
        xor esi, {d}
        lea {a}, [{a}+esi+{t}]
        rol {a}, {s}
        add {a}, {b}
    '''.strip()
    return r

def ROUND1(a, b, c, d, k, s, t):
    r = f'''
        mov esi, {d}
        mov edi, {d}
        add {a}, [rbp+{k*4}]
        not esi
        and edi, {b}
        and esi, {c}
        or  esi, edi
        lea {a}, [{a}+esi+{t}]
        rol {a}, {s}
        add {a}, {b}
    '''.strip()
    return r

def ROUND2(a, b, c, d, k, s, t):
    r = f'''
        mov esi, {c}
        add {a}, [rbp+{k*4}]
        xor esi, {d}
        xor esi, {b}
        lea {a}, [{a}+esi+{t}]
        rol {a}, {s}
        add {a}, {b}
    '''.strip()
    return r

def ROUND3(a, b, c, d, k, s, t):
    r = f'''
        mov esi, {d}
        not esi
        add {a}, [rbp+{k*4}]
        or  esi, {b}
        xor esi, {c}
        lea {a}, [{a}+esi+{t}]
        rol {a}, {s}
        add {a}, {b}
    '''.strip()
    return r


_asm = f'''
mov rbp, 0xbabecafe000
mov byte ptr [rbp+50], 0x80
mov qword ptr [rbp+56], 400
mov eax, 0x67452301
mov ebx, 0xEFCDAB89
mov ecx, 0x98BADCFE
mov edx, 0x10325476
{ROUND0('eax', 'ebx', 'ecx', 'edx',  0,  7,  0xD76AA478)}
{ROUND0('edx', 'eax', 'ebx', 'ecx',  1, 12,  0xE8C7B756)}
{ROUND0('ecx', 'edx', 'eax', 'ebx',  2, 17,  0x242070DB)}
{ROUND0('ebx', 'ecx', 'edx', 'eax',  3, 22, -0x3E423112)}
{ROUND0('eax', 'ebx', 'ecx', 'edx',  4,  7, -0x0A83F051)}
{ROUND0('edx', 'eax', 'ebx', 'ecx',  5, 12,  0x4787C62A)}
{ROUND0('ecx', 'edx', 'eax', 'ebx',  6, 17, -0x57CFB9ED)}
{ROUND0('ebx', 'ecx', 'edx', 'eax',  7, 22, -0x02B96AFF)}
{ROUND0('eax', 'ebx', 'ecx', 'edx',  8,  7,  0x698098D8)}
{ROUND0('edx', 'eax', 'ebx', 'ecx',  9, 12, -0x74BB0851)}
{ROUND0('ecx', 'edx', 'eax', 'ebx', 10, 17, -0x0000A44F)}
{ROUND0('ebx', 'ecx', 'edx', 'eax', 11, 22, -0x76A32842)}
{ROUND0('eax', 'ebx', 'ecx', 'edx', 12,  7,  0x6B901122)}
{ROUND0('edx', 'eax', 'ebx', 'ecx', 13, 12, -0x02678E6D)}
{ROUND0('ecx', 'edx', 'eax', 'ebx', 14, 17, -0x5986BC72)}
{ROUND0('ebx', 'ecx', 'edx', 'eax', 15, 22,  0x49B40821)}
{ROUND1('eax', 'ebx', 'ecx', 'edx',  1,  5, -0x09E1DA9E)}
{ROUND1('edx', 'eax', 'ebx', 'ecx',  6,  9, -0x3FBF4CC0)}
{ROUND1('ecx', 'edx', 'eax', 'ebx', 11, 14,  0x265E5A51)}
{ROUND1('ebx', 'ecx', 'edx', 'eax',  0, 20, -0x16493856)}
{ROUND1('eax', 'ebx', 'ecx', 'edx',  5,  5, -0x29D0EFA3)}
{ROUND1('edx', 'eax', 'ebx', 'ecx', 10,  9,  0x02441453)}
{ROUND1('ecx', 'edx', 'eax', 'ebx', 15, 14, -0x275E197F)}
{ROUND1('ebx', 'ecx', 'edx', 'eax',  4, 20, -0x182C0438)}
{ROUND1('eax', 'ebx', 'ecx', 'edx',  9,  5,  0x21E1CDE6)}
{ROUND1('edx', 'eax', 'ebx', 'ecx', 14,  9, -0x3CC8F82A)}
{ROUND1('ecx', 'edx', 'eax', 'ebx',  3, 14, -0x0B2AF279)}
{ROUND1('ebx', 'ecx', 'edx', 'eax',  8, 20,  0x455A14ED)}
{ROUND1('eax', 'ebx', 'ecx', 'edx', 13,  5, -0x561C16FB)}
{ROUND1('edx', 'eax', 'ebx', 'ecx',  2,  9, -0x03105C08)}
{ROUND1('ecx', 'edx', 'eax', 'ebx',  7, 14,  0x676F02D9)}
{ROUND1('ebx', 'ecx', 'edx', 'eax', 12, 20, -0x72D5B376)}
{ROUND2('eax', 'ebx', 'ecx', 'edx',  5,  4, -0x0005C6BE)}
{ROUND2('edx', 'eax', 'ebx', 'ecx',  8, 11, -0x788E097F)}
{ROUND2('ecx', 'edx', 'eax', 'ebx', 11, 16,  0x6D9D6122)}
{ROUND2('ebx', 'ecx', 'edx', 'eax', 14, 23, -0x021AC7F4)}
{ROUND2('eax', 'ebx', 'ecx', 'edx',  1,  4, -0x5B4115BC)}
{ROUND2('edx', 'eax', 'ebx', 'ecx',  4, 11,  0x4BDECFA9)}
{ROUND2('ecx', 'edx', 'eax', 'ebx',  7, 16, -0x0944B4A0)}
{ROUND2('ebx', 'ecx', 'edx', 'eax', 10, 23, -0x41404390)}
{ROUND2('eax', 'ebx', 'ecx', 'edx', 13,  4,  0x289B7EC6)}
{ROUND2('edx', 'eax', 'ebx', 'ecx',  0, 11, -0x155ED806)}
{ROUND2('ecx', 'edx', 'eax', 'ebx',  3, 16, -0x2B10CF7B)}
{ROUND2('ebx', 'ecx', 'edx', 'eax',  6, 23,  0x04881D05)}
{ROUND2('eax', 'ebx', 'ecx', 'edx',  9,  4, -0x262B2FC7)}
{ROUND2('edx', 'eax', 'ebx', 'ecx', 12, 11, -0x1924661B)}
{ROUND2('ecx', 'edx', 'eax', 'ebx', 15, 16,  0x1FA27CF8)}
{ROUND2('ebx', 'ecx', 'edx', 'eax',  2, 23, -0x3B53A99B)}
{ROUND3('eax', 'ebx', 'ecx', 'edx',  0,  6, -0x0BD6DDBC)}
{ROUND3('edx', 'eax', 'ebx', 'ecx',  7, 10,  0x432AFF97)}
{ROUND3('ecx', 'edx', 'eax', 'ebx', 14, 15, -0x546BDC59)}
{ROUND3('ebx', 'ecx', 'edx', 'eax',  5, 21, -0x036C5FC7)}
{ROUND3('eax', 'ebx', 'ecx', 'edx', 12,  6,  0x655B59C3)}
{ROUND3('edx', 'eax', 'ebx', 'ecx',  3, 10, -0x70F3336E)}
{ROUND3('ecx', 'edx', 'eax', 'ebx', 10, 15, -0x00100B83)}
{ROUND3('ebx', 'ecx', 'edx', 'eax',  1, 21, -0x7A7BA22F)}
{ROUND3('eax', 'ebx', 'ecx', 'edx',  8,  6,  0x6FA87E4F)}
{ROUND3('edx', 'eax', 'ebx', 'ecx', 15, 10, -0x01D31920)}
{ROUND3('ecx', 'edx', 'eax', 'ebx',  6, 15, -0x5CFEBCEC)}
{ROUND3('ebx', 'ecx', 'edx', 'eax', 13, 21,  0x4E0811A1)}
{ROUND3('eax', 'ebx', 'ecx', 'edx',  4,  6, -0x08AC817E)}
{ROUND3('edx', 'eax', 'ebx', 'ecx', 11, 10, -0x42C50DCB)}
{ROUND3('ecx', 'edx', 'eax', 'ebx',  2, 15,  0x2AD7D2BB)}
{ROUND3('ebx', 'ecx', 'edx', 'eax',  9, 21, -0x14792C6F)}
add eax, 0x67452301
add ebx, 0xEFCDAB89
add ecx, 0x98BADCFE
add edx, 0x10325476
mov [rbp+0x800], eax
mov [rbp+0x804], ebx
mov [rbp+0x808], ecx
mov [rbp+0x80c], edx
'''.strip()

print(_asm)
print()

sc = asm(_asm)
sc = b'\x66' * (0x2000 - len(sc)) + sc
ins_cnt = len(_asm.split('\n'))
print(f'ins_cnt = {ins_cnt}')
print(f'sc len = {len(sc)}')
print(f'avg len per ins = {len(sc)/float(ins_cnt)}')

y = remote('111.186.59.29', 10086)

y.send(sc)

y.interactive()
