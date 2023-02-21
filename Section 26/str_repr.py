#183
# str et repr

# Version 1:

# class Personne:
#     def __init__(self, nom, age):
#         self.nom = nom
#         self.age = age
    
#     def afficherInfos(self):
#         print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")
        

# personne1 = Personne("Jean", 20)
# personne1.afficherInfos()

# print(personne1)
# # OUTPUT:   Je m'appelle Jean et j'ai 20 ans
# #           <__main__.Personne object at 0x000002688B68BFD0>

# -------------------------------------------------------------------------

# Version 2:

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def afficherInfos(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")
    
    # def __str__(self):
    #     return "STR"
    
    def __repr__(self):
        # return "Personne " + str(self.__dict__)
        # OU
        return __class__.__name__ + " " + str(self.__dict__) #__class__._name__ permet de récupérer le nom de la class

personne1 = Personne("Jean", 20)
personne1.afficherInfos()

print(personne1)
# OUTPUT: Personne {'nom': 'Jean', 'age': 20}