from turtle import *

def polygone(taille, couleur):
    n = 10  # Nombre de côtés (vous pouvez changer cela)
    angle = 360 / n
    color(couleur)

    for _ in range(n):
        forward(taille)
        left(angle)

# Exemple d'utilisation :
polygone(100, "green")
done()  # Pour afficher le dessin
