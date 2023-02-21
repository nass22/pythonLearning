personne = {"nom" : "Mélanie", "age" : 25, "taille": 1.60}

# print(personne)
# print(personne['nom'])

personnes_dict = {
    "Mélanie": (25, 1.60),
    "Paul": (32, 1.80),
    "Jacques": (47, 1.74),
    "Arthur": (15, 1.65)
}

infos1 = personnes_dict("Jacques") # si le clé n'existe pas, il renvoit une erreur!

infos = personnes_dict.get("Jacques") # Le get permet de gérer les erreurs. Si il ne trouve pas la clé, il return none

print(infos)