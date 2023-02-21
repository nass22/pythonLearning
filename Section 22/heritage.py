# 156

class EtreVivant:
    ESPECE_ETRE_VIVANT = "(être vivant non identifié)"
    
    def AfficherInfosEtreVivant(self):
        print("Info être vivant : " + self.ESPECE_ETRE_VIVANT)

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félin)"

class Personne:
    ESPECE_ETRE_VIVANT = "Humain (Mammifère Homo sapiens)"   # variable de classe (1 pour toutes les Personnes)

    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        info_personne = "Bonjour, je m'appelle " + self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + " ans"

        print(info_personne)

        if self.age != 0:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18

    def DemanderNom(self):
        self.nom = input("Nom de la personne : ")

    def AfficherInfosEtreVivant(self):
        print("Info être vivant : " + Personne.ESPECE_ETRE_VIVANT)

class Etudiant(Personne):
    def __init__(self, nom: str, age: int, etudes: str):
        super().__init__(nom, age)
        self.etudes = etudes
    
    def SePresenter(self):
        super().SePresenter()
        print("Je suis étudiant en " + self.etudes)

# --- UTILISATION ---
liste_personnes = [Personne("Jean", 30), 
                   Personne("Paul", 15),
                   Personne("Zoe", 20)]

# Personne.ESPECE_ETRE_VIVANT = "Mutant"

for personne in liste_personnes:
    personne.SePresenter()
    personne.AfficherInfosEtreVivant()
    print()

chat1 = Chat()
chat1.AfficherInfosEtreVivant()

etudiant = Etudiant("Samir", 19, "Informatique")
etudiant.SePresenter()