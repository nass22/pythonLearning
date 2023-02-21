# 161, 162, 163, 164
# Liste de pizzas

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

pizzas = [
    Pizza("4 Fromages", 12.85, ("Gorgonzola", "Parmesan", "Mozzarella", "Fontin"), True),
    Pizza("Margherita", 9.89, ("Tomate", "Mozzarella", "Basilic")),
    Pizza("Végétarienne", 10.55, ("Tomate", "Aubergine", "Champignons", "Oignons"), True)
]

def tri(e):
    return e.ingredients

pizzas.sort(key=tri)



# for pizza in pizzas:
#     if "Tomate" in pizza.ingredients:
#         pizza.Afficher()

for pizza in pizzas:
    pizza.Afficher()
