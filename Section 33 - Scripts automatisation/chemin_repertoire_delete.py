# 225 - Chemins, répertoires et suppression
import os.path

# afin de gérer les chemins en fonction de l'OS, on va utiliser os.path.join()
# os.path.join("file", "fichier_a_delete.txt") = "file/fichier_a_delete.txt"
# si il y a des sous-répertoires: ("file, "sous-repertoire", "fichier_a_delete.txt")

filename = os.path.join("file", "fichier_a_delete.txt")

if os.path.exists(filename):
    print("Le fichier existe!")
else:
    print("Le fichier n'existe pas!")

# Pour créer un dossier, on utilise: os.mkdir("fichier")

# os.mkdir("fichier")
# os.rmdir("fichier") #supprime un dossier 