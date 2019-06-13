#!/usr/bin/env python
import paramiko
from pwn import *

# fb{you_win_the_game_again_again}

sh = ssh( 'osquerygame' , 'challenges.fbctf.com' , password = 'osquerygame' , port = 2222 ,  )
y = sh.shell()


def show():
    p = 'SELECT * FROM farm WHERE action = \'show\';'
    y.send( p + '\n' )

def quests():
    p = 'select * from farm_quests;'
    y.send( p + '\n' )

def pickup( src ):
    p = 'SELECT * FROM farm WHERE action = \'pickup\' AND src = %s;' % hex( src )
    y.send( p + '\n' )

def move( src , dst ):
    p = 'SELECT * FROM farm WHERE action = \'move\' AND src = %s AND dst = %s;' % ( hex( src ) , hex( dst ) )
    y.send( p + '\n' )

def _water( dst ):
    p = 'SELECT * FROM farm WHERE action = \'water\''
    for i in dst:
        p += ' AND dst = %s' % hex( i )
    y.send( p + ';\n' )

def plant( dst ):
    p = 'SELECT * FROM farm WHERE action = \'plant\''
    for i in dst:
        p += ' AND dst = %s' % hex( i )
    y.send( p + ';\n' )


def parse_map( w = False ):
    o = y.recvuntil( 'y> ' )
    needle = o.split('\n').index( '  0 1 2 3 4 5 6 7 8 9 A B C D E F \r' )
    pig_pos , sheep_pos , sunflower_pos , water_pos = 0 , 0 , 0 , 0
    plot_pos = []
    for n , l in enumerate( o.split('\n')[ needle + 1 : needle + 1 + 16 ] ):
        print n , l
        if sheep in l:
            sheep_pos = ( n << 4 ) + l.index( sheep ) / 4
        if pig in l:
            pig_pos = ( n << 4 ) + l.index( pig ) / 4
        if sunflower in l:
            sunflower_pos = ( n << 4 ) + l.index( sunflower ) / 4
        if water in l:
            water_pos = ( n << 4 ) + l.index( water ) / 4
        if plot in l:
            plot_pos.append( ( n << 4 ) + l.index( plot ) / 4 )

    return pig_pos , sheep_pos , sunflower_pos , water_pos , plot_pos



print y.recvuntil( 'y> ' )

sheep = '\xf0\x9f\x90\x91'
pig = '\xf0\x9f\x90\xb7'
grass = '\xf0\x9f\x8c\xbf'
sunflower = '\xf0\x9f\x8c\xbb'
water = '\xf0\x9f\x9a\xb0'
plot = '\xe2\xac\x9c'


y.send( 'select * from farm;\n' )


pig_pos , sheep_pos , sunflower_pos , water_pos , plot_pos = parse_map()
print plot_pos
print 'pig -> %s\nsheep -> %s\nsunflower -> %s\nwater -> %s' % ( hex( pig_pos ) , hex( sheep_pos ) , hex( sunflower_pos ) , hex( water_pos ) )
move( sheep_pos , pig_pos + 1 )


pig_pos , sheep_pos , sunflower_pos , water_pos , plot_pos = parse_map()
print 'pig -> %s\nsheep -> %s\nsunflower -> %s\nwater -> %s' % ( hex( pig_pos ) , hex( sheep_pos ) , hex( sunflower_pos ) , hex( water_pos ) )

plant( plot_pos )
print y.recvuntil( 'y> ' )

_water( plot_pos )
print y.recvuntil( 'y> ' )

pickup( plot_pos[0] )
print y.recvuntil( 'y> ' )

quests()
print y.recvuntil( 'y> ' )

show()
print y.recvuntil( 'y> ' )