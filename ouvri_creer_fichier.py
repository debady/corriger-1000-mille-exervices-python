import os 
os.getcwd()
os.chdir("c:\\cours_de_fichiers")
a=open("mardi.txt","a+")
a.write("NOM: N'guessan \n")
a.write("PRENOM:  Kouadio David \n")
a.write("PSEUDO:Debady chatu \n")
a.write(" \n")
a.close()

with open("mardi.txt","a+") as file:
    file.write("trop bon jolie \n")
    file.write("trop bon  \n")
    file.write("trop bon vrai \n")    