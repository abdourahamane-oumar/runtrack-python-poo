#Création de la classe Livre avec les attributs privé
class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = nombre_pages

 #Ceci et l'assesseurs (getters)
    def get_titre(self):
        return self._titre 
    
    def get_auteur(self):
        return self._auteur
    
    def get_nombre_pages(self):
        return self._nombre_pages
        
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
    
print("")
mon_livre = Livre( "Excalibur", "Pierre Dubois", 46)
print("Le titre:", mon_livre.get_titre())
print("l'auteur:", mon_livre.get_auteur())
print("le nombre de pages:",mon_livre.get_nombre_pages())
mon_livre.set_nombre_pages(-20)
print("")









