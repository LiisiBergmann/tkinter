from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def tervita():
    tervitus = 'Teie info on saadetud'
    messagebox.showinfo(message=tervitus)


raam = Tk()
raam.title("Info")


silt_1 = ttk.Label(raam, text="Nimi")
silt_1.grid(column=0, row=0, padx=5, pady=5, sticky=(N, W))
silt_2 = ttk.Label(raam, text="Perenimi")
silt_2.grid(column=0, row=1, padx=5, pady=5, sticky=(N, W))
silt_3 = ttk.Label(raam, text="Telefoni number")
silt_3.grid(column=0, row=2, padx=5, pady=5, sticky=(N, W))
silt_4 = ttk.Label(raam, text="Gmail")
silt_4.grid(column=0, row=3, padx=5, pady=5, sticky=(N, W))


# ROW alla
# column kõrvale


nimi = ttk.Entry(raam)
nimi.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))
perenimi = ttk.Entry(raam)
perenimi.grid(column=1, row=1, padx=5, pady=5, sticky=(N, W, E))
telefoni_number = ttk.Entry(raam)
telefoni_number.grid(column=1, row=2, padx=5, pady=5, sticky=(N, W, E))
gmail = ttk.Entry(raam)
gmail.grid(column=1, row=3, padx=5, pady=5, sticky=(N, W, E))

nupp = ttk.Button(raam, text="Saada ära", command=tervita)
nupp.grid(column=1, row=4, padx=5, pady=5, sticky=(N, S, W, E))


raam.columnconfigure(1, weight=1)
raam.rowconfigure(1, weight=1)


raam.mainloop()