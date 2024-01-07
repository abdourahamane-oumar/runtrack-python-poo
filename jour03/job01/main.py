class Ville:
    def __init__(self, nom, nb_habitants):
        self._nom = nom
        self._nb_habitants = nb_habitants
        
        #Ceci et l'assesseurs (getters)
    def get_nom(self):
        return self._nom
    def get_nb_habitants(self):
        return self._nb_habitants
    
        #Ceci et la parti mutateurs (setters)
    def set_nb_habitants(self, nb_habitants):
        self._nb_habitants = nb_habitants
 
class Personne:
    def __init__(self, nom, âge, ville):
        self._nom = nom
        self._âge = âge
        self._ville = ville

         #Ceci et l'assesseurs (getters)
    def get_nom(self):
        return self._nom
    def get_âge(self):
        return self._âge
    def get_ville(self):
        return self._ville

    def ajouter_population(self):
        ville = self._ville
        ville.set_nb_habitants(ville.get_nb_habitants() + 1)


#Création de l'objet Ville avec les arguments "Paris" et "100000"
Paris = Ville("Paris", 1000000)
print(f"Population de la ville de {Paris.get_nom()}: {Paris.get_nb_habitants()} ")

#Création de l'objet Ville avec les arguments "Marseille" et "861635"
Marseille = Ville("Marseille", 861635)
print(f"Population de la ville de {Marseille.get_nom()}: {Marseille.get_nb_habitants()} ")

#Création des Objet Personne avec les argument entre ().
P1 = Personne("John", 45, Paris)
P2 = Personne("Myrtille", 4, Paris)
P3 = Personne("Chloé", 18, Marseille)

#Affiche chaque personne dans la console.
print(f"{P1.get_nom()}, {P1.get_âge()} ans, habitant à Paris")
print(f"{P2.get_nom()}, {P2.get_âge()} ans, habitant à Paris")
print(f"{P3.get_nom()}, {P3.get_âge()} ans, habitant à Marseille")

#Permet d'ajouter les personne dans la liste de la ville
P1.ajouter_population()
P2.ajouter_population()
P3.ajouter_population()

#Création des Objet Ville de Paris et Marseille après l'arriver de nouvelle personne.
print(f"Mise a jour de la population de la ville de {Paris.get_nom()} {Paris.get_nb_habitants()} habitants")
print(f"Mise a jour de la population de la ville de {Marseille.get_nom()} {Marseille.get_nb_habitants()} habitants")
