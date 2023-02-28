import requests
import json

#API REST
response = requests.get("https://codeavecjonathan.com/res/pizzas1.json")

if response.status_code == 200:
    response.encoding = "utf-8"  # permet de gérer les problèmes d'accents
    print(response.text)
    json.loads(response.text)
    print("Nombre de pizzas : " + str(len(json.loads(response.text))))
else:
    print("Vérifier que votre url soit correct!")
