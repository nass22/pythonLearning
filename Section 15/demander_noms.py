# SECTION 15 
# Exercice 104

def demander_nom():
    tab_noms = []
    nom = "0"
    
    while not nom == "":
        nom = input("Nom de la personne: ")
        if nom == "":
            break
        else:
            tab_noms.append(nom)
    
    print(tab_noms)
    
demander_nom()    