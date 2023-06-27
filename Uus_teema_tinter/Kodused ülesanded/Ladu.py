from tkinter import *
from tkinter import ttk
raam = Tk()
ladu = {}
ladu[1] = {"õun",4,0.5}
ladu[2] = {"pirn",5,0.6}
ladu[3] = {"tomat",1,1.2}
def pane_korvi():


triipkood = ttk.Entry(raam)
triipkood.grid(column=0, row=0, padx= 5, pady=5)
toode = ttk.Entry(raam)
toode.grid(column=0, row=0, padx= 5, pady=5)

mainloop()
