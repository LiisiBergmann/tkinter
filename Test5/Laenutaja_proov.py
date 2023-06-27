from datetime import *

class Laenutaja_proov:

    def __init__(self, nimi):
        self.nimi = nimi

    def getNimi(self):
        return self.nimi
    def setnimi(self, nimi):
        self.nimi = nimi

    def laenutatud_raamatute_list(self, raamatute_list):
        laenutatud_raamatute_listid = []
        for raamat in raamatute_list:
            if raamat.getLaenutaja() == self.nimi:
                laenutatud_raamatute_listid.append(raamat)
        return laenutatud_raamatute_listid

    def raamatuteViivisteMaksumusteSummaTänaseni(self, raamatute_list):
        laenutatud_raamatute_list = self.laenutatud_raamatute_list(raamatute_list)
        summa = 0
        for raamat in laenutatud_raamatute_list:
            summa += raamat.viiviseMaksumusTänaseni()
        return summa

    def raamatuteViivisteMaksumusteSummaAntudKuupäevani(self, raamatute_list, kuupäev):
        laenutatud_raamatute_list = self.laenutatud_raamatute_list(raamatute_list)
        summa = 0
        for raamat in laenutatud_raamatute_list:
            summa += raamat.viiviseMaksumusAntudKuupäevani(kuupäev)
        return summa