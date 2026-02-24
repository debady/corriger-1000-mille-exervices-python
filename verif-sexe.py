#---------------------
#PROGRAMME QUI DEMANDE LE NOM ET 
#LE GENRE  DE L'UTILISATEUR
# PUIS  LE RPOGRAMME LUI AFFICHE UN PROGRAMME PERSONNALISER AVEC 
# SON NOM + SON GENRE 
#----------------

print('Bonjour et bienvenue \n')
name = input('Entrez votre nom :')
genre = input('Quel est votre genre :')
print('\n')

if(genre== 'homme'):
    print('bonjour Monsieur',name)
elif (genre == 'femme'):
    print('Bonjour Madame ',name)
else:
    print('Bienvenue', name)
    print('vous n\'avez pas défini votre genre !')