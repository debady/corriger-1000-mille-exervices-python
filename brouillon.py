# importation 
from tkinter import *

apk=Tk()
apk.title("fenetre apk")
apk.geometry("400x600")

# fonction
def fonctPrincip():
    print("foncnnionnel")
    

# declar var
#varRecupNom = str()

lbl=Label(apk,text="votre nom :")
lbl.place(x=100,y=100)

textEntry = Entry(apk)
textEntry.place(x=250,y=100)

btn= Button(text="validé",command=fonctPrincip)
btn.place(x=300,y=200)

lblAff = Label(apk,textvariable="")
apk.mainloop()