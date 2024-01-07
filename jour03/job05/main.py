import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, advers):
        degats = random.randint(1, 10)
        print(f"{self.nom} attaque {advers.nom} et lui enleve {degats} de dégats. ")
        advers.vie -= degats


class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Peut tu choisir le niveaux de difficulté (1,2 ou 3):"))

    def lancerJeu(self):
        self.choisirNiveau()
        Lord = Personnage("Lord", 80 * self.niveau)
        Floyd = Personnage("Floyd", 40 * self.niveau)

        while Lord.vie > 0 and Floyd.vie > 0:
            Lord.attaquer(Floyd)
            if Floyd.vie <= 0:
                print(f"{Floyd.nom} à succombé à c'est blessure. ! {Lord.nom} à remporter la bataille .")
                break

            Floyd.attaquer(Lord)
            if Lord.vie <= 0:
                print (f"{Lord.nom} à succombé à c'est blessure.! {Floyd.nom} à remporter la bataille.")
                break
            
            print(f"{Lord.nom} - Vie: {Lord.vie} / {Floyd.nom} - Vie : {Floyd.vie}")
            input("Presser la touche Entrer pour continuer.")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()         