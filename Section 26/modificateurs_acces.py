# 185
# Modificateurs d'accès: Public, private, protected
# Public: on peut y accéder depuis l'intérieur de la class mais aussi depuis l'extérieur
# Private: on peut l'utiliser seulement à l'intérieur de la class (__nom)
# Protected: accès depuis l'intérieur de la classe et des classes dérivés (_nom)

class Personne:
    def __init__(self, nom):
        # on passe self.nom en private ( __nom):
        self._nom = nom
    
    def se_presenter(self):
        print(f"Je m'appelle {self._nom}")

class Etudiant(Personne):
    def se_presenter(self):
        print(f"Je suis étudiant et je m'appelle {self._nom}")

personne1 = Etudiant("Jean")
.


personne1.se_presenter()