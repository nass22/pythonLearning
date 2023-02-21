# 139
# Set

noms = ["Marie", "Paul", "Jean", "Marc", "Emilie", "Marie"]

set_noms = set(noms)
# set permet d'avoir une liste avec des valeurs uniques (sans doublons). On peut boucler dessus, mais il n'est pas indexé!

print(noms)
print(set_noms)

# Si on veut indexé le set, on doit ajouter list devant:
list_indexe = list(set(noms))

print(list_indexe[0])

