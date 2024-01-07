class Compte_Bancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self._numero_compte = numero_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert

        #Création des méthodes: 

    def afficher(self):
        print("numero_compte:", self._numero_compte)
        print("Nom:", self._nom)
        print("prenom:" ,self._prenom)
        print("Solde:", self._solde,"€")
        print("Découvert autorisé:", self._decouvert)

    def afficherSolde(self):
        print(f"Solde du client {self._prenom}: {self._solde}€.")

    def versement(self, montant):
        self._solde += montant
        print(f"Versement de {montant}€. Nouveaux solde: {self._solde}€")

    def retrait(self, montant):
        if self._solde >= montant or self._decouvert:
            self._solde -= montant
            print(f"Retrait de {montant}€. Nouveaux solde: {self._solde}€")
        else:
            print("Solde insuffisant pour le retrait.")

    def agios(self):
        if self.solde < 0:
            agios = self.calculer_agios()
            self._solde -= agios
            print("Des agios de {} ajoutés")
    
    def virement(self, numero_compte, destinataire, montant):
        if self._solde >= montant or self._decouvert:
            self._solde -= montant
            destinataire.versement(montant)
            print(f"Virement de {montant}€ vers le compte {numero_compte}")
        else:
            print("Solde insuffisant pour effectuer le virement.")


C1 = Compte_Bancaire(numero_compte="45379",nom="Textor",prenom="John", solde=800)
C2 = Compte_Bancaire(numero_compte="53940",nom="Bajwel",prenom="Rudy", solde=-300, decouvert=True)

C1.afficher()
C1.versement(300)
C1.retrait(1000)

C1.virement("45379", C2, 300)

C2.afficher()



