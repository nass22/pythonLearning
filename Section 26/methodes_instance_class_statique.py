# 184
# Méthodes d'instance, de classe et statiques

class Personne: 
    TYPE = "Humain"
    def __init__(self, nom):
        self.nom = nom 
    
    def se_presenter(self):
        print(f"Je m'appelle {self.formater_chaine(self.nom)} - " + self.TYPE)
    
    # méthode statique
    @staticmethod # staticmethod est un décorateur et va dire à la class de pas y insérer self
    def formater_chaine(a):
        return a[0].upper() + a[1:].lower()

    @classmethod # ici grâce à classmethod, on aura accès à la class avec le cls
    def methode_de_class(cls):
        print("Méthode de classe: " + cls.TYPE)

personne1 = Personne("jean")
personne1.se_presenter()

Personne.methode_de_class()