from tkinter import *
from pixboard import *
from math import sin


width = 256
height = 256
setup(width, height)

x = 0
while x < width:
    y = 0
    while y < height:
        red = x
        green = y
        blue = int((sin(x/12) + 1) * 127)
        set_pixel(x, y,(green, blue, red))
        #set_pixel(x, y,(blue, green, red))
        y += 1
    x += 1


show()