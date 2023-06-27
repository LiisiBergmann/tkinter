from tkinter import *
import time

def tick():
    aeg2 = time.strftime('%H:%M:%S')
    kell.config(text = aeg2)
    kell.after(200, tick)

raam = Tk()
kell = Label(raam, font = ('arial',100,'bold'), bg ='white')
kell.pack(fill = BOTH, expand=1)
tick()
raam.mainloop()