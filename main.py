from PIL import Image, ImageDraw
import os
import sys
from random import SystemRandom
random = SystemRandom()
xrange = range

img = Image.open("foto1.jpg")
out_1 = "_1.jpg"
out_2 = "_2.jpg"

img = img.convert('1')
width = img.size[0]*2
height = img.size[1]*2
image_A = Image.new('1',(width,height))
image_B = Image.new('1',(width,height))

draw_A = ImageDraw.Draw(image_A)
draw_B = ImageDraw.Draw(image_B)
patterns = ((1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1),
            (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1))

for x in xrange(0,int(width/2)):
    for y in xrange(0,int(height/2)):
        pixel = img.getpixel((x,y))
        pat = random.choice(patterns)
        draw_A.point((x*2,y*2),pat[0])
        draw_A.point((x*2+1,y*2),pat[1])
        draw_A.point((x*2,y*2+1),pat[2])
        draw_A.point((x*2+1,y*2+1),pat[3])
        if pixel == 0:  # Dark pixel so B gets the anti pattern
            draw_B.point((x * 2, y * 2), 1 - pat[0])
            draw_B.point((x * 2 + 1, y * 2), 1 - pat[1])
            draw_B.point((x * 2, y * 2 + 1), 1 - pat[2])
            draw_B.point((x * 2 + 1, y * 2 + 1), 1 - pat[3])
        else:
            draw_B.point((x * 2, y * 2), pat[0])
            draw_B.point((x * 2 + 1, y * 2), pat[1])
            draw_B.point((x * 2, y * 2 + 1), pat[2])
            draw_B.point((x * 2 + 1, y * 2 + 1), pat[3])

image_A.save(out_1,'PNG')
image_B.save(out_2,'PNG')