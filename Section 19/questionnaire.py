# 120: exercice

# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

'''
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
'''


def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    global score
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(choix)):
        print(f" {i+1}: {choix[i]}")

    print()
    reponse = int(input(f"Votre réponse (entre 1 et {len(choix)}): "))
    reponse = choix[reponse-1]
    if reponse == bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        
    print()


score = 0


question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)


print("Score final :", score)
