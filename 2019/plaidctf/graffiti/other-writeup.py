# from https://pastebin.com/Z4tpppkJ
import scapy
from scapy.all import *
import struct
import sys
 
sys.path.append('.')
import q3huff
 
FRAGMENTED = 1 << 31
CL_DECODE_START = 4
SV_DECODE_START = 12
MAX_RELIABLE_COMMANDS = 64
MAX_STRING_CHARS = 1024
 
reliableCommands = [bytearray([0, 0]) for i in range(MAX_RELIABLE_COMMANDS)]
 
def decompress(data):
    r = q3huff.Reader(data)
    res = []
    while True:
        b = r.read_byte()
        if b == -1:
            break
        res.append(b)
    return bytes(res)
 
def dec_start(data):
    r = q3huff.Reader(data)
    relack = r.read_long() & 0xFFFFFFFF
    cmd = r.read_byte()
    return relack, cmd
 
def dec_start_srv(data):
    r = q3huff.Reader(data)
    server_id = r.read_long() & 0xFFFFFFFF
    msgack = r.read_long() & 0xFFFFFFFF
    relack = r.read_long() & 0xFFFFFFFF
    cmd = r.read_byte()
    return server_id, msgack, relack, cmd
 
def decrypt_cl(data, challenge, readcount=0):
    data = bytearray(data)
 
    offset = SV_DECODE_START
 
    server_id, msgack, reliableAcknowledge, _ = dec_start_srv(data)
 
    s = reliableCommands[reliableAcknowledge & (MAX_RELIABLE_COMMANDS-1)]
    index = 0
    key = (challenge ^ msgack ^ server_id) & 0xFF
 
    for i in range(readcount + offset, len(data)):
        if not s[index]:
            index = 0;
        if s[index] > 127 or s[index] == 0x25:
            key ^= 0x2e << (i & 1)
        else:
            key ^= s[index] << (i & 1)
        key &= 0xFF
 
        index += 1
 
        data[i] = data[i] ^ key
    return data
 
def decrypt(data, challenge, seq, readcount=0):
    data = bytearray(data)
 
    offset = CL_DECODE_START
 
    reliableAcknowledge, _ = dec_start(data)
 
    s = reliableCommands[reliableAcknowledge & (MAX_RELIABLE_COMMANDS-1)]
    index = 0
    key = (challenge ^ seq) & 0xFF
 
    for i in range(readcount + offset, len(data)):
        if not s[index]:
            index = 0;
        if s[index] > 127 or s[index] == 0x25:
            key ^= 0x2e << (i & 1)
        else:
            key ^= s[index] << (i & 1)
        key &= 0xFF
 
        index += 1
 
        data[i] = data[i] ^ key
    return data
 
def parse_commands(data):
    i = 0
 
    while True:
        if i >= len(data):
            return
        cmd = data[i]
        if cmd != 4:
            return
        i += 1
        idx = struct.unpack('<I', data[i:i+4])[0]
        i += 4
        s = data[i:data.index(b'\x00', i)+1]
        i += len(s)
        reliableCommands[idx] = s
        print(idx, repr(s))
 
 
pcap = rdpcap('graffiti-0baaf6c57f4f3efbed1e0d57bc02a13a.pcap')
 
start_dump = False
challenge = 0
challenge_server = 0
 
 
f = open('a.dm_71','wb')
 
fragmented_data = ''
frag_seq = -1
 
for p in pcap:
    if p.haslayer(IP) and p.haslayer(UDP) and p.haslayer(Raw):
        ip = p.getlayer(IP)
 
        if ip.src == '192.168.151.140':
            # client commands
            data = p.getlayer(UDP).load
            if not data.startswith(b'\xff'*4):
                n = struct.unpack('<I', data[:4])[0]
                #print(data.hex())
 
                dec = decrypt_cl(data[6:], challenge)
                server_id, msgack, relack, cmd = dec_start_srv(dec)
                if cmd == 4: # clc_clientCommand
                    print(hex(n), hex(server_id), msgack, relack,)
                    dec = decompress(dec)
                    parse_commands(dec[12:])
 
        elif ip.dst == '192.168.151.140':
            #server commands
 
            data = p.getlayer(UDP).load
 
            if not challenge and b'challengeResponse' in data:
                parts = data.split(b' ')
                challenge = int(parts[1])
                challenge_server = int(parts[2])
                print ('chall', challenge, challenge_server)
 
            if not data.startswith(b'\xff'*4):
                n = struct.unpack('<I', data[:4])[0]
 
                if n & FRAGMENTED:
                    frag_seq = n & ~FRAGMENTED
                    frag_off, frag_size = struct.unpack('<HH', data[4:8])
                    if frag_off == 0:
                        fragmented_data = data[8:]
                        assert len(fragmented_data) == frag_size
 
                    else:
                        assert n == frag_seq | FRAGMENTED
                        assert len(fragmented_data) == frag_off
                        assert len(data[8:]) == frag_size
                        fragmented_data = fragmented_data + data[8:]
                    continue
 
                if n != frag_seq and fragmented_data:
                    f.write(struct.pack('<I', frag_seq))
                    f.write(struct.pack('<I', len(fragmented_data)))
                    f.write(decrypt(fragmented_data, challenge, frag_seq))
                    fragmented_data = None
                    frag_seq = -1
                    start_dump = True
 
 
                if not start_dump:
                        continue
 
 
                f.write(struct.pack('<I', n))
                f.write(struct.pack('<I', len(data)-4))
                f.write(decrypt(data[4:], challenge, n))
