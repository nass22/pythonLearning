# SECTION 9 
# EXERCICE 2

import time

def cooking(minutes, secondes):
    cuisson_minutes = int(minutes)
    cuisson_secondes = int(secondes)
    time_secondes = (cuisson_minutes*60)+cuisson_secondes
    
    count = time_secondes
    
    while count > 0:
        min_remaining = count//60
        sec_remaining = count-min_remaining*60
        
        print(f"Temps restant: {min_remaining:02d}min et {sec_remaining:02d}sec", end="", flush=True)
        for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)
            
            count -= 1
        print("")
    
    print("")
    print("Fin de cuisson")

def cooking_time_choice():
    print('Choississez votre temps de cuisson:')
    print("Oeuf à la coque:  1")
    print("Oeuf mollet:  2")
    print("Oeuf dur:  3")
    print("")
    
    choice = ""
    
    while not choice == "1" or choice == "2" or choice == "3":
        choice = str(input("Votre choix: "))
        
        match choice:
            case "1":
                cooking(1,0)
            case "2":
                cooking(6, 0)
            case "3":
                cooking(10, 0)
            case _:
                print("Choississez une des 3 propositions SVP!")
                print("")
        
cooking_time_choice()

