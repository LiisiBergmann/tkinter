from tkinter import *
from tkinter.ttk import *
from time import strftime
import time

raam = Tk()
raam.title('Digikell')
tahvel = Canvas(raam, width=300, height=200, background="white")
tahvel.grid()
vahe = ''


def üks(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1 + 25, y1, x1 + 25, y1 + 35)
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 65)
def kaks(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 40, x1 - 5, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale

def kolm(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale

def neli(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla

def viis(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale

def kuus(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 25)  # alla
    tahvel.create_line(x1, y1 + 30, x1 + 20, y1 + 30)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 35, x1 + 25, y1 + 55)  # alla
    tahvel.create_line(x1, y1 + 60, x1 + 20, y1 + 60)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 55, x1 - 5, y1 + 35)  # alla

def seitse(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 + 25, y1 + 35, x1 + 25, y1 + 55)  # alla

def kaheksa(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 60, x1 - 5, y1 + 40)  # alla
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale

def üheksa(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale

def null(x1,y1):
    x1 = 30
    y1 = 40
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1 - 5, y1 + 60, x1 - 5, y1 + 40)  # alla
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale

def tick():
    tahvel.delete('all')
    tahvel.create_oval(102.5, 50, 97.5, 55, fill="black")
    tahvel.create_oval(102.5, 70, 97.5, 75, fill="black")
    tahvel.create_oval(182.5, 50, 177.5, 55, fill="black")
    tahvel.create_oval(182.5, 70, 177.5, 75, fill="black")
    global vahe
    string = time.strftime('%H:%M:%S')
    tund1 = int(string[0])
    tund2 = int(string[1])
    minut1 = int(string[3])
    minut2 = int(string[4])
    sekund1 = int(string[6])
    sekund2 = int(string[7])
    x1 = 30
    y1 = 40
    if tund1 == 0:
        null()
    if tund1 == 1:
        üks(x1,y1)
    if tund1 == 2:
        kaks()

    if tund2 == 1:
        x1 += 40
        üks(x1,y1)
    if tund2 == 2:
        x1 += 40
        kaks()
    if tund2 == 3:
        x1 += 40
        kolm()
    if tund2 == 4:
        x1 += 40
        neli()
    if tund2 == 5:
        x1 += 40
        viis()
    if tund2 == 6:
        x1 += 40
        kuus()
    if tund2 == 7:
        x1 += 40
        seitse()
    if tund2 == 8:
        x1 += 40
        kaheksa()
    if tund2 == 9:
        x1 += 40
        üheksa()
    if tund2 == 0:
        x1 += 40
        null()

    if minut1 == 5:
        x1 += 80
        viis()
    if minut1 == 4:
        x1 += 80
        neli()
    if minut1 == 3:
        x1 += 80
        kolm()
    if minut1 == 2:
        x1 += 80
        kaks()
    if minut1 == 1:
        x1 += 80
        üks(x1,y1)
    if minut1 == 0:
        x1 += 80
        null()

    
    if minut2 == 1:
        x1 += 120
        üks(x1,y1)
    if minut2 == 2:
        x1 += 120
        kaks()
    if minut2 == 3:
        x1 += 120
        kolm()
    if minut2 == 4:
        x1 += 120
        neli()
    if minut2 == 5:
        x1 += 120
        viis()
    if minut2 == 6:
        x1 += 120
        kuus()
    if minut2 == 7:
        x1 += 120
        seitse()
    if minut2 == 8:
        x1 += 120
        kaheksa()
    if minut2 == 9:
        x1 += 120
        üheksa()
    if minut2 == 0:
        x1 += 120
        null()

    if sekund2 == 1:
        x1 += 160
        üks(x1,y1)
    if sekund2 == 2:
        x1 += 160
        kaks()
    if sekund2 == 3:
        x1 += 160
        kolm()
    if sekund2 == 4:
        x1 += 160
        neli()
    if sekund2 == 5:
        x1 += 160
        viis()
    if sekund2 == 6:
        x1 += 160
        kuus()
    if sekund2 == 7:
        x1 += 160
        seitse()
    if sekund2 == 8:
        x1 += 160
        kaheksa()
    if sekund2 == 9:
        x1 += 160
        üheksa()
    if sekund2 == 0:
        x1 += 160
        null()

    if sekund1 == 5:
        x1 += 200
        viis()
    if sekund1 == 4:
        x1 += 200
        neli()
    if sekund1 == 3:
        x1 += 200
        kolm()
    if sekund1 == 2:
        x1 += 200
        kaks()
    if sekund1 == 1:
        x1 += 200
        üks(x1,y1)
    if sekund1 == 0:
        x1 += 200
        null()


    tahvel.after(1000, tick)

tick()
raam.mainloop()
