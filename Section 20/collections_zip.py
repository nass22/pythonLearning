# 138
# Collections: Zip


pizzas_nom = ("4 fromages", "Thonno", "Margherita")
pizzas_prix = (14, 13, 12)

noms_et_prix = list(zip(pizzas_nom, pizzas_prix))
# print(noms_et_prix)
# list permet d'indexer le tuple
# OUTPUT: [('4 fromages', 14), ('Thonno', 13), ('Margherita', 12)]

# for (nom, prix) in zip(pizzas_nom, pizzas_prix):
#     print(f"{nom} - {prix}€")
# OUTPUT: 4 fromages - 14€
#            Thonno - 13€
#        Margherita - 12€

# unzipped = list(zip(*noms_et_prix))
# print(unzipped)
# zip (*..) permet de recréer les 2 listes
# OUTPUT: [('4 fromages', 'Thonno', 'Margherita'), (14, 13, 12)]

# OU

pizza_nom, pizza_prix = list(zip(*noms_et_prix))
# print(pizza_nom)
# OUTPUT: ('4 fromages', 'Thonno', 'Margherita')
print(pizza_prix)
# OUTPUT: (14, 13, 12)