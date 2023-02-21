# 127
# Tris: sort et sorted

def tri_longueur_caracteres(nom):
    return len(nom)

noms = ["Sabrina", "Camélia", "Naya", "Samir"]

# noms.sort()
# Output : ['Camélia', 'Naya', 'Sabrina', 'Samir']

# noms.sort(reverse=True)
# Output : ['Samir', 'Sabrina', 'Naya', 'Camélia']

#Tri par longeur caractère
# noms.sort(key=lambda nom : len(nom))
# Lambda permet d'écrire une fonction directement sans devoir en créer une!
# Output : ['Naya', 'Samir', 'Sabrina', 'Camélia']

# noms_tries = sorted(noms)
# Crée une nouvelle liste
# Output : ['Camélia', 'Naya', 'Sabrina', 'Samir']

# noms_tries = sorted(noms, reverse=True)
# Output : ['Samir', 'Sabrina', 'Naya', 'Camélia']

noms_tries = sorted(noms, key=tri_longueur_caracteres, reverse=True)
# On ne met pas les () après tri_longueur_caracteres car ici on appelle pas la fonction, c'est la notion de callback ici
# Tri_longeur_caracteres et lambda nom : len(nom) font la meme chose, mais lambda permet de ne pas réécrire une fonction
# Output : ['Sabrina', 'Camélia', 'Samir', 'Naya']


print(noms_tries)