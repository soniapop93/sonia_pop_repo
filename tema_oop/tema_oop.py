# Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
# ○ __init__ : instanțiem numărător și numitor
# ○ __str__ : afisam "numărător/numitor"
# ○ __add__ : returnam o noua fractie care reprezinta adunarea
# ○ __sub__: returnam o nouă fracție care reprezinta scădearea
# ○ inverse: returnează o nouă fracție (inversa fracției)

class Fractie:

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return '%s/%s' % (self.numarator, self.numitor)

    def cel_mai_mare_numitor_comun(self, numarator, numitor):
        while numarator % numitor != 0:
            numarator_vechi = numarator
            numitor_vechi = numitor

            numarator = numarator_vechi
            numitor = numarator_vechi % numitor_vechi
        return numitor

    def __add__(self, alta_fractie):
        new_numarator = self.numarator * alta_fractie.numitor + self.numitor * alta_fractie.numarator
        new_numitor = self.numitor * alta_fractie.numitor
        cmmnc = self.cel_mai_mare_numitor_comun(new_numarator, new_numitor)
        result = Fractie(int(new_numarator/cmmnc), int(new_numitor/cmmnc))
        return result

    def __sub__(self, alta_fractie):
        new_numarator = self.numarator * alta_fractie.numitor - self.numitor * alta_fractie.numarator
        new_numitor = self.numitor * alta_fractie.numitor
        cmmnc = self.cel_mai_mare_numitor_comun(new_numarator, new_numitor)
        result = Fractie(int(new_numarator/cmmnc), int(new_numitor/cmmnc))
        return result

    def inverse(self):
        return Fractie(self.numitor, self.numarator)




print(Fractie(3,4))

f1 = Fractie(5,7)
f2 = Fractie(3,7)
f3 = f1+f2
print(f3)


f4 = Fractie(5,7)
f5 = Fractie(3,7)
f6 = f4-f5
print(f6)

f = Fractie(3,4)
print(f.inverse())