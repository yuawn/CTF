from PIL import Image
import re

orig = Image.open('./stego-db93e2fd60dfe6e1192e3124c67f4a42.png')
#orig = Image.open('./mblue.png')
res = Image.new("RGB",(640,436))

s = ''

for x in range(640):
    s = ''
    for y in range(200,230):
        #if y not in range(140,260):
            #continue
        pix = orig.getpixel( (x,y) )

        b = []

        for i in range(3):

            #b.append( pix[i] )

            if i == 2:
                s +=str( pix[i] & 0x1 )


                b.append( pix[i] & 0x1 )
            else:
                b.append( pix[i] & 0x0 )

        #npix = tuple(b)

        #res.putpixel( (x,y) , npix )
    print s[:160]
#res.save('res.png')
#print s[:8]
#print s
s2 = re.findall('........',s)
s3 = ''
print s2
for i in s2:
    #if int(i,2) in range(32,127):
    s3 += chr(int(i,2))

print s3
