# SECTION 9
# EXERCICE 3

import random
import time
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def sequence():
    print("Bienvenue dans le jeu du Simon")
    print("")
    score = 0
    sequence_base = str(random.randint(1000, 9999))
    print(f"Retenez cette séquence: {sequence_base}")
    time.sleep(3)
    clear_screen()
    sequence_user = input("Votre réponse: ")
    print("")

    while sequence_base == sequence_user:
        print('Réponse correct!')
        print("")
        score += 1
        
        random_number = str(random.randint(0,9))
        sequence_base = f"{sequence_base}{random_number}"
        print(f"Retenez cette séquence: {sequence_base}")
        time.sleep(3)
        clear_screen()
        sequence_user = input("Votre réponse: ")
        print("")
        
    print(f"Dommage, vous vous êtes trompé! La séquence était: {sequence_base}")
    print(f"Votre score est de: {score}")
 
sequence()

