# SECTION 11
# EXERCICE 88

user_choice = int(input("Choississez la table de multiplication à afficher: "))

def afficher_table_multi(n: int, min=1, max=10):
    if max < min:
        print("Votre max doit être plus grand que le min!")
        return                      #permet de ne pas executer le reste du code!
    else:
        for i in range(min, max+1):
            result = i*n
            print(f"{i}x{n} = {result}")
        
afficher_table_multi(user_choice)