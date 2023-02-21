# 223 - Lire un fichier texte

f = open("lire_texte.txt", "r")

# text = f.readline()
# print(text)

for line in f:
    print(line)

f.close()