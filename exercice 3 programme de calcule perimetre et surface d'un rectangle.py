longueur = float(input("veuillez saisir la longueur du rectangle : "))
largeur  = float(input("veuillez saisir la largeur du rectangle : "))
surface= longueur*largeur
perimetre=(longueur+largeur)*2

print("la surface du rectangle fait ",format(surface,".2f") ,"et le perimetre fait ", format(perimetre,".2f")  )