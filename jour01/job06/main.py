class Animal:
    
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

animal_instance = Animal()

#Affiche l'âge initial
print(f"L'age de l'animal {animal_instance.age} ans")

#Appel de la méthode vieillir
animal_instance.vieillir()
print(f"L'age de l'animal {animal_instance.age} ans")

# Utilisation de la méthode nommer pour donner un nom à l'animal
animal_instance.nommer("Fidji")
print(f"l'animal se nomme {animal_instance.prenom}")

