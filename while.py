#LA BOUCLE WHILE:
"""
n = 0


while n < 10:
    print("La valeur de n: " +str(n))
    n= n+1
"""

#Exercice 2
# mdp = ""

# while not mdp == "TEST":     #tant que mdp n'est pas = à TEST alors demander le mdp
#     mdp = input("Quel est votre mot de pass?")
    
# print("Mdp correct! Bien joué!")

#Exercice 28: forcer à rentrer un nom:

nom = input("Quel est votre nom?")

while nom == "":
    nom = input("Quel est votre nom?")

print("Votre nom est: " +nom)