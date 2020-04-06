class Atome:
    """ atomes simplifies, chosis parmi les 10 premiers elements du tableau
    periodique des elements de Mendeleiev"""
    table = [None, ('hydrogene', 0), ('helium', 2), ('lithium', 4), ('beryllium', 5), ('bore', 6),
             ('carbone', 6), ('azote', 7), ('oxygene', 8), ('fluor', 10), ('neon', 10)]

    def __init__(self, nat):
        """ le numero atomique determine le nombre de protons, d'electrons et de neutrons"""
        self.np = nat
        self.ne = nat
        self.nn = Atome.table[nat][1]

    def affiche(self):
        print()
        print("Nom de l'element : ", Atome.table[self.np][0])
        print("%s protons, %s electrons, %s neutrons" % (self.np, self.ne, self.nn))

class Ion(Atome):
    """les ions sont des atomes qui ont perdus ou gagnes des electrons"""
    def __init__(self, nat, charge):
        "le numero atomique et la charge electriaue determinent l'ion"
        # appel au constructeur de la classe Atome afin que les ions heritent des proprietes \
        # des atomes :
        Atome.__init__(self, nat)
        self.ne = self.ne - charge
        self.charge = charge

    def affiche(self):
        Atome.affiche(self)
        print("Particule electrisee. Charge =", self.charge)

