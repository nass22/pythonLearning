# Exercice 32: fonction demander un nom:

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input('Quel est ton nom?')
    return reponse_nom

nom = demander_nom()

print('Votre nom est: ' + nom)