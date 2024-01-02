#Création de la classe personne avec les attributs Nom et Prénom.
class Personne:

 def __init__(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom

#Ajout de la méthode SePrésenter avec l'ajout des paramètres
 def SePresenter(self):
  return f"Je suis {self.nom} {self.prenom}"

#Instanciation de plusieurs personnes et appel de la methode SePrésenter pour vérifier le fonctionnement.
p1 = Personne ("David", "Lafarge")
print(p1.SePresenter())
p2 = Personne ("Romain", "Dubois")
print(p2.SePresenter())
p3 = Personne ("Loris", "Abeille")
print(p3.SePresenter())
p4 = Personne ("Martin", "Sommier")
print(p4.SePresenter())




