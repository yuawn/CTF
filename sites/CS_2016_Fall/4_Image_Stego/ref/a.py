from PIL import Image
image= Image.open("warp_speed.5978d1405660e365872cf72dddc7515603f657f12526bd61e56feacf332cccad.jpg")
image2 = Image.new("RGB", (504, 500))

for y in range(500):
    for x in range(504):
        x2 = x + (y / 8) * 504
        y2 = y % 8
        try:
            p = image.getpixel((x2 % 1000, y2 + (x2 / 1000)*8))
        except :
            pass
        image2.putpixel((x,y), p)

image2.save("result.png")
