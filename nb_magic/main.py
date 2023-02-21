# SECTION 6
import random

nb_min = 1
nb_max = 10
nb_magic = random.randint(1, 10)

"""
def ask_number(nb_min, nb_max):
    find_nb = 0
    nb_try = 3
    
    
        
    while not find_nb == nb_magic and nb_try > 0:
        try:
            find_nb = int(input(f"Trouvez le nombre magique entre {nb_min} et {nb_max} :"))
            
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez!")
        else:
            if find_nb < nb_min or find_nb > nb_max:
                print(f"ERREUR: le nombre doit être entre {nb_min} et {nb_max}. Réessayez:")
                
                find_nb = 0
            else:                    
                while find_nb != nb_magic:
                    nb_try -= 1
                    
                    if find_nb < nb_magic:
                        find_nb = int(input(f"Le chiffre est plus grand que votre proposition. Il vous reste: {nb_try} vie(s)! Réessayez:"))

                    elif find_nb > nb_magic:
                        find_nb = int(input(f"Le chiffre est plus petit que votre proposition. Il vous reste: {nb_try} vie(s)! Réessayez:"))
                
                if find_nb == nb_magic:
                        print(f"Bravo, vous avez trouvé le nombre magique: {find_nb}")

    print(f"Vous n'avez plus de vies! Le chiffre magique était: {nb_magic}")

                
ask_number(nb_min, nb_max)
"""
    

def ask_number(nb_min, nb_max):
    find_nb = 0
    nb_try = 3
    
    
        
    for i in range(0, nb_try):
        nb_try -= 1
        try:
            find_nb = int(input(f"Trouvez le nombre magique entre {nb_min} et {nb_max} :"))
            
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez!")
        else:
            if find_nb < nb_min or find_nb > nb_max:
                print(f"ERREUR: le nombre doit être entre {nb_min} et {nb_max}. Réessayez:")
                
                find_nb = 0
            else:                    
                while find_nb != nb_magic:
                    nb_try -= 1
                    
                    if find_nb < nb_magic:
                        find_nb = int(input(f"Le chiffre est plus grand que votre proposition. Il vous reste: {nb_try} vie(s)! Réessayez:"))

                    elif find_nb > nb_magic:
                        find_nb = int(input(f"Le chiffre est plus petit que votre proposition. Il vous reste: {nb_try} vie(s)! Réessayez:"))
                
                if find_nb == nb_magic:
                        print(f"Bravo, vous avez trouvé le nombre magique: {find_nb}")

    print(f"Vous n'avez plus de vies! Le chiffre magique était: {nb_magic}")

                
ask_number(nb_min, nb_max)