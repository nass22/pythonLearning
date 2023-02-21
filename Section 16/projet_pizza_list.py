
pizzas = ["4 fromages", "tonno", "végétarien", "margherita"]
vide = ()

def afficher_pizzas(collection):
    
    if not collection: 
        print("AUCUNES PIZZAS")
    else:
        print(f"----- LISTES DES PIZZAS ({len(collection)}) -----")
        for i in collection:
            print(i)
    
        print()
        print(f"La première pizza est: {collection[0]}")
        print(f"La dernière pizza est: {collection[-1]}")


def ajouter_pizza():
    pizza_user = input("Ajouter une pizza:")
    if pizza_user != "":
        if pizza_user in pizzas:
            print("Erreur la pizza existe déjà!")
        else:
            pizzas.append(pizza_user)
    print()

ajouter_pizza()
afficher_pizzas(pizzas)