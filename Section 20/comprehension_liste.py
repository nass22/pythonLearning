# 132
# Compréhensions de listes

noms = ["Sabrina", "Camélia", "Naya", "Samir"]

longeurs_noms = []

for nom in noms:
    longeurs_noms.append(len(nom))

# print(longeurs_noms)
# Output: [7, 7, 4, 5]

longeurs_noms2 = [len(nom) for nom in noms]
# print(longeurs_noms2)
# Output: [7, 7, 4, 5]

longeurs_noms3 = [len(nom) for nom in noms if len(nom) < 7]
# print(longeurs_noms3)
# Output: [4, 5]

longeurs_noms4 = [len(nom) if len(nom) < 7 else 0 for nom in noms]
# print(longeurs_noms4)
# Output: [0, 0, 4, 5]

nom_avec_i = [nom for nom in noms if "i" in nom]
# print(nom_avec_i)

a = [i for i in range(5) if (i//2)*2 == i]
# print(a)
# Output: [0, 2, 4]

b = [True if (i//2)*2 == i else False for i in range(5)]
# print(b)
# Output: [True, False, True, False, True]

c = [(i, True if (i//2)*2 == i else False) for i in range(5)]
print(c)
# Output: [(0, True), (1, False), (2, True), (3, False), (4, True)]
