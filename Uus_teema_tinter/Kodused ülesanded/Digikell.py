from tkinter import *
from tkinter.ttk import *
from time import strftime

#neid numbreid oli ikka väga raske maalida, terve öö kulus selleks, vähemalt sai tehtud
raam = Tk()
raam.title('Digikell')

def time():
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000, time)
#tahvel.delete('all')




lbl = Label(raam, font=('times', 50, 'bold'),
            background='white',
            foreground='black')
lbl.pack(anchor='center')
time()

mainloop()