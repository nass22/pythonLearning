# 231
# Lire les données en base de données

import sqlite3

con = sqlite3.connect("albums2.db")
curseur = con.cursor()

# curseur.execute('SELECT * FROM artiste')
# artistes = curseur.fetchall()
# print(artistes)

# for artiste in curseur.execute('SELECT * FROM artiste'):
#     print(artiste)

albums_cd = curseur.execute('SELECT titre FROM album a JOIN artiste ar ON a.artiste_id = ar.artiste_id AND ar.nom = "Celine Dion"').fetchall()

print(albums_cd)

con.close()