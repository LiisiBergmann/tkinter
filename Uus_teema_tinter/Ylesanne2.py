from tkinter import *

raam = Tk()

def soome_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Soome lipp")
    tahvel = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel.create_rectangle(200, 0, 270, 392, fill="#002F6C")
    tahvel.create_rectangle(0, 160, 600, 230, fill="#002F6C")
    tahvel.grid()

def taani_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Taani lipp")
    tahvel2 = Canvas(uus_aken, width=600, height=392, background="red")
    tahvel2.create_rectangle(200, 0, 270, 392, fill="white")
    tahvel2.create_rectangle(0, 160, 600, 230, fill="white")
    tahvel2.grid()

def eesti_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Eesti lipp")
    tahvel3 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel3.create_rectangle(0, 0, 600, 131, fill="#002F6C")
    tahvel3.create_rectangle(0, 131, 600, 262, fill="#000000")
    tahvel3.grid()

def saksamaa_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Saksamaa lipp")
    tahvel4 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel4.create_rectangle(0, 0, 600, 131, fill="#000000")
    tahvel4.create_rectangle(0, 131, 600, 262, fill="#f80404")
    tahvel4.create_rectangle(0, 262, 600, 393, fill="#eec900")
    tahvel4.grid()

def venemaa_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Venemaa lipp")
    tahvel5 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel5.create_rectangle(0, 0, 600, 131, fill="#fbfafa")
    tahvel5.create_rectangle(0, 131, 600, 262, fill="#0804f6")
    tahvel5.create_rectangle(0, 262, 600, 393, fill="#e50202")
    tahvel5.grid()

def poola_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Poola lipp")
    tahvel6 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel6.create_rectangle(0, 0, 600, 200, fill="#fbfafa")
    tahvel6.create_rectangle(0, 200, 600, 400, fill="#ff0202")
    tahvel6.grid()

def leedu_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Leedu lipp")
    tahvel7 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel7.create_rectangle(0, 0, 600, 131, fill="#eec900")
    tahvel7.create_rectangle(0, 131, 600, 262, fill="#003300")
    tahvel7.create_rectangle(0, 262, 600, 393, fill="#690808")
    tahvel7.grid()

def läti_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Leedu lipp")
    tahvel8 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel8.create_rectangle(0, 0, 600, 160, fill="#690808")
    tahvel8.create_rectangle(0, 160, 600, 250, fill="#ffffff")
    tahvel8.create_rectangle(0, 250, 600, 410, fill="#690808")
    tahvel8.grid()

def jaapani_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Jaapani lipp")
    tahvel9 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel9.create_rectangle(0, 600, 600, 600, fill="#ffffff")
    tahvel9.create_oval(200, 200, 300, 300, fill="#690808")
    tahvel9.grid()

def tai_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Tai lipp")
    tahvel9 = Canvas(uus_aken, width=600, height=360, background="white")
    tahvel9.create_rectangle(0, 0, 600, 60, fill="#f80202")
    tahvel9.create_rectangle(0, 60, 600, 120, fill="#ffffff")
    tahvel9.create_rectangle(0, 120, 600, 240, fill="#0702f8")
    tahvel9.create_rectangle(0, 240, 600, 300, fill="#ffffff")
    tahvel9.create_rectangle(0, 300, 600, 360, fill="#f80202")
    tahvel9.grid()

def itaalia_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Itaalia lipp")
    tahvel10 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel10.create_rectangle(0, 600, 200, 0, fill="#08bc21")
    tahvel10.create_rectangle(200, 600, 400, 0, fill="#fbfbfb")
    tahvel10.create_rectangle(400, 600, 600, 0, fill="#f20000")
    tahvel10.grid()

def tshehhi_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Tshehhi lipp")
    tahvel11 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel11.create_rectangle(0, 0, 600, 200, fill="#ffffff")
    tahvel11.create_rectangle(0, 200, 600, 400, fill="#fb0808")
    tahvel11.create_polygon(0,0, 250,200, 0,400, fill="#2608fb")
    tahvel11.grid()

def kreeka_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Kreeka lipp")
    tahvel12 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel12.create_rectangle(0, 0, 600, 45, fill="#2938da")
    tahvel12.create_rectangle(0, 45, 600, 90, fill="#ffffff")
    tahvel12.create_rectangle(0, 90, 600, 135, fill="#2938da")
    tahvel12.create_rectangle(0, 135, 600, 180, fill="#ffffff")
    tahvel12.create_rectangle(0, 180, 600, 225, fill="#2938da")
    tahvel12.create_rectangle(0, 225, 600, 270, fill="#ffffff")
    tahvel12.create_rectangle(0, 270, 600, 315, fill="#2938da")
    tahvel12.create_rectangle(0, 315, 600, 360, fill="#ffffff")
    tahvel12.create_rectangle(0, 360, 600, 405, fill="#2938da")
    tahvel12.create_rectangle(0, 405, 600, 450, fill="#ffffff")

    tahvel12.create_rectangle(0, 225, 250, 0, fill="#2938da")

    tahvel12.create_rectangle(100, 0, 155, 225, fill="#ffffff")
    tahvel12.create_rectangle(0, 85, 250, 140, fill="#ffffff")
    tahvel12.grid()

def norra_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Norra lipp")
    tahvel13 = Canvas(uus_aken, width=600, height=400, background="#ff3500")
    tahvel13.create_rectangle(180, 0, 290, 500, fill="#fbfbfb")
    tahvel13.create_rectangle(0, 120, 700, 230, fill="#fbfbfb")
    tahvel13.create_rectangle(210, 0, 260, 500, fill="#00059b")
    tahvel13.create_rectangle(0, 150, 700, 200, fill="#00059b")
    tahvel13.grid()

def laose_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Laose lipp")
    tahvel14 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel14.create_rectangle(0, 0, 600, 100, fill="#e31d06")
    tahvel14.create_rectangle(0, 100, 600, 290, fill="#2126ab")
    tahvel14.create_rectangle(0, 290, 600, 390, fill="#e31d06")
    tahvel14.create_oval(100, 100, 300, 300, fill="#ffffff")
    tahvel14.grid()

def guyana_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("Guyana lipp")
    tahvel15 = Canvas(uus_aken, width=600, height=400, background="#3cb833")
    tahvel15.create_polygon(0,0, 600,200, 0,400, fill="white")
    tahvel15.create_polygon(0, 20, 540, 200, 0, 380, fill="#f6ef17")
    tahvel15.create_polygon(0, 0, 300, 200, 0, 400, fill="black")
    tahvel15.create_polygon(0, 20, 250, 200, 0, 380, fill="#eb2020")
    tahvel15.grid()

def south_africa_lipp():
    uus_aken = Toplevel(raam)
    uus_aken.title("South Africa lipp")
    tahvel16 = Canvas(uus_aken, width=600, height=400, background="white")
    tahvel16.create_rectangle(0, 0, 600, 200, fill="red")
    tahvel16.create_rectangle(0, 200, 600, 400, fill="blue")
    tahvel16.create_polygon(40, 0, 300, 180, 600,180, 600, 240, 320, 240, 40,400, fill="green")
    tahvel16.create_polygon(80, 0, 340, 220, 600, 220, 600, 280, 320, 240, 40, 400, fill="#ffffff")

    tahvel16.create_polygon(0, 25, 280, 200, 0, 375, fill="yellow")
    tahvel16.create_polygon(0, 50, 250, 200, 0, 350, fill="black")
    tahvel16.grid()




raam.title("Lipud")
soome_nupp = Button(raam, text="Soome", command=soome_lipp)
taani_nupp = Button(raam, text="Taani", command=taani_lipp)
eesti_nupp = Button(raam, text="Eesti", command=eesti_lipp)

saksamaa_nupp = Button(raam, text="Saksamaa", command=saksamaa_lipp)
venemaa_nupp = Button(raam, text="Venemaa", command=venemaa_lipp)
poola_nupp = Button(raam, text="Poola", command=poola_lipp)

leedu_nupp = Button(raam, text="Leedu", command=leedu_lipp)
läti_nupp = Button(raam, text="Läti", command=läti_lipp)
jaapani_nupp = Button(raam, text="Jaapani", command=jaapani_lipp)

tai_nupp = Button(raam, text="Tai", command=tai_lipp)
itaalia_nupp = Button(raam, text="Itaalia", command=itaalia_lipp)
tshehhi_nupp = Button(raam, text="Tshehhi", command=tshehhi_lipp)

kreeka_nupp = Button(raam, text="Kreeka", command=kreeka_lipp)
norra_nupp = Button(raam, text="Norra", command=norra_lipp)
laose_nupp = Button(raam, text="Laos", command=laose_lipp)

guyana_nupp = Button(raam, text="Guyana", command=guyana_lipp)
south_africa_nupp = Button(raam, text="South Africa", command=south_africa_lipp)




soome_nupp.grid(column=1, row=0, padx=5, pady=7, sticky=(N, W))
taani_nupp.grid(column=2, row=0, padx=5, pady=7, sticky=(N, W))
eesti_nupp.grid(column=3, row=0, padx=5, pady=7, sticky=(N, W))

saksamaa_nupp.grid(column=1, row=1, padx=5, pady=7, sticky=(N, W))
venemaa_nupp.grid(column=2, row=1, padx=5, pady=7, sticky=(N, W))
poola_nupp.grid(column=3, row=1, padx=5, pady=7, sticky=(N, W))

leedu_nupp.grid(column=1, row=2, padx=5, pady=7, sticky=(N, W))
läti_nupp.grid(column=2, row=2, padx=5, pady=7, sticky=(N, W))
jaapani_nupp.grid(column=3, row=2, padx=5, pady=7, sticky=(N, W))

tai_nupp.grid(column=1, row=3, padx=5, pady=7, sticky=(N, W))
itaalia_nupp.grid(column=2, row=3, padx=5, pady=7, sticky=(N, W))
tshehhi_nupp.grid(column=3, row=3, padx=5, pady=7, sticky=(N, W))

kreeka_nupp.grid(column=1, row=4, padx=5, pady=7, sticky=(N, W))
norra_nupp.grid(column=2, row=4, padx=5, pady=7, sticky=(N, W))
laose_nupp.grid(column=3, row=4, padx=5, pady=7, sticky=(N, W))

guyana_nupp.grid(column=1, row=5, padx=5, pady=7, sticky=(N, W))
south_africa_nupp.grid(column=2, row=5, padx=5, pady=7, sticky=(N, W))

raam.mainloop()
