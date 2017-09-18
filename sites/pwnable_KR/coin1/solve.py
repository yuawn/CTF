from pwn import *
# need to connect inside pwnable server internet
#flag -> b1NaRy_S34rch1nG_1s_3asy_p3asy


host = '0.0.0.0'
port = 9007

y = remote(host , port)

y.recvuntil('- Ready? starting in 3 sec... -\n')

while True:
    con = y.recvline()
    log.info(con)
    toc = y.recvline()
    log.critical(toc)
    if toc.find('=') < 0:
        flag = y.recvline()
        log.success(flag)
        break
    n = int(toc[toc.find('=')+1:toc.find(' ')])
    c = int(toc[toc.find('C=')+2:-1])
    l = 0
    r = n - 1
    for i in range(c):
        mid = (l + r) / 2
        payload = ' '.join(str(j) for j in range(l,mid))
        y.sendline( payload )
        res = int(y.recvline()[:-1])
        log.success("{}~{} weight {}".format(l , mid , res))
        if res < (mid - l) * 10 :
            r = mid + 1
        else:
            l = mid
    y.sendline(str(l))

#y.interactive()
