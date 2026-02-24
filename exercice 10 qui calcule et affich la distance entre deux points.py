import math
nbr=int(input("veuillez saisir un nombre a mettre sous la racine carrée : "))
xa=int(input("veuillez saisir les coordonnée xa du points A: "))
xb=int(input("veuillez saisir les coordonnée xb du points A: "))
ya=int(input("veuillez saisir les coordonnée ya du points B: "))
yb=int(input("veuillez saisir les coordonnée yb du points b: "))
somme=(ya-xa)**2+(yb-xb)**2
racine=math.sqrt(somme)
print("la racine carrée de  ", nbr,"est ", math.sqrt(nbr))
print("la disatnce entre le points A et le points B est ",format(racine,".2f") )
