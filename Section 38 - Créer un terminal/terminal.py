import os
import subprocess


while True:
    cmd_user = input(os.getcwd() + " > ")

    if cmd_user == "exit":
        break
    
    cmd_split = cmd_user.split(" ")
    if len(cmd_split) == 2 and cmd_user[0] == "cd":
        try:
            os.chdir(cmd_split[1])
        except FileNotFoundError:
            print("Invalid directory")
    else:  
        # Popen: ancienne interface
        # run: executer une commande et attend une réponse
        result = subprocess.run(cmd_user, shell=True, capture_output=True, universal_newlines=True) 
        '''
        ls sur mac (à la place de dir)
        shell=True permet d'exécuter la commande en shell
        capture_output=True permet de récupérer les données de la commande
        universal_newlines=True dit de décoder de la meilleure manière le résultat
        '''

        print(result.stdout)
        print(result.stderr) # permet d'afficher les erreurs







