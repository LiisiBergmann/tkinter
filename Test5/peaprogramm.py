from Raamat import Raamat
from Laenutaja import *
from datetime import *

laenutajad = []
raamatud = []

fail = open("laenutused.txt")
for rida in fail:
    andmed = rida.split(":")
    lugeja = andmed[0].strip()
    raamatu_andmed = andmed[1].strip().split('"')
    raamatu_pealkiri = raamatu_andmed[1]
    viivis_ja_kuupäev = raamatu_andmed[2].strip().split()
    viivis = float(viivis_ja_kuupäev[0])
    kuupäev = date(int(viivis_ja_kuupäev[1].split("-")[0]), int(viivis_ja_kuupäev[1].split("-")[1]),int(viivis_ja_kuupäev[1].split("-")[2]))
    raamat = Raamat(raamatu_pealkiri, lugeja, viivis,kuupäev)
    laenutaja = Laenutaja(lugeja)
    if laenutaja not in laenutajad:
        laenutajad.append(laenutaja)
    raamatud.append(raamat)


suvaline_kuupäev = date(2018, 12, 12)
for laenutaja in laenutajad:
    viiviste_summa_tänaseni = laenutaja.raamatuteViivisteMaksumusteSummaTänaseni(raamatud)
    viiviste_summa_antud_kuupäevani = laenutaja.raamatuteViivisteMaksumusteSummaAntudKuupäevani(raamatud, suvaline_kuupäev)
    print(laenutaja.getNimi(), "on võlgu:")
    print("Tänaseni:", viiviste_summa_tänaseni)
    print("Antud kuupäevani", suvaline_kuupäev, ":", viiviste_summa_antud_kuupäevani)