from bs4 import BeautifulSoup

f = open("recette.html", "r")
html_content = f.read()
f.close()

body = BeautifulSoup(html_content, 'html.parser')

titre_h1 = body.find("h1")

description = body.find("p", class_="description")

# description = body.find("p", {"class": "description"})

# print(description) # récupère la balise html

# print(description.text) # récupère le texte de la balise html
# print(description.get_text()) # récupère le texte de la balise html

list_div_centre = body.find_all("div", class_="centre")

p_description = list_div_centre[1].find("p", class_="description")

# print(p_description.text)

# Exercice récupérer la balise img et son src

img = body.find("img")

print(img["src"])




