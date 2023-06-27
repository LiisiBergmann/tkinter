from tkinter import *
from tkinter.ttk import *
from time import strftime


raam = Tk()
raam.title('Digikell')

tahvel = Canvas(raam, width=200, height=200, background="white")
tahvel.grid()

x1=30
y1=40
x2=30
y2=40
                 #(x1,y1,       x2,y2)

def kaks():
    tahvel.create_line(x1+25, y1, x1+25, y1 + 35)
    tahvel.create_line(x1+25, y1 + 40, x1+25, y1 + 65)
    """tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1+25, y1 + 5,    x1+25, y1 + 30)#alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65,      x1+20, y1 + 65)#kõrvale"""
    #tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale#
    #tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 25)  # alla
    #tahvel.create_line(x1, y1 + 30, x1 + 20, y1 + 30)  # kõrvale
    #tahvel.create_line(x1 + 25, y1 + 35, x1 + 25, y1 + 55)  # alla
    #tahvel.create_line(x1, y1 + 60, x1 + 20, y1 + 60)  # kõrvale
    #tahvel.create_line(x1 - 5, y1 + 55, x1 - 5, y1 + 35)  # alla


    #üheksa
    #tahvel.create_line(x1, y1 ,     x1+20, y1)#kõrvale
    #tahvel.create_line(x1+25, y1 + 5,    x1+25, y1 + 30)#alla
    #tahvel.create_line(x1-5, y1 + 5,     x1-5, y1 + 30)#alla
    #tahvel.create_line(x1, y1 + 35,     x1+20, y1 + 35)#kõrvale
    #tahvel.create_line(x1+25, y1 + 40,    x1+25, y1 + 60)#alla
    #tahvel.create_line(x1, y1 + 65,      x1+20, y1 + 65)#kõrvale

    #kaheksa
    #tahvel.create_line(x1, y1,        x1+20, y1)#kõrvale
    #tahvel.create_line(x1+25, y1 + 5,      x1+25, y1 + 30)#alla
    #tahvel.create_line(x1-5, y1 + 5,       x1-5, y1 + 30)#alla
    #tahvel.create_line(x1, y1 + 35,      x1+20, y1 + 35)#kõrvale
    #tahvel.create_line(x1-5, y1 + 60,     x1-5, y1 + 40)#alla
    #tahvel.create_line(x1+25, y1 + 40,        x1+25, y1 + 60)#alla
    #tahvel.create_line(x1, y1 + 65,    x1+20, y1 + 65)#kõrvale


    #seitse
    #tahvel.create_line(x1, y1,        x1+20, y1)#kõrvale
    #tahvel.create_line(x1+25, y1+5,        x1+25, y1 + 30)#alla
    #tahvel.create_line(x1+25, y1 + 35,        x1+25, y1 + 55)#alla

    #kuus
    #tahvel.create_line(x1, y1,       x1+20, y1)#kõrvale
    #tahvel.create_line(x1-5, y1+5,       x1-5, y1 + 25)#alla
    #tahvel.create_line(x1, y1 + 30,         x1+20, y1 + 30)#kõrvale
    #tahvel.create_line(x1+25, y1 + 35,       x1+25, y1 + 55)#alla
    #tahvel.create_line(x1, y1 + 60,         x1+20, y1 + 60)#kõrvale
    #tahvel.create_line(x1-5, y1 + 55,        x1-5, y1 + 35)#alla

    #viis
    #tahvel.create_line(x1, y1,        x1+20, y2)#kõrvale
    #tahvel.create_line(x1-5, y1 + 5,        x1-5, y1 + 25)#alla
    #tahvel.create_line(x1, y1 + 30,        x1+20, y1 + 30)#kõrvale
    #tahvel.create_line(x1+25, y1 + 35,        x1+25, y1 + 58)#alla
    #tahvel.create_line(x1+20, y1 + 62,        x1, y1 + 62)#kõrvale

#tahvel.create_line(x1, y2,           x2 + 20, y2)#kõrvale
#tahvel.create_line(x1+20, y1+5,      x1+20, y1 + 25)#alla
#tahvel.create_line(x1+15, y1 + 30,       x1, y1 + 30)#kõrvale
#tahvel.create_line(x1, y1 + 35,       x1, y1 + 55)#alla
#tahvel.create_line(x1, y1 + 60,       x1+20, y1 + 60)#kõrvale
kaks()
mainloop()