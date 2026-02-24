#-----------------------------
# Ecrire un programme python qui demande le nom de l'utilisateur
# et son sa date de naissance puis le programme affiche
# Bonjour + son Nom vous êtes né en + Date de naissance donc vous avez + son age 
#-----------------------------


VarNom = input('veuillez saisir votre nom :...')
VarAnneeNaisse = int(input('veuillez saisir votre date de naissance :..'))

calculAge = 2024 - VarAnneeNaisse

print('\nBonjour ',VarNom,' bienvenue ! vous êtes né en ',VarAnneeNaisse,' donc vous avez ',calculAge,' ans \n\n')
print(f'\nBonjour {VarNom} bienvenue ! vous êtes né en {VarAnneeNaisse} donc vous avez {calculAge} ans \n')