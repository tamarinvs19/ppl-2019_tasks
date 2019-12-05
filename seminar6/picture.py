from PIL import PSDraw
from PIL import Image, ImageDraw, ImageFont
im = Image.open("wallpaper_debian.jpg")

d = ImageDraw.Draw(im)
d.text((100, 50), "Hello World", fill=(255,255,0))
fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)

im.save('new.jpg')
