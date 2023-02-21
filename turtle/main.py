# SECTION 5
import turtle

def escalier(taille, marche):
    
    for i in range(0, marche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)
    
def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)
t = turtle.Turtle()

def carres(taille_depart, nb):
    for i in range(0, nb):
        carre((i+1)*taille_depart)
carres(50, 4)

turtle.done()