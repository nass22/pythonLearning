# 154

# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
liste = []
nb_personne = int(input("Combien de personnes voulez-vous insérer? "))

for i in range(nb_personne):
    nom = input(f"nom de la personne {i+1} : ")
    liste.append(Personne(nom))

for personne in liste:
    personne.SePresenter()