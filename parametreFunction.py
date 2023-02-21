def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input('Quel est ton nom?')
    return reponse_nom


age = 0

def demander_age(nom_personne):
    global age
    while age == 0:
        age_str = input(nom_personne + " quel est votre âge?")
        try:
            age = int(age_str)
        except:
            print('Erreur: vous devez entrer un nombre!')
    return age

def afficher_inforamtions_personne(nom_personne, age):
    print(nom_personne + ' vous avez: ' + str(age) + " ans")



nom = demander_nom()
age = demander_age(nom)

afficher_inforamtions_personne(nom, age)
