# 221 - Ouvrir, écrire, lire, fermer un fichier texte

f = open("mon_fichier.txt", "a")
# f.write("Helloo\n") # \n permet d'aller à la ligne

l = ["première ligne", "deuxième ligne", "troisième ligne"]

f.writelines("\n".join(l))
f.close()
