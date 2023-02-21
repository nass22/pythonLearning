# 137
# Exercice nombre total caractères

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

# Boucle for:
def nb_caractere_for():
    nb_caracteres = 0
    for nom in noms:
        nb_caracteres += len(nom)

    print(nb_caracteres)
    
# nb_caractere_for()


# Completion de liste:
longeur_noms = [len(nom) for nom in noms]
# print(sum(longeur_noms))


# Join
longeur = "".join(noms)
print(len(longeur))