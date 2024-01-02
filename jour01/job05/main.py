#Création de la classe Point avec les attributs
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

#Création de toute les méthodes 
        
    def afficherlesPoints(self):
        print(f"les cordonnées des point sont {self.x} est {self.y}")

        
    def afficherX(self):
        print(f"Affiche respective du point x est: {self.x}")

    def afficherY(self):
        print(f"Affiche respective du point y est: {self.y}")

    def changerX(self, nouveauX):
        self.x = nouveauX
        print(f"La Nouvelle valeur de x est: {self.x}")

    def changerY(self, nouveauY):
        self.y = nouveauY
        print(f"La Nouvelle valeur de y est: {self.y}")


point_instance = Point (5, 2)

#Appel de plusieurs méthodes.

point_instance.afficherlesPoints()
point_instance.afficherX()
point_instance.afficherY()

#Changement des coordoonées
point_instance.changerX(0)
point_instance.changerY(7)