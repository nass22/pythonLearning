import requests

response = requests.get("https://codeavecjonathan.com/res/programmation.txt")

if response.status_code == 200:
    response.encoding = "utf-8" # permet de gérer les problèmes d'accents
    print(response.text)
else :
    print("Vérifier que votre url soit correct!")