# SECTION 12
# EXERCICE 90


questions_reponses = (
    ("France", "Nantes", "Marseille", "Paris", "Cannes", "C"),
    ("Belgique", "Mons", "Bruxelles", "Liège", "Bruges", "B"),
    ("Suisse", "Bâle", "Genève", "Zurich", "Berne", "D"),
    ("Canada", "Ottawa", "Toronto", "Quèbec", "Vancouver", "A")
)

def questionnaire(questions_reponses):
    score = 0
    for i in questions_reponses:
        print("Quel est la capitale de ce pays:", i[0], "?")
        print("A -", i[1])
        print("B -", i[2])
        print("C -", i[3])
        print("D -", i[4])
        print()
        response = input("Votre réponse: ")
        
        if response.upper() == i[5]:
            print("Bonne réponse!")
            print()
            score +=1
        else:
            print("Dommage, la bonne réponse était:", i[5])
            print()
    print("Bien joué, votre score est de:", score,"/", len(questions_reponses))

questionnaire(questions_reponses)