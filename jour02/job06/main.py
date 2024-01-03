class Commande:
    def __init__(self, num_commande):
        self._num_commande = num_commande
        self._plats_commandes = {}  
        self._statut_commande = "En cours"

    def _calculer_total(self):
        total = sum(prix for prix, statut in self._plats_commandes.values() if statut == "En cours")
        return total

    def ajouter_plat(self, nom_plat, prix_plat):
        self._plats_commandes[nom_plat] = (prix_plat, "En cours")
        print(f"Plat ajouté à la commande : {nom_plat}")

    def annuler_commande(self):
        self._plats_commandes.clear()
        self._statut_commande = "Annulée"
        print("Commande annulée.")

    def afficher_commande(self):
        total = self._calculer_total()
        print(f"\nCommande #{self._num_commande} - Statut : {self._statut_commande}")
        for plat, (prix, statut) in self._plats_commandes.items():
            print(f"{plat} - Prix : {prix}€ - Statut : {statut}")
        print(f"Total à payer : {total}€")

    def calculer_tva(self, taux_tva=0.20):
        total = self._calculer_total()
        tva = total * taux_tva
        return tva


commande1 = Commande(1)

commande1.ajouter_plat("Pizza", 12.5)
commande1.ajouter_plat("Salade", 8.0)
commande1.ajouter_plat("Pâtes", 10.0)

commande1.afficher_commande()

tva_calculée = commande1.calculer_tva()
print(f"\nTVA à payer : {tva_calculée}€")

commande1.annuler_commande()
