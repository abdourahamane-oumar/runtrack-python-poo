#Création de la classe Livre avec les attributs privé
class Livre:
    def __init__(self, titre, auteur, nombre_pages, disponible=True):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = nombre_pages
        self._disponible = disponible

 #Ceci et l'assesseurs (getters)
    def get_titre(self):
        return self._titre 
    
    def get_auteur(self):
        return self._auteur
    
    def get_nombre_pages(self):
        return self._nombre_pages
    
    def verification(self):
        return self._disponible
    
    def emprunter(self):
        if self._disponible:
         print(f"Le livre {self._titre} a été emprunté.")
         self._disponible = False
        else:
            print(f"Le livre {self._titre} n'est pas disponible")
        
    def rendre(self):
        if not self._disponible:
            print(f"Le livre {self._titre} à été rendu.")
            self._disponible = True
        else:
            print(f"Le livre {self._titre} ne peut être rendue, il à deja été restituer")

 #Ceci et la parti mutateurs (setters)
    def set_titre(self, titre):
        self._titre = titre

    def set_auteur(self, auteur):
        self._auteur = auteur

    def set_nombre_pages(self, nombre_pages):
        self._nombre_pages = nombre_pages
        if isinstance (nombre_pages, int) and nombre_pages > 0:
            self._nombre_pages = nombre_pages
        else:
            print("Erreur: le nombre de page doit être supérieur à 0, veuillez réésayez.")

 #Création de la méthodes nommée vérification
    def verification(self):
        return self._disponible
    
mon_livre = Livre( "Excalibur", "Pierre Dubois", 46,)
print("Le titre:", mon_livre.get_titre())
print("l'auteur:", mon_livre.get_auteur())
print("le nombre de pages:",mon_livre.get_nombre_pages())
print("livre disponible :", mon_livre.verification())
mon_livre.set_nombre_pages(1)
print("")
#Emprunte le livre.
mon_livre.emprunter()

#Vérifie une seconde fois si la possibilité d'emprunter le livre et possible.
mon_livre.emprunter()

#Permet de rendre le livre.
mon_livre.rendre()

#Permet de rendre une seconde fois le livre, un message négatif s'affiche car il à déja été restituer.
mon_livre.rendre()









