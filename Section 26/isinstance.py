# 178

class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
        
        if not isinstance(age, int):
            print("L'âge doit être de type INT")
    
    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}")
        if self.age > 0:
            print(f"L'an prochain j'aurai: {self.age+1} ans")


personne = Personne("Jean", "32")
personne.AfficherInfos()