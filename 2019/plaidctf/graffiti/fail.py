#!/usr/bin/env python
from scapy.all import *

"""
TCP/UDP proxy.
"""

import argparse
import signal
import logging
import select
import socket


FORMAT = '%(asctime)-15s %(levelname)-10s %(message)s'
logging.basicConfig(format=FORMAT)
LOGGER = logging.getLogger()

#LOCAL_DATA_HANDLER = lambda x:x
REMOTE_DATA_HANDLER = lambda x:x

BUFFER_SIZE = 2 ** 12  # 1024. Keep buffer size as power of 2.


def u16( dd ):
    return ( ord( dd[1] ) << 8 ) + ord( dd[0] )

d = {}
d2 = []
t = 0

def LOCAL_DATA_HANDLER( data ):
    global d , d2 , t
    '''
    r = d2[t]
    t += 1
    l = 7
    if t > 15:
        return data[:l] + d2[ t ][l:]
    else:
        return data
    '''
    sequence = u16( data )
    if sequence > 28 and sequence < 6001:
        print '[+] mod! ' , sequence
        a = 20
        l = 4
        #return d[ sequence ]
        return data[:a] + d[ sequence ][a:a+l] + data[ a + l : ]
        #return data
    else:
        print sequence
        return data
    #'''


def udp_proxy(src, dst):
    """Run UDP proxy.
    
    Arguments:
    src -- Source IP address and port string. I.e.: '127.0.0.1:8000'
    dst -- Destination IP address and port. I.e.: '127.0.0.1:8888'
    """
    LOGGER.debug('Starting UDP proxy...')
    LOGGER.debug('Src: {}'.format(src))
    LOGGER.debug('Dst: {}'.format(dst))
    
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind(ip_to_tuple(src))
    
    client_address = ('192.168.31.234',27960)
    server_address = ip_to_tuple(dst)

    #s = conf.L3socket(iface='en0')
    
    LOGGER.debug('Looping proxy (press Ctrl-Break to stop)...')
    while True:
    #for i in range( 10 ):
        #print i
        data, address = proxy_socket.recvfrom(BUFFER_SIZE)
        #print address
        
        if client_address == None:
            client_address = address

        if address == client_address:
            print 'to server'
            #print data
            data = LOCAL_DATA_HANDLER(data)
            proxy_socket.sendto(data, server_address)
            #s.send( IP( dst = "192.168.31.49" , src = '192.168.31.160' ) / UDP( dport = 27960 , sport = 27960 ) / Raw( load = data ) )
        elif address == server_address:
            #print 'to client'
            #print data
            data = REMOTE_DATA_HANDLER(data)
            #s.send( IP( dst = "192.168.31.234" , src = '192.168.31.160' ) / UDP( dport = 27960 , sport = 27960 ) / Raw( load = data ) )
            proxy_socket.sendto(data, client_address)
            #client_address = None
        else:
            LOGGER.warning('Unknown address: {}'.format(str(address)))

    


def ip_to_tuple(ip):
    """Parse IP string and return (ip, port) tuple.
    
    Arguments:
    ip -- IP address:port string. I.e.: '127.0.0.1:8000'.
    """
    ip, port = ip.split(':')
    return (ip, int(port))
# end-of-function ip_to_tuple


def main():
    """Main method."""
    parser = argparse.ArgumentParser(description='TCP/UPD proxy.')
    
    # TCP UPD groups
    proto_group = parser.add_mutually_exclusive_group(required=True)
    proto_group.add_argument('--tcp', action='store_true', help='TCP proxy')
    proto_group.add_argument('--udp', action='store_true', help='UDP proxy')
    
    parser.add_argument('-s', '--src', required=True, help='Source IP and port, i.e.: 127.0.0.1:8000')
    parser.add_argument('-d', '--dst', required=True, help='Destination IP and port, i.e.: 127.0.0.1:8888')
    
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument('-q', '--quiet', action='store_true', help='Be quiet')
    output_group.add_argument('-v', '--verbose', action='store_true', help='Be loud')
    
    args = parser.parse_args()
    
    if args.quiet:
        LOGGER.setLevel(logging.CRITICAL)
    if args.verbose:
        LOGGER.setLevel(logging.NOTSET)
    
    if args.udp:
        udp_proxy(args.src, args.dst)
    elif args.tcp:
        tcp_proxy(args.src, args.dst)
# end-of-function main    


ps = rdpcap( './graffiti-0baaf6c57f4f3efbed1e0d57bc02a13a.pcap' )
print 'done!'

for p in ps[UDP]:
    try:
        if p[IP].dst == '192.168.151.139':
            #print u16( p.load[:2] )
            d[ u16( p.load[:2] ) ] = p.load
            d2.append( p.load )
    except:
        pass

main()
