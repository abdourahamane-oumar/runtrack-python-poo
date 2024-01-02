class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        print(f"Informations du produit - Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%")

    def modifierNom(self, nouveauNom):
        self.nom = nouveauNom

    def modifierPrixHT(self, nouveauPrixHT):
        self.prixHT = nouveauPrixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA


produit1 = Produit("Baguette", 20, 10)
produit2 = Produit("Tomates", 30, 5)

produit1.afficher()
produit2.afficher()


produit1.modifierNom("Baguette")
produit1.modifierPrixHT(40)

produit2.modifierNom("Tomates")
produit2.modifierPrixHT(50)
 

print("\nInformations après modification :")
produit1.afficher()
produit2.afficher()


prixTTC1 = produit1.CalculerPrixTTC()
prixTTC2 = produit2.CalculerPrixTTC()


print(f"\nPrix TTC de la {produit1.obtenirNom()}: {prixTTC1}")
print(f"Prix TTC du {produit2.obtenirNom()}: {prixTTC2}")
