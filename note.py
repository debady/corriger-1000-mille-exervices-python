import os
os.chdir("c:\\1_PROGRAMME_PYTHON\_PROGRAMME_")
n=input("combien de note voulez vous saisir ? :" )
n=int(n)
i=0
while i<n:
    nom=input("nom de l'etudiants : ")
    note=input("note : ")
    c=nom+":"+note
    
    b=open("note.txt","a")
    b.write(c)
    b.close()
    i=i+1
print(c)