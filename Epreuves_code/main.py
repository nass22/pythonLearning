def convertisseur():
    pouce = 2.54
    cm = 0.394
    question = 0
    
    while not question == 1 or question == 2:
        question = str(input("Convertisseur: TAPEZ 1 pour cm -> pouce / TAPEZ 2 pour pouce -> cm / TAPEZ exit pour quitter: "))
        
        if question == "1":
            value = float(input("Entrez votre mesure en cm: "))
            result = round(value * cm,2)
            
            print(f"{value} cm donne {result} pouce(s)")
        elif question == "2":
            value = float(input("Entrez votre mesure en pouce(s): "))
            result = round(value * pouce, 2)
            
            print(f"{value} pouce(s) donne {result} cm")
        elif question == "exit":
            break
        else:
            print('ERROR: Vous devez choisir entre 1 OU 2!')
            
convertisseur()