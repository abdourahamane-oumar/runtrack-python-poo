class Student:
    def __init__(self, nom, prenom, num_etudiant, credits=0):
        self._nom = nom
        self._prenom = prenom
        self._num_etudiant = num_etudiant
        self._credits = credits
        self._level = self._student_eval()

    #Ceci et l'assesseurs (getters)
    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom

    def get_num_etudiant(self):
        return self._num_etudiant

    def get_credits(self):
        return self._credits

    def get_level(self):
        return self._level

    #Ceci et la parti mutateurs (setters)
    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._student_eval()
            print(f"{credits} crédits ont été ajoutés à l'étudiant {self._prenom} {self._nom}.")
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    #permets l'évaluations en privée du niveau de l'étudiant
    def _student_eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    #créations de la méthode student_info, pour afficher les infos en console
    def student_info(self):
        print(f"NOM = {self._prenom}") 
        print(f"Prénom = {self._nom}") 
        print(f"id = {self._num_etudiant}")
        print(f"Niveau = {self._level}")


john_doe = Student("Doe", "John", 145)

john_doe.add_credits(20)
john_doe.add_credits(30)
john_doe.add_credits(30)
print(f"Le nombre de crédits de {john_doe.get_prenom()} {john_doe.get_nom()} est de {john_doe.get_credits()} points.")
john_doe.student_info()

