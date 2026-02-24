# importation des module
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage

#dictionnaire de couleur
couleur = {"neuro":"#252726",
           "purple":"#800080",
           "white":"#ffffff"
           }

#parametres de l'ecran
app=Tk()
app.title('MARMITE D\'ORE')
app.geometry('400x680')
app.config(bg='gray38')
# app.iconbitmap("icone.ico")
app.resizable(0,0)

# definition de nos fonction switch(on met global devant une 
# variable dans une fonction pour dire qu'on la declarer a lexterieur de la fonction)
def switch():
    global btnetat
    if btnetat is True:
        # creation de fermerture animer
        for x in range(150):
            navbarelateral.place(x=-x,y=0)
            topframe.update()
        #resset des couleur tt cequi est deriere ne doit pas bouger
        bannertext.config(fg='purple')
        acceuitexte.config(bg=couleur['purple'])
        topframe.config(bg=couleur['purple'])
        app.config(bg='gray30')
        btnetat=False
    else:
        for x in range(-150,0):
            navbarelateral.place(x=x,y=0)
            topframe.update()
            btnetat=True
         


# creation de fermerture
#creation doiuverture


#parametrage du switch
btnetat=False

# chargement image navbar
navicon=PhotoImage(file='menu.png')
closeicon=PhotoImage(file='close.png')
imgfont=PhotoImage(file='background.png')


#def barre de top
topframe =tk.Frame(app,bg=couleur['purple'])
topframe.pack(side="top",fill=tk.X)

#texte de la barre
acceuitexte=tk.Label(topframe,text="RESTO PRESTO",
                     font='ExtraCondensed 15',
                     bg=couleur['purple'],
                     fg=couleur['white'],height=2,padx=20)
acceuitexte.pack(side="right")

#baner texte image et image de font
can=Canvas(app,width=600,height=600)
can.create_image(0,0,anchor=NW,
                 image=imgfont)
can.pack()

# texte centrer
bannertext=tk.Label(app,text="RESTAURANT \nDEBADY",font='ExtraCondensed 15',
                    fg='purple')
bannertext.place(x=120,y=600)

#navbar icone
navbarbtn=tk.Button(topframe,image=navicon,bg=couleur['purple'],padx=20,bd=0,
                    activebackground=couleur['purple'],
                    command=switch)
navbarbtn.place(x=10,y=10)

#barre laterale
navbarelateral=tk.Frame(app,bg="gray30",width=150,height=300)
navbarelateral.place(x=0,y=0)
tk.Label(navbarelateral,font='ExtraCondensed 15',bg=couleur['purple'],fg='black',width=300,height=2,padx=20).place(x=0,y=0)
Y=80

# option navbare laterale
option =["Acceuil","Page","Profil","Parametre","Aide"]


#position element navbar
for i in range(5):
    tk.Button(navbarelateral,text=option[i],font='ExtraCondensed 15',bg='gray30',fg=couleur['white'],activebackground='gray30',bd=0).place(x=10,y=Y)
    Y=Y+40


#confug btn close
fermebtn=tk.Button(navbarelateral,image=closeicon,bg=couleur['purple'],activebackground=couleur['purple'],padx=0,command=switch)
fermebtn.place(x=120,y=10)
#afficher en permanance
app.mainloop()