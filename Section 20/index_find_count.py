# 131
# Index, find, count

noms = ["Sabrina", "Camélia", "Naya", "Samir", "Sabrina"]

# print(noms.index("Samir"))
# Output: 3

# print(noms.index("Samir", 1, 5))
# index(value, indice départ, indice fin)
# Output: 3

# print(noms.count("Sabrina"))
# Output: 2

a = "Jean-Martin-Toto"

i = a.find("Martin")
# Output: 5

j = a.find("martin")
# Output: -1
# return -1 quand l'élément n'existe pas dans la liste

print(j)

