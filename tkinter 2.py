# pour la surface 

import tkinter as tk
import random as rd

# pour le game 

import random
choix=random.randint(100, 500)

nbre_tentative=10   
victoire_gamer=0
i=nbre_tentative



app=tk.Tk()

app.geometry("500x200+100+100")
app.title("NGUESSAN_DAVID_DEBADY")

a=tk.IntVar(app,rd.randint(100, 500))

def init():
    e=rd.randint(100, 500)
    a.set(e)

def incre():
    d=a.get()
    d+=1
    a.set(d)


def decre():
    c=a.get()
    c-=1
    a.set(c)


# demander le nom du joueur 

nom_joueur=input("veuillez saisir votre nom  d'il vous plait : ")
print(nom_joueur," veuillez saisir votre coup")
while nbre_tentative>0:
    coup_gamer=input()
    coup_gamer=int()
    nbre_tentative-=1
    
    if coup_gamer>choix:
        print("vore nombre est grande")
        
    elif coup_gamer<choix:
        print("votre nombre est petite ")
    else:
        break
if nbre_tentative==0:
    print("houp nombre tentative epuisé c'etais ",choix)
else:
    print("bravo vous avez trouvez ",choix ,"au ",10-nbre_tentative," eme essaie !")       
        
    
    

lbl_1=tk.Label(app,textvariable=a)
lbl_1.grid()


btn_initialiser=tk.Button(app,text="INITIALISATIEON",command=init)
btn_initialiser.grid()

lab_nouvel=tk.Label(app,text="la nouvelle valeurs est : ",textvariable=init)
lab_nouvel.grid()


btn_increm=tk.Button(app,text="incrementé",command=incre)
btn_increm.grid()

lab_nouvel=tk.Label(app,text="la nouvelle valeurs est : ",textvariable=a)
lab_nouvel.grid()


btn_decre=tk.Button(app,text="decrementé",command=decre)
btn_decre.grid()

lab_nouvel=tk.Label(app,text="la nouvelle valeurs est : ",textvariable=a)
lab_nouvel.grid()










app.grid()
app.mainloop()