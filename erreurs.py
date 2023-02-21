#GERER LES ERREURS EN PYTHON (try except):

age = input("Quel âge avez-vous?")

try: 
    age_prochain = int(age) + 1
except ValueError: 
    print("Erreur")
else: 
    print('L\'année prochaine vous aurez: ' + str(age_prochain) + "ans.")
