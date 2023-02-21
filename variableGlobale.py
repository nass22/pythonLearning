age = 0

def demander_age():
    global age #On précise global car aussi non il ne trouve pas la variable
    while age == 0:
        age_str = input('Quel est votre âge?')
        try:
            age = int(age_str)
        except:
            print('Erreur: vous devez entrer un nombre!')
        
demander_age()
print('Votre age est de: ' + str(age))