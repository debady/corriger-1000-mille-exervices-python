# ----------------------------------------
# PROGRAMME PYTHON QUI PERMET 
# DE LIRE UN TEXTE QUE L'ON AURA SAISIR AVEC TKINTER
#-----------------------------------------------

import tkinter as tk
import pyttsx3

def lire_texte_saisi():
    texte_saisi = simpledialog.askstring("Saisie de texte", "Entrez votre texte :")
    if texte_saisi:
        print(f"Vous avez saisi : {texte_saisi}")
        # Initialisation du moteur de synthèse vocale
        engine = pyttsx3.init()
        engine.say(texte_saisi)
        engine.runAndWait()
    else:
        print("Aucun texte saisi.")

# Création de la fenêtre principale
app = tk.Tk()
app.title("Lecteur de texte")

# Création d'un bouton pour lancer la saisie
bouton_saisie = tk.Button(app, text="Saisir du texte", command=lire_texte_saisi)
bouton_saisie.pack()

# Lancement de la boucle des événements
app.mainloop()
