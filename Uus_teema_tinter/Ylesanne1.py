from tkinter import *

raam = Tk()
raam.title("Bahama saarte lipp")
tahvel = Canvas(raam, width=600, height=600, background="white")
tahvel.grid()




tahvel.create_rectangle(0,0,         200,20, fill= "blue")
tahvel.create_rectangle(0,20,      200,40, fill = "yellow")
tahvel.create_rectangle(0,40,       200,60, fill = "blue")
tahvel.create_polygon(0,0,     50,30,      0,60,  fill="black")


raam.mainloop()

