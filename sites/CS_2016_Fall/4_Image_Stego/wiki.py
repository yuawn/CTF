from PIL import Image

orig = Image.open('./Steganography_original.png')
res = Image.new("RGB",(200,200))

for x in range(200):
    for y in range(200):
        pix = orig.getpixel( (x,y) )

        b = []

        for i in range(3):

                b.append( pix[i] & 0x3 )

        npix = tuple(b)

        res.putpixel( (x,y) , npix )

res.save('wiki_res.png')
