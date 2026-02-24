from tkinter import *
from tkinter import simpledialog

def lire_texte_saisi():
    texte_saisi = simpledialog.askstring("Saisie de texte ?", "Entrez votre texte :")
    if texte_saisi:
        print(f"Vous avez saisi : {texte_saisi}")
    else:
        print("Aucun texte saisi.")

# Création de la fenêtre principale
app = Tk()
app.title("Lecteur de texte")
app.geometry('400x400')

# Création d'un bouton pour lancer la saisie
bouton_saisie = Button(app, text="Saisir du texte ?", command=lire_texte_saisi)
bouton_saisie.pack()

# Lancement de la boucle des événements
app.mainloop()
