fail = open("noolemängu_tulemused.txt","r")
tulemused = []
sõnastik = {}
summa = 0
for rida in fail:
    osad = rida.split(":")
    tulemused = osad[1].split()
    for arv in tulemused:
        summa += int(arv)
    sõnastik[osad[0]] = summa
    summa = 0
sõnastik_koopia = sõnastik
suurim = ""
for arv in sõnastik:
    suurim = arv
    for j in sõnastik:
        if sõnastik[j] > sõnastik[suurim]:
            suurim = j
    print(suurim+":",sõnastik[suurim])
    sõnastik[suurim] = 0