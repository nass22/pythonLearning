import requests

response = requests.get("https://codeavecjonathan.com/res/exemple.html")

if response.status_code == 200:
    response.encoding = "utf-8"  # permet de gérer les problèmes d'accents
    print(response.text)
else:
    print("Vérifier que votre url soit correct!")