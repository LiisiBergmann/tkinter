fail = open("taksod.txt","r")
nimed = []
hind = []
kmhind = []
summa = 0
for rida in fail:
    osa = rida.strip().split(",")
    nimed.append(osa[0])
    hind.append(osa[1])
    kmhind.append(float(osa[2]))
    
for arv in hind:
    summa += float(arv)
print(summa)
a = []
summa1 = 0
print(sum(kmhind))



