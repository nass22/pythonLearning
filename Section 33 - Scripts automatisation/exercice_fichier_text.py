fichier = open("exercice_txt.txt", "w")

for i in range(10):
    fichier.write(str(i+1)+"\n")

fichier.close()