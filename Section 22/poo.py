# 146,147
# Premiers pas en POO

class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        self.age = age
        if self.nom == "":
            self.DemanderNom()
        print("Constructeur", self.nom)

    def SePresenter(self):
        if (self.age == 0):
            print("Bonjour je m'appelle", self.nom)
        else:
            if self.EstMajeur():
                print("Bonjour je m'appelle", self.nom, ", j'ai", self.age, "ans et je suis majeur.")
            else: 
                print("Bonjour je m'appelle", self.nom, ", j'ai", self.age, "ans et je suis mineur.")

    def EstMajeur(self):
        # if (self.age >= 18):
        #     return True
        # return False
        return self.age >= 18

    def DemanderNom(self):
        self.nom = input(str("Quel est votre nom? "))
        

# personne1 = Personne("Jean", 30)
# personne1.SePresenter()

# personne2 = Personne("Paul", 15)
# personne2.SePresenter()

personne3 = Personne("Samir", 15)
personne3.SePresenter()

personne4 = Personne(age=22)
personne4.SePresenter()




# print("Nom:", personne1.nom)    