# 136
# Exercice: "in" insensible à la casse

noms = ["Sabrina", "Camélia", "Naya", "Samir"]

def element_dans_liste(e, list):
    # new_list = []
    # for elem in list:
    #     new_list.append(elem.lower())
    
    new_list  = [elem.lower() for elem in list]
    
    if e.lower() in new_list:
        print(e, "est présent dans la liste")
    else:
        print(e, "n'est PAS présent dans la liste")
    


element_dans_liste("saMir", noms)