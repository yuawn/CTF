#!/usr/bin/env python
from pwn import *
import os , codecs , json

res = []

while True:
    obj = ''

    logs = os.listdir( 'fdr' ) 

    fs = [[] for _ in range(20)]

    for i in range(20):
        name = 'fdr-log-%d.log' % i
        for f in sorted(logs):
            if f.startswith( name ):
                fs[i].append( f )


    for i in range( 1000 ):
        for j in range(20):
            try:
                o = open( 'fdr/%s' % fs[j][i] ).read()
                if o:
                    obj += codecs.decode( codecs.decode( eval( o[1:] ) , 'base64' ) , 'zlib' )
            except:
                pass


    is_light = False
    pwd = ''
    lights = []

    if not obj:
        continue

    for i in obj[6:-1].strip().split( '}{"_io"' ):
        i = '{"_io"' + i + '}'
        i = json.loads( i )
        body = i['packet_content']['packet_body']
        if 'messages' in body:
            msg = i['packet_content']['packet_body']['messages'][0]
            message_control , data = msg['message_control'] , msg['data']
            
            if message_control == 1985:
                if is_light:
                    if ( pwd , lights ) not in res:
                        res.append( ( pwd , lights ) )
                    pwd = ''
                    lights = []
                    is_light = False
                c = ''
                if data[0] == 2:
                    c = '{'
                elif data[0] == 3:
                    c = '}'
                elif data[0] == 1:
                    c = '\n'
                else:
                    c = chr( data[0] - 4 + 0x41 )

                pwd += c

                #print( 'message_control -> %d, Pressing -> %s' % ( message_control , c ) )
            elif message_control == 1988:
                is_light = True
                light = data[0] << 24 | data[1] << 16 | data[2] << 8 | data[3]
                if light:
                    lights.append( light )
                #print( 'message_control -> %d, Light -> %s' % ( message_control , bin(light)[2:].rjust( 32 , '0' ) ) )
            else:
                print( 'Unkown message_control -> %d !!!!!!!!!!!' % message_control )
           
    print '-' * 0x10
    #print res
    for i in res:
        print i
    log = open( 'info' , 'w+' )
    log.write( str(res) )
    log.close()

    sleep( 10 )





'''
{
   "u""_io":{
      "u""_io":{
         
      },
      "u""bits_left":0,
      "u""bits":0
   },
   "u""_parent":{
      "u""_io":"None",
      "u""_parent":"None",
      "u""_root":"None",
      "u""pcm825":"None"
   },
   "u""_root":"None",
   "u""packet_type":1,
   "u""packet_content":{
      "u""_parent":"None",
      "u""_root":"None",
      "u""_io":"None",
      "u""operation_code":2,
      "u""packet_body":{
         "u""_io":"None",
         "u""_parent":"None",
         "u""_root":"None",
         "u""message_count":1,
         "u""messages":[
            {
               "u""_parent":"None",
               "u""can_status":7696,
               "u""message_control":1988,
               "u""data_type":3,
               "u""service_code":114,
               "u""byte_count":4,
               "u""_root":"None",
               "u""error_counter":16954,
               "u""message_code":43,
               "u""_io":"None",
               "u""frame_type":0,
               "u""node_id":50,
               "u""time_stamp":140729627348947,
               "u""can_identifier":1988,
               "u""data":[
                  0,
                  0,
                  0,
                  0
               ]
            }
         ]
      },
      "u""frame_counter":109
   }
}
'''
