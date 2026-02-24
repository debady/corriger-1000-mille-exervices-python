# les importations
import tkinter as tk
from tkinter import *
import random as rd

# définition de la fénêtre
app=tk.Tk()
app.title('JEUX DE DEVINETTE DE NOMBRE')
app.geometry('200x280')
app.configure(bg='gray')
app.resizable('0x0')

#---------les variables
nbre_deviner =rd.randrange(100,500)
var_Take_Saisir =int()
print(nbre_deviner)

nbre_chance=tk.IntVar(app,rd.randrange(10,11))
#--------- fin les variables

#Fonction principale
def Traitement():
    var_Take_Saisir = int(Entry_user.get())
    if var_Take_Saisir>nbre_deviner:

        label_resultats.config(text='{}'.format(Entry_user.get()+' est trop grand'))
        label_nbre_chance.config(text=nbre_chance)

        var_tempo = nbre_chance.get()
        var_tempo-=1
        nbre_chance.set(var_tempo)

    elif var_Take_Saisir<nbre_deviner:
        label_resultats.config(text='{}'.format(Entry_user.get()+' est trop pétit'))
        label_nbre_chance.config(text=nbre_chance)

        var_tempo = nbre_chance.get()
        var_tempo-=1
        nbre_chance.set(var_tempo)

    elif var_Take_Saisir==nbre_deviner:
        label_resultats.config(text='{}'.format(Entry_user.get()+' est correct Bravo !'))
        label_nbre_chance.config(text=nbre_chance)
        
        var_tempo = nbre_chance.get()
        var_tempo-=1
        nbre_chance.set(var_tempo)

    else:
        label_resultats.config(text='{} {}'.format(Entry_user.get()+' Une erreur s\'est produit !'))

def nouveau():
    global Entry_user

    Entry_user.delete(0,END)
    label_resultats.config(text='')  

lab_nbre_affiche = Label(app,text='VOUS AVEZ 10 CHANCES\n POUR TROUVER LE BON NOMBRE\n PRIT ENTRE 100 ET 500')
lab_nbre_affiche.place(x=5,y=40)

label_nbre_chance = Label(app,text='Reste Nbre chance :')
label_nbre_chance.place(x=30,y=94)

label_nbre_chance = Label(app,textvariable=nbre_chance)
label_nbre_chance.place(x=140,y=94)

label_message = Label(app,text='saisir ici')
label_message.place(x=10,y=120)

Entry_user=Entry(app)
Entry_user.place(x=60,y=120)

btn_soumettre= Button(app,text='Deviner',background='green',command=Traitement)
btn_soumettre.place(x=40,y=150)

btn_new= Button(app,text='New',background='orange',command=nouveau)
btn_new.place(x=100,y=150)

label_resultats= Label(app,textvariable='')
label_resultats.place(x=50,y=194)

Btn_Fermer = Button(app,text='FERMER',command=quit,fg='red')
Btn_Fermer.place(x=75,y=250)

app.mainloop()