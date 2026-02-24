import os
os.chdir("c:\\fichiers")
n=input("combien de note voulez vous saisir ? "  )
n=int(n)
print("veuillez saisir le nom de l' etudiant ")
i=0
while i<0:
    nom=input()
    note=input("note:")
    c=nom+":"+note
    print(c)
    b=open("note.txt")     
    b.write(c)
    b.close()
    i=i+1
