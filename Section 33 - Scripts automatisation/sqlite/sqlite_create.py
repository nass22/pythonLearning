# 229
# Création de la table SQLITE

import sqlite3

con = sqlite3.connect("albums2.db")
curseur = con.cursor()

curseur.execute("""CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);""")
    
curseur.execute("""CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    annee_sortie INTEGER);""")

curseur.execute('INSERT INTO artiste (nom) VALUES ("Michael Jackson");')
mj_id = curseur.lastrowid

curseur.execute('INSERT INTO artiste (nom) VALUES ("Celine Dion");')
cd_id = curseur.lastrowid

curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ('+ str(mj_id) +', "Thriller", 1983), (1, "Bad", 1987);')

curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ('+str(cd_id) +', "Falling into You", 1996), (2, "Let\'s Talk About Love", 1997);')

con.commit()
con.close()