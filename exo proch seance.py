MOTDEPASSE =10
NOM ='nguessan'

saisirNom = input('Veuillez saisir votre nom :')
saisirMotdepasse = input('Veuillez saisir votre mot de passe :')

nbreEssai = 3
x=0
while nbreEssai>=0 and saisirNom!=NOM and saisirMotdepasse!=MOTDEPASSE:
    
    print('Nom ou mot de passe incorrect ,réessayer !')

    saisirNom = input('Veuillez saisir votre nom :')
    saisirMotdepasse = input('Veuillez saisir votre mot de passe :')


    if nbreEssai==0 and (saisirNom!=NOM or saisirMotdepasse!=MOTDEPASSE):
        print('vou n\'avez plus le droit')
        break
    

    nbreEssai=nbreEssai-1

if nbreEssai!=0 and saisirNom==NOM and saisirMotdepasse==MOTDEPASSE:
        print('Acceuil     Mise à jour')
        print('Consultation     sécurité\nQuitter')