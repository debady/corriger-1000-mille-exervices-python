def nombre_radiateur(longueur,largeur,hauteur):
    L=largeur
    l=longueur
    H=hauteur
    nr=(L*l*H)//8
    return nr
Longueur=int(input("veuillez saisir la longueur : "))
largeur=int(input("veuillez saisir la largeur : "))
hauteur=int(input("veuillez saisir la hauteur : "))
d=nombre_radiateur(longueur, largeur, hauteur)
print("if faut",d)