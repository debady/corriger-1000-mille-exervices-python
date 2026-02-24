#          les dictionnaire permets de stocker des donne"
#          il fonctinne avec une CLE 'nom de la clef' est sa valeur =sa valeurs
#         b={}
#         b=[a]
#         print(b)
#         a=input("saisir quelque chose ")
#          pour supprimer on fait b.pop('nom de la clef')
#          remener les tuple print(b.items())
#         afficher les tout les cles print(b.keys())
#         afficher les tout valeurs print(b.valeurs())
#         print(type(b))
#         print(dir(b))
#          remplacer une cle b['papaye']=b.pop('kiwi')



b={}
b['orange']=40
b['crise']=500
b['kiwi']=66
b['mangue']=30
b['pasteque']=888
b['NOM']='david'
for (a,i) in b.items():
    print("je suis monsieurs  ",a,"qte",b)
b.pop('mangue')
b['papaye']=b.pop('kiwi')
b.keys()
print(b.keys())
print(b.values())
print(b)
print(b.items())
tab=[]
tab.append(b)
import os 
os.chdir("c:\\cours_de_fichiers")
open("file.txt","a")
a=open("file.txt","w")
a.write(tab)
a.close()