import copy
# 181
# Comparaison d'objets

# Version 1:

# class Personne:
#     def __init__(self, nom, age):
#         self.nom = nom
#         self.age = age
    
#     def afficherInfos(self):
#         print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")

# personne1 = Personne("Sabrina", 31)
# personne1.afficherInfos()
# personne2 = Personne("Sabrina", 31)
# personne2.afficherInfos()

# personne3 = personne1

# print(personne1 == personne2)
# # Output: FALSE car pour lui ce sont 2 objets différents même si les données sont les mêmes
# print(personne1 is personne2)
# # Output: FALSE car pour lui ce sont 2 objets différents même si les données sont les mêmes

# print(personne1 is personne3)
# # Output: TRUE car c'est le même objet

# -----------------------------------------------------------

# Version 2:

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def afficherInfos(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")
    
    def __eq__(self, other): # eq = equality -> permet de redéfinir l'égalité
        return self.nom == other.nom and self.age == other.age

# Exemple 1:

# personne1 = Personne("Sabrina", 31)
# personne1.afficherInfos()
# personne2 = Personne("Sabrina", 31)
# personne2.afficherInfos()


# print(personne1 == personne2)
# # Output: TRUE car on a redéfinit l'égalité! Si self.nom == other.nom and self.age == other.age alors return True
# print(personne1 is personne2)
# # Output: FALSE car pour lui ce sont 2 objets différents même si les données sont les mêmes

# print(personne1.__dict__)
# # Output: {'nom': 'Sabrina', 'age': 31} -> on obtient un dictionnaire

# print(personne1.__dict__ == personne2.__dict__)
# # Output: True

# ----------------------------------------------------------------

# Exemple 2:

# personne1 = Personne("Sabrina", 31)
# personne1.afficherInfos()

# personne2 = personne1
# personne1.nom = "Paul"
# personne2.afficherInfos()


# print(personne1 == personne2)
# # Output: TRUE car on a redéfinit l'égalité! Si self.nom == other.nom and self.age == other.age alors return True
# print(personne1 is personne2)
# # Output: TRUE car pour lui ce sont les mêmes objets

# print(personne1.__dict__)
# # Output: {'nom': 'Paul', 'age': 31} -> on obtient un dictionnaire

# print(personne1.__dict__ == personne2.__dict__)
# # Output: True

# ----------------------------------------------------------------

# Exemple 3:
# shallow copy / deep copy

personne1 = Personne("Sabrina", 31)
personne1.afficherInfos()

personne2 = copy.copy(personne1)
personne2.nom = "Paul"
personne2.afficherInfos()


print(personne1 == personne2)
# Output: False
print(personne1 is personne2)
# Output: FALSE

print(personne1.__dict__)
# Output: {'nom': 'Paul', 'age': 31} -> on obtient un dictionnaire

print(personne1.__dict__ == personne2.__dict__)
# Output: True

# -----------------------------------------------------------

# Version 3:

class Personne:
    def __init__(self, nom, age, amis):
        self.nom = nom
        self.age = age
        self.amis = amis
    
    def afficherInfos(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")
    
    def __eq__(self, other): # eq = equality -> permet de redéfinir l'égalité
        return self.nom == other.nom and self.age == other.age

personne1 = Personne("Sabrina", 31, ["Samir", "Camélia", "Naya"])
personne1.afficherInfos()

personne2 = copy.deepcopy(personne1) #deepcopy permet de copier tous les éléments 
# personne2.nom = "Paul"
personne1.amis[0] = "Patrick"
personne2.afficherInfos()


print(personne1 == personne2)
# Output: False
print(personne1 is personne2)
# Output: FALSE

print(personne2.__dict__)
# Output: {'nom': 'Sabrina', 'age': 31, 'amis': ['Samir', 'Camélia', 'Naya']}

print(personne1.__dict__)
# Output: {'nom': 'Sabrina', 'age': 31, 'amis': ['Patrick', 'Camélia', 'Naya']}

print(personne1.__dict__ == personne2.__dict__)
# Output: True