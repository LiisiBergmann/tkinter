
from datetime import *
class Laenutaja:
    def __init__(self, nimi):
        self.nimi = nimi

    def getNimi(self):
        return self.nimi
    def setnimi(self, nimi):
        self.nimi = nimi

    def laenutaja_raamatud(self, raamatute_list):
        laenutatud_raamatute_list = []
        for raamat in raamatute_list:<
            if raamat.getLaenutaja() == self.nimi:
                laenutatud_raamatute_list.append(raamat)
        return laenutatud_raamatute_list

    def raamatuteViivisteMaksumusteSummaTänaseni(self, raamatute_list):
        laenutatud_raamatute_list = self.laenutaja_raamatud(raamatute_list)
        summa = 0
        for raamat in laenutatud_raamatute_list:
            summa += raamat.viiviseMaksumusTänaseni()
        return summa

    def raamatuteViivisteMaksumusteSummaAntudKuupäevani(self, raamatute_list, kuupäev):
        laenutatud_raamatute_list = self.laenutaja_raamatud(raamatute_list)
        summa = 0
        for raamat in laenutatud_raamatute_list:
            summa += raamat.viiviseMaksumusAntudKuupäevani(kuupäev)
        return summa

    def toString(self):
        print("Laenutaja nimi:", self.nimi)


