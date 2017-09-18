#!/usr/bin/env python
# -*- coding: ascii -*-

def get_gif_num_frames(filename):
    frames = 0
    with open(filename, 'rb') as f:
        if f.read(6) not in ('GIF87a', 'GIF89a'):
            raise GIFError('not a valid GIF file')
        f.seek(4, 1)
        def skip_color_table(flags):
            if flags & 0x80: f.seek(3 << ((flags & 7) + 1), 1)
        flags = ord(f.read(1))
        f.seek(2, 1)
        skip_color_table(flags)
        while True:
            block = f.read(1)
            if block == ';': break
            if block == '!': f.seek(1, 1)
            elif block == ',':
                frames += 1
                f.seek(8, 1)
                skip_color_table(ord(f.read(1)))
                f.seek(1, 1)
            else: raise GIFError('unknown block type')
            while True:
                l = ord(f.read(1))
                if not l: break
                f.seek(l, 1)
    return frames


from PIL import Image
import os

#f = get_gif_num_frames('task.gif')
#print f
def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0: 
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass

import sys

def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print "Cant load", infile
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()

    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)

            #new_im = Image.new("RGB", im.size)
            new_im.paste(im)
            new_im.save(str(i)+'.tiff')
            #if(os.stat('foo' + str(i)+'.png')):
                # os.remove('foo' + str(i) + '.jpg')
            i += 1
            mypalette = im.getpalette()
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence


#processImage( 'task.gif' )





'''
im = Image.open('task.gif')
for i, frame in enumerate(iter_frames(im)):
    o = Image.new("RGB", frame.size )
    o.paste( frame )
    o.save('%d.png' % i)
'''



#for i in range( 310 ):
#    if c == 12:
#        c = 1
#        continue
#    c = c + 1
#    im = Image.open('%d.png' % i)
im = Image.open('task.gif')
out = Image.new("RGB", (620, 420))

c = 1

t = 0

for i, frame in enumerate(iter_frames(im)):
    if i % 11 == 0:
        for x in range( 2 ):
            for y in range( 420 ):
                p = frame.getpixel( ( x , y ) )
                out.putpixel( ( x + i * 2 ,  419 - y ) , p )
        c = 1
        continue
    c = c + 1
    print c
    for x in range( 2 ):
        for y in range( 420 ):
            p = frame.getpixel( ( x , y ) )
            out.putpixel( ( x + i * 2 ,  y ) , p )


out.save("gif.png")