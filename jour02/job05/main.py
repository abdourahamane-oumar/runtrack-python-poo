#Classe plus assignation des attributs(marque,modele,année...)
class Voiture:
    def __init__(self, marque, modele, année, kilometrage, en_marche=False, reservoir=50):
        self._marque = marque
        self._modele = modele
        self._année = année
        self._kilometrage = kilometrage
        self._en_marche = en_marche
        self._reservoir = reservoir
    

        #Ceci et l'assesseurs (getters)
    def get_marque(self):
        return self._marque
    def get_modele(self):
        return self._modele
    def get_année(self):
        return self._année
    def get_kilometrage(self):
        return self._kilometrage
    def get_en_marche(self):
        return self._en_marche
    def get_reservoir(self):
        return self._reservoir
    
        #Ceci et la parti mutateurs (setters)
    def set_marque(self, marque):
        self._marque = marque
    def set_modele(self, modele):
        self._modele = modele
    def set_année(self, année):
        self._année = année
    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage
    def set_en_marche(self, en_marche):
        self._en_marche = en_marche
    def set_reservoir(self, reservoir):
        self._reservoir = reservoir

    def _verifier_plein(self):
        return self._reservoir

        #Création de la méthode demarrer et arreter afin de changer la valeurs de l'attribut en_marche en True et en False
    def démarrer(self):
        if self._verifier_plein() > 5:
            self._en_marche = True
            print("La voiture peut démarrer")
        else:
            print("La voiture ne peut pas démarrer, il n'y à pas suffisament d'essence")

    def arreter(self):
        self._en_marche = False
        print("La voiture c'est arrêtée")
        
ma_voiture = Voiture("Peugeot", "308", "2023", "84300",)
print("Marque:", ma_voiture.get_marque())
print("Modele:", ma_voiture.get_modele())
print("l'année de mises en circulation:",ma_voiture.get_année())
print("kilomètres:", ma_voiture.get_kilometrage())
print("En marche:", ma_voiture.get_en_marche())
print("niveaux du réservoir:", ma_voiture.get_reservoir())

#Permets d'afficher en ligne de commande le message de la methode démarrer.
ma_voiture.démarrer()

#Permets d'afficher en ligne de commande le message de la methode arreter.
ma_voiture.arreter()
