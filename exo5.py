tab = ['david',' kouadio','jean','akissi','jean','jack','franck','david','jean','paul']
nom=''

while nom!='FIN':
    nbreNom=0

    nom = input("veuillez taper un nom :")
    for i in range(len(tab)):
        
        if tab[i]==nom:
            nbreNom=nbreNom+1
            
    print(nbreNom)
