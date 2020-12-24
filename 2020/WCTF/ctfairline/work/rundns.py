#!/usr/bin/env python3
from dnslib.server import DNSServer, DNSLogger, DNSRecord, RR
from dnslib import QTYPE
import time
import sys
import random

class TestResolver:
    def resolve(self,request,handler):
        q_name = str(request.q.get_qname())
        reply = request.reply()
        client_host, client_port = handler.client_address
        protocol = handler.protocol
        qname, qtype = request.q.qname, QTYPE[request.q.qtype]
        ip = '1.2.3.4'
        print(f'{client_host}:{client_port} {protocol} {qtype} {qname} -> {ip}')
        reply.add_answer(*RR.fromZone(q_name + " 0 A " + ip))
        return reply
logger = DNSLogger(prefix=False)
resolver = TestResolver()
server = DNSServer(resolver,port=53,address="0.0.0.0")
server.start_thread()
try:
    print('Listen on port 53...')
    while True:
        time.sleep(1)
        sys.stderr.flush()
        sys.stdout.flush()
except KeyboardInterrupt:
    pass
finally:
    server.stop()
