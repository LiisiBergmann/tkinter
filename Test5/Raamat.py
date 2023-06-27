from datetime import *

class Raamat:

    def __init__(self, nimi, lugeja, viivis, kuupäev):
        self.nimi = nimi
        self.lugeja = lugeja
        self.viivis = viivis
        self.kuupäev = kuupäev

    def getnimi(self):
        return self.nimi
    def setnimi(self, nimi):
        self.nimi = nimi
    def getlugeja(self):
        return self.lugeja
    def setlugeja(self, lugeja):
        self.lugeja = lugeja
    def getviivis(self):
        return self.viivis
    def setviivis(self, viivis):
        self.viivis = viivis
    def getkuupäev(self):
        return self.kuupäev
    def setkuupäev(self, kuupäev):
        self.kuupäev = kuupäev


    def getLaenutaja(self):
        return self.lugeja


    def viiviseMaksumusTänaseni(self):
        kuupäevade_vahe = (date.today() - self.kuupäev).days
        return self.viivis * kuupäevade_vahe

    def viiviseMaksumusAntudKuupäevani(self, antudkuupäev):
        if antudkuupäev > self.kuupäev:
            kuupäevade_vahe = (antudkuupäev - self.kuupäev).days
            return self.viivis * kuupäevade_vahe
        else:
            return 0

    def toString(self):
        print("Raamatu pealkiri:",self.nimi)
        print("Raamatu lugeja:", self.lugeja)
        print("Raamatu viivis:", str(self.viivis))
        print("Raamatu tagastamiskuupäev:", str(self.kuupäev))
        print("Raamatu viivis tänaseni:", str(round(self.viiviseMaksumusTänaseni(),2)))

