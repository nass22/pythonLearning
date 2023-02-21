age = int(input('Quel âge avez-vous?'))

if age < 10:
    print('Vous êtes enfant')
elif age == 17:
    print('Vous êtes presque majeur')
elif age == 18:
    print('Vous êtes tout juste majeur: félicitation')
elif age > 18 and age <= 60: #on peut simplifier cela en: 18 < age <= 60
    print('Vous êtes majeur')
elif age > 60:
    print('Vous êtes sénior')
else:
    print('Vous êtes mineur')