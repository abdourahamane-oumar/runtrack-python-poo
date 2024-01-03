#Création de la classe Rectangle avec les attributs privé
class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

 #Ceci et l'assesseurs (getters)
    def get_longueur(self):
        return self._longueur
    
    def get_largeur(self):
        return self._largeur
    
 #Ceci et la parti mutateurs (setters)
    def set_longueur(self, longueur):
        self._longueur = longueur

    def set_largeur(self, largeur):
        self._largeur = largeur

mon_rectangle = Rectangle(10, 5)

print("Longeur initiale:", mon_rectangle.get_longueur())
print("Largeur initiale:", mon_rectangle.get_largeur())

print("")
mon_rectangle.set_longueur(18)
mon_rectangle.set_largeur(10)

print("longeur modifier:", mon_rectangle.get_longueur())
print("Largeur modifier:", mon_rectangle.get_largeur())
    

    