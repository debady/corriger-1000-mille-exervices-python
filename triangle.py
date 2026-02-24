from turtle import *
from random import *

def polygone(taille, couleur):
    n = randint(1,11)  # Nombre de côtés (vous pouvez changer cela)
    print(n)
    angle = 360 / n
    color(couleur)

    for _ in range(n):
        forward(taille)
        left(angle)

# Exemple d'utilisation :
polygone(100, "green")
done()  # Pour afficher le dessin
