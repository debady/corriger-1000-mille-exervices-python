# apres avoir ajouter ce dont on voulais on fait suite \n
import os
os.getcwd()
os.mkdir("C:\\fireforx\Code - Python\python\mon_Docier")
os.chdir("C:\\fireforx\Code - Python\python")
open("message.txt","w") 
a=open("message.txt","a")
a.write("je suis au village nn \n")
a.write("bonjour\n")
a.close()

with open("porte.txt","a") as a:
    a=open("porte.txt","w")
    a.write("nguessan1\n")
    a.write("nguessan\n")