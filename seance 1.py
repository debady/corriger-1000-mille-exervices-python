
# resolution de la fenetre 
#



#   titre de la fenetre 

#app.title("ma premiere application ")

# fixer la position de l'ecran afin de ne plus bouger 
#app.resizable(0,0)

# METHODE d'affichage 
# pack
# grid()
# place()
# la couleurs fg"la couleurs"
# bg="la couleurs" pour la couleur de fond 
# les variables en tkinker 
# Intvar () entier 
# stringvar() chaine de caracteres
# doublevar () pour les float

import tkinter as tk 
app=tk.Tk()
app.title("ma premiere application ")
app.resizable(0,0)

lbl_1=tk.Label(app,text="bonjour IGL/RIT",fg="Blue")


app.mainloop()