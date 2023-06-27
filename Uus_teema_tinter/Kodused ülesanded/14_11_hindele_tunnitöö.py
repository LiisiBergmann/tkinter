from tkinter.ttk import *
from time import strftime
from tkinter import *
import time


raam = Tk()
raam.title('Digikell')
tahvel = Canvas(raam, width=300, height=200, background="white")
tahvel.grid()
vahe = ''


def üks(x1, y1):
    tahvel.create_line(x1 + 25, y1, x1 + 25, y1 + 35)
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 65)


def kaks(x1, y1):
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 40, x1 - 5, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale


def kolm(x1, y1):
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale


def neli(x1, y1):
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 65)  # alla


def viis(x1, y1):
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale


def kuus(x1, y1):
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 25)  # alla
    tahvel.create_line(x1, y1 + 30, x1 + 20, y1 + 30)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 60, x1 - 5, y1 + 40)  # alla


def seitse(x1, y1):
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 + 25, y1 + 35, x1 + 25, y1 + 65)  # alla


def kaheksa(x1, y1):
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 - 5, y1 + 60, x1 - 5, y1 + 40)  # alla
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale


def üheksa(x1, y1):
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1, y1 + 35, x1 + 20, y1 + 35)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale


def null(x1, y1):
    tahvel.create_line(x1, y1, x1 + 20, y1)  # kõrvale
    tahvel.create_line(x1 + 25, y1 + 5, x1 + 25, y1 + 30)  # alla
    tahvel.create_line(x1 - 5, y1 + 5, x1 - 5, y1 + 30)  # alla
    tahvel.create_line(x1 - 5, y1 + 60, x1 - 5, y1 + 40)  # alla
    tahvel.create_line(x1 + 25, y1 + 40, x1 + 25, y1 + 60)  # alla
    tahvel.create_line(x1, y1 + 65, x1 + 20, y1 + 65)  # kõrvale


def numbrid():
    tahvel.delete('all')
    tahvel.create_oval(105.5, 60, 100.5, 65, fill="black")
    tahvel.create_oval(105.5, 80, 100.5, 85, fill="black")
    tahvel.create_oval(190.5, 60, 185.5, 65, fill="black")
    tahvel.create_oval(190.5, 80, 185.5, 85, fill="black")


    global vahe


    string = time.strftime('%H:%M:%S')
    tunni_esimene_arv = int(string[0])
    tunni_teine_arv = int(string[1])
    minuti_esimene_arv = int(string[3])
    minuti_teine_arv = int(string[4])
    sekundi_esimene_arv = int(string[6])
    sekundi_teine_arv = int(string[7])
    x1 = 30
    y1 = 40

    if tunni_esimene_arv == 0:
        null(x1, y1)

    if tunni_esimene_arv == 1:
        üks(x1, y1)

    if tunni_esimene_arv == 2:
        kaks(x1, y1)

    if tunni_teine_arv == 1:
        x1 += 40
        üks(x1, y1)

    if tunni_teine_arv == 2:
        x1 += 40
        kaks(x1, y1)

    if tunni_teine_arv == 3:
        x1 += 40
        kolm(x1, y1)

    if tunni_teine_arv == 4:
        x1 += 40
        neli(x1, y1)

    if tunni_teine_arv == 5:
        x1 += 40
        viis(x1, y1)

    if tunni_teine_arv == 6:
        x1 += 40
        kuus(x1, y1)

    if tunni_teine_arv == 7:
        x1 += 40
        seitse(x1, y1)

    if tunni_teine_arv == 8:
        x1 += 40
        kaheksa(x1, y1)

    if tunni_teine_arv == 9:
        x1 += 40
        üheksa(x1, y1)

    if tunni_teine_arv == 0:
        x1 += 40
        null(x1, y1)

    if minuti_esimene_arv == 5:
        x1 += 45
        viis(x1, y1)

    if minuti_esimene_arv == 4:
        x1 += 45
        neli(x1, y1)

    if minuti_esimene_arv == 3:
        x1 += 45
        kolm(x1, y1)

    if minuti_esimene_arv == 2:
        x1 += 45
        kaks(x1, y1)

    if minuti_esimene_arv == 1:
        x1 += 45
        üks(x1, y1)

    if minuti_esimene_arv == 0:
        x1 += 45
        null(x1, y1)

    if minuti_teine_arv == 0:
        x1 += 40
        null(x1, y1)

    if minuti_teine_arv == 1:
        x1 += 40
        üks(x1, y1)

    if minuti_teine_arv == 2:
        x1 += 40
        kaks(x1, y1)

    if minuti_teine_arv == 3:
        x1 += 40
        kolm(x1, y1)

    if minuti_teine_arv == 4:
        x1 += 40
        neli(x1, y1)

    if minuti_teine_arv == 5:
        x1 += 40
        viis(x1, y1)

    if minuti_teine_arv == 6:
        x1 += 40
        kuus(x1, y1)

    if minuti_teine_arv == 7:
        x1 += 40
        seitse(x1, y1)

    if minuti_teine_arv == 8:
        x1 += 40
        kaheksa(x1, y1)

    if minuti_teine_arv == 9:
        x1 += 40
        üheksa(x1, y1)

    if sekundi_esimene_arv == 5:
        x1 += 50
        viis(x1, y1)

    if sekundi_esimene_arv == 4:
        x1 += 50
        neli(x1, y1)

    if sekundi_esimene_arv == 3:
        x1 += 50
        kolm(x1, y1)

    if sekundi_esimene_arv == 2:
        x1 += 50
        kaks(x1, y1)

    if sekundi_esimene_arv == 1:
        x1 += 50
        üks(x1, y1)

    if sekundi_esimene_arv == 0:
        x1 += 50
        null(x1, y1)

    if sekundi_teine_arv == 0:
        x1 += 50
        null(x1, y1)

    if sekundi_teine_arv == 1:
        x1 += 50
        üks(x1, y1)

    if sekundi_teine_arv == 2:
        x1 += 50
        kaks(x1, y1)

    if sekundi_teine_arv == 3:
        x1 += 50
        kolm(x1, y1)

    if sekundi_teine_arv == 4:
        x1 += 50
        neli(x1, y1)

    if sekundi_teine_arv == 5:
        x1 += 50
        viis(x1, y1)

    if sekundi_teine_arv == 6:
        x1 += 50
        kuus(x1, y1)

    if sekundi_teine_arv == 7:
        x1 += 50
        seitse(x1, y1)

    if sekundi_teine_arv == 8:
        x1 += 50
        kaheksa(x1, y1)

    if sekundi_teine_arv == 9:
        x1 += 50
        üheksa(x1, y1)

    tahvel.after(1000, numbrid)


numbrid()
raam.mainloop()
