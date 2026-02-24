# importation 
from tkinter import *

# config fenetre
apk=Tk()
apk.title("fenetre apk")
apk.geometry("450x400")
# fonction---------

#fonct princip
def fonctPrincip():
    varRecupNom = str(textEntry.get())
    if varRecupNom=="":
        print("champs vide")
        lblAff.config(text="remplis les champs")
    else:
        print("Voir nom saisir !")
        lblAff.config(text="votre nom  {}".format(textEntry.get()))
#fonct remplacer
def new():
     print("saisisez le nouveau nom")
     global textEntry
     textEntry.delete(0,END)
     lblAff.config(text="")
    
#-------------
# declar var
varRecupNom = str()
# fin decla var ------------

#corps programme-------------------
lbl=Label(apk,text="NOM:")
lbl.place(x=5,y=40)

textEntry = Entry(apk)
textEntry.place(x=50,y=40)

btn= Button(text="validé",command=fonctPrincip)
btn.place(x=25,y=100)

btn= Button(text="nouveau",command=new)
btn.place(x=100,y=100)

btnquit= Button(text="finir",command=quit,bg="red")
btnquit.place(x=200,y=100)

lblAff = Label(apk,textvariable="")
lblAff .place(x=10,y=200)

#fin corps----------------------------------

apk.mainloop()