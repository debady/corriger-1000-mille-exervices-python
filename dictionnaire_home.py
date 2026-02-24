i=0
nbre_phrase=int(input("combien de phrase voulez vous enter ? :"))
while i<nbre_phrase:
    print("veuillez saisir la ",i+1," eme phrase ")
    phrase=input()
    open("dictionnaire_pour_phrase.txt","a")
    c="\n"+phrase
    a=open("dictionnaire_pour_phrase.txt","a")

    a.write(c)
    a.close()
    i=i+1
    
