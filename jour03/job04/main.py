class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.nb_buts += 1
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (#{self.numero}, {self.position}):")
        print(f"Buts marqués: {self.nb_buts}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print("-------------------------")
        
class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()
            
    def mettreAJourStatistiquesJoueur(self, numero_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.numero == numero_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()
            
 #Création des joueurs               
Enric = Joueur("Enric", 4, "Défenseur Central")
Lucas = Joueur("Lucas", 10, "Milieux Offensive")
Robin = Joueur("Robin", 7, "Attaquant")
Paolo = Joueur("Paolo",1, "Gardien de but")

#Création des équipes
FCBarcelone = Equipe("Fc_Barcelone")
ManchesterCity = Equipe("Manchester_City")

#Ajout des joueurs dans les équipes
FCBarcelone.ajouterJoueur(Enric)
ManchesterCity.ajouterJoueur(Lucas)
FCBarcelone.ajouterJoueur(Robin)
ManchesterCity.ajouterJoueur(Paolo)

# #Statistiques
FCBarcelone.afficherStatistiquesJoueurs()
ManchesterCity.afficherStatistiquesJoueurs()
print("\n")
#Simuler un match et re afficher les statistiques.
FCBarcelone.mettreAJourStatistiquesJoueur(4,"carton_rouge")
ManchesterCity.mettreAJourStatistiquesJoueur(10,"passe")
FCBarcelone.mettreAJourStatistiquesJoueur(7,"but")

FCBarcelone.afficherStatistiquesJoueurs()
ManchesterCity.afficherStatistiquesJoueurs()
