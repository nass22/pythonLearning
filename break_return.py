# Différence entre break & return

# Avec le return, on sort complètement de la fonction (voir fonction a()), tandis qu'avec le break le code qui suit s'exécute (voir fonction b())

# return ne s'applique que dans une fonction, tandis que le break peut-etre utilisé dans une simple boucle.


def a():
    print("Début de la fonction")
    for i in range(0,100):
        if i > 20:
            return
        print(i)
    print('Fin de la fonction')
    
def b():
    print("Début de la fonction")
    for i in range(0,100):
        if i > 20:
            break
        print(i)
    print('Fin de la fonction')

a()

''' 
OUTPUT: 

a:
Début de la fonction
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

b:
Début de la fonction
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
Fin de la fonction
''' 
