# SECTION 7
import random

nb_min = 1
nb_max = 10
nb_question = 4
nb_boucle = 1
nb_points = 0

def question():
    global nb_boucle
    global nb_points
    
    
    while nb_boucle <= nb_question:
        random_nb1 = random.randint(nb_min, nb_max)
        random_nb2 = random.randint(nb_min, nb_max)
        operator = random.randint(0, 1)
    
        if operator == 0:
            operation = "+"
            result = int(random_nb1 + random_nb2)
        else: 
            operation = "*"
            result = int(random_nb1 * random_nb2)
            
        print(f"Question {nb_boucle}/{nb_question}")
        
        
        
        question = int(input(f"Calculez: {random_nb1} {operation} {random_nb2} : "))
        
        if question == result: 
            print("La réponse est correcte!")
            nb_points += 1
        else: 
            print("La réponse est incorrect!")
        
        nb_boucle += 1
        print()
    
    moyenne = int(nb_question/2)
    
    
    print(f"Résultat: {nb_points}/{nb_question}")
    
    
    if nb_points == 0:
        print("Révisez vos maths!")
    elif nb_points > moyenne:
        print("Excellent!")
    elif nb_points == moyenne:
        print("Pas mal")
    else:
        print("Peut mieux faire")
    
question()