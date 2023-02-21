# 165

class Pizza:    
    def __init__(self, nom: str = "", prix: float = 0, ingredients: str = "", vegetarien: bool = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarien = vegetarien

    def Afficher(self):
        veg_str = ""
        if self.vegetarien:
            veg_str = " (VEGETARIENNE)"
        print(f"PIZZA: {self.nom} - {self.prix}€ {veg_str}")
        print("Ingrédients:", '/'.join(self.ingredients))
        print()

class PizzaPersonnalisee(Pizza):
    PRIX_BASE = 7
    PRIX_INGREDIENT = 1.2
    dernier_numero = 1
    
    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisée " + str(self.numero), 0, [])
        self.Demander_ingredients()
        self.Calculer_prix()
    
    def Demander_ingredients(self):
        print(f"Ingredient pour la pizza numéro {self.numero}")
        while True:
            ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer): ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
    
    def Calculer_prix(self):
        nb_ingredients = len(self.ingredients)
        self.prix = (self.PRIX_BASE + (nb_ingredients*self.PRIX_INGREDIENT))
        

pizzas = [
    Pizza("4 Fromages", 12.85, ("Gorgonzola", "Parmesan", "Mozzarella", "Fontin"), True),
    Pizza("Margherita", 9.89, ("Tomate", "Mozzarella", "Basilic")),
    Pizza("Végétarienne", 10.55, ("Tomate", "Aubergine", "Champignons", "Oignons"), True),
    PizzaPersonnalisee(),
    PizzaPersonnalisee()
]

# def tri(e):
#     return e.ingredients

# pizzas.sort(key=tri)


# for pizza in pizzas:
#     if "Tomate" in pizza.ingredients:
#         pizza.Afficher()

for pizza in pizzas:
    pizza.Afficher()




