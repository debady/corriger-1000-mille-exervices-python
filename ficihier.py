import os 
os.getcwd()
os.chdir("c:\\ALGEBRE")
a=open("double.txt","a")
a.close()

nbre=int(input(("combien de note : ")))
x=0
while x<nbre:
    print("veuillez saisir la ",x+1,"eme note ")
    note=float(input())
    note=str(note)
    a.write("\n"+note)
    x=x+1