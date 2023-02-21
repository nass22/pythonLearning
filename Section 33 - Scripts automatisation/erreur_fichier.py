# 224 - Erreur fichier absent

# FICHIER QUI N'EXISTE PAS

# try: 
#     f = open("fichier_qui_n_existe_pas.txt", "r")
# except:
#     print("ERROR: Votre fichier n'existe pas!")
# else:
#     texte = f.read()
#     print("CONTENU DU FICHIER: \n")
#     print(texte)
#     f.close()

import os.path

# FICHIER QUI EXISTE

""" try: 
    f = open("lire_texte.txt", "r")
except:
    print("ERROR: Votre fichier n'a pu être lu")
else:
    texte = f.read()
    print("CONTENU DU FICHIER: \n")
    print(texte)
    f.close() """

# SAVOIR SI UN FICHIER EXISTE OU NON:
# os.path.exists() peut s'utiliser pour un fichier mais aussi sur un dossier

filename = "lire_texte.txt"
if os.path.exists(filename):
    print("Le fichier existe!")
else:
    print("Le fichier n'existe pas!")

