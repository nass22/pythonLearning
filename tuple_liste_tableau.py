# Tuple () : immutable -> non modifiable - utilise moins de mémoire
# Liste [] : mutable -> rajouter/supprimer des éléments ou le modifier


# ----------TUPLES----------:
personnes = ("Camélia", "Sabrina", "Samir")

# for i in range(0, len(personnes)):
#     print(personnes[i])
    
# Ou plus simplement:

for i in personnes:
    print(i)
    

# ----------LISTES----------
personnes = ["Camélia", "Sabrina", "Samir"]
nouvelle_personne = "Martine"

personnes.append(nouvelle_personne)

del personnes[1]

print(personnes)

