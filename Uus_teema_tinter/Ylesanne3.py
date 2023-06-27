from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def tervita():
    tervitus = 'Tere ' + nimi.get() + " " + perenimi.get() + "!"
    messagebox.showinfo(message=tervitus)
    print(str(tervitus.split('!'))+", rõõm sind näha, mulle ei meeldi sinu üllatused!")


raam = Tk()
raam.title("Tervitaja")


silt_1 = ttk.Label(raam, text="Nimi")
silt_1.grid(column=0, row=0, padx=5, pady=5, sticky=(N, W))
silt_2 = ttk.Label(raam, text="Perenimi")
silt_2.grid(column=0, row=1, padx=5, pady=5, sticky=(N, W))

nimi = ttk.Entry(raam)
nimi.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W, E))
perenimi = ttk.Entry(raam)
perenimi.grid(column=1, row=1, padx=5, pady=5, sticky=(N, W, E))

nupp = ttk.Button(raam, text="Tervita!", command=tervita)
nupp.grid(column=1, row=2, padx=5, pady=5, sticky=(N, S, W, E))


raam.columnconfigure(1, weight=1)
raam.rowconfigure(1, weight=1)


raam.mainloop()