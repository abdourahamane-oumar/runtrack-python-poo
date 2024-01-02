class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation de la classe Personnage
personnage_instance = Personnage(x=2, y=3)
print("Position initiale :", personnage_instance.position())

#Déplacement du personnage
personnage_instance.gauche()
personnage_instance.haut()
print("Nouvelle position :", personnage_instance.position())
