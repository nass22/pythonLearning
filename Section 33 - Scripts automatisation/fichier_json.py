# 226
# Manipuler les données au format JSON

import json

""" 
personne = {"nom": "Paul",
            "age" : 25,
            "amis" : ["Sophie", "Marie", "Jean"]}

# Sérialiser DATA -> TXT (json) = dumps
# Désérialiser TXT (json) -> DATA = loads

personne_serialize = json.dumps(personne)

print("JSON: " + personne_serialize)

f = open("fichier_json.txt", "w")
f.write(personne_serialize)
f.close() 
"""

#--------------------------------------------------------
# 
f = open("fichier_json.txt", "r")

donnees_json = f.read()
f.close()

personne = json.loads(donnees_json)
print(personne["nom"])