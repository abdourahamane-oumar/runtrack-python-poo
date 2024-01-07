class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []       

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                break
    
    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                break

    def afficherListe(self):
        for tache in self.taches:
            print(f"Tâche: {tache.titre} - Description: {tache.description} - Statut: {tache.statut}")
    
    def filterListe(self, statut):
        filter_taches = [tache for tache in self.taches if tache.statut == statut]
        return filter_taches
    
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 5",)
tache3 = Tache("Rédiger le rapport", "Inclure les données du projet")
        
Liste = ListeDeTaches()
Liste.ajouterTache (tache1)
Liste.ajouterTache (tache2)
Liste.ajouterTache (tache3)

#Permets de voir tout les taches actuelle
print("Toutes les tâches:")
Liste.afficherListe()

#Permets de supprimer une tâche puis renvoie la liste pour vérifier que elle à bien été supprimer
print("\nSupprimer une Tâche:")
Liste.supprimerTache("Rédiger le rapport")
Liste.afficherListe()

#Modifier la tâche en terminée, puis l'afficher pour voir si la modification à été prises.
print("\nTâche Terminée:")
Liste.marquerCommeFinie("Réviser pour l'examen")
Liste.afficherListe()

#Afficher la liste des tâches à faire.
print("\nListe des tâches à faire:")
taches_a_faire = Liste.filterListe("à faire")
for tache in taches_a_faire:
    print(f"Tâche: {tache.titre} - Description: {tache.description} - Statut: {tache.statut}")