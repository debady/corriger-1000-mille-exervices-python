               # les importantion

import random
import tkinter as tk
import sqlite3



                # gestion de la fenetre

mini_projet=tk.Tk()
mini_projet.geometry("600x600+300+300")
mini_projet.title("GESTION DE BASE DE DONNEE ")
#mini_projet.iconbitmap('C:\\Users\\nguessan\\Desktop\\mini projet python\\Butterfly-PNG-Transparent-Photo.Butterfly-PNG-Transparent-Photo.png')
mini_projet.config(background="#94f7e6")
mini_projet.minsize(400,500)
mini_projet.maxsize(400,500)

textin=tk.StringVar() 
textinn=tk.StringVar()
david=tk.IntVar()
esther=tk.StringVar()
marc=tk.StringVar()



                        # champs des label affichage 

h= tk.Label(mini_projet, text="  Bienvenue dans la l'applicattion de gestion \nde mise a jour de la base de donnée des\n numeros de 8 chiffre a 10 ",bg="#ee339a" ,fg="#0a0600")
h.place( x=150,y=7) 

g = tk.Label(mini_projet, text= " nom ✔️ : " )
g.place( x=60,y=42)

l =tk. Label(mini_projet, text=" prenom ✨ : ")
l.place( x=60, y =80)

h= tk.Label(mini_projet, text=" telephone 🍊 : ")
h.place( x=60,y=120)

I = tk.Label(mini_projet, text=" @dresse mail ☢️ : ")
I.place( x=60,y=180)

 
              # champs des entrez saisir 
  
valeur1 =tk.Entry(mini_projet,width=20,textvar=textin)
valeur1.place( x=160,y=42)

lblresulta= tk.Label(mini_projet, text="veuillez entrer le nom à rechercher:")
lblresulta.place(x=5,y=400)

valeur2 = tk.Entry(mini_projet,width=20,textvar=textinn)
valeur2.place( x=160, y =80)
                  
valeur3 = tk.Entry(mini_projet,width=20,textvar=david)
valeur3.place( x=160,y=120)

valeur4 = tk.Entry(mini_projet,width=20,textvar=esther)
valeur4.place( x=170,y=180)


valeur5 = tk.Entry(mini_projet,width=20,textvar=marc)
valeur5.place(x=220,y=400)


boutton_quit =tk. Button(mini_projet, text="QUITTER",command=quit)
boutton_quit.place(x = 13, y= 450)



def insert():
    name1 = textin.get()
    prenom1 =textinn.get()
    tel = david.get()
    motpass = esther.get()
    conn = sqlite3.connect('david_python.db')
    
    with conn :
        cursor =conn.cursor()
        new_user = (cursor.lastrowid,name1,prenom1,tel,motpass)
        cursor.execute('INSERT INTO fn VALUES(?,?,?,?,?)',new_user)
        conn.commit()
        print("Operation d'enregistrement effectuée avec success !!!")
        conn.close()
boutton_qui =tk.Button(mini_projet, text="ENREGISTRER",command=insert)
boutton_qui.place(x = 150, y= 250)

textin=tk.StringVar()

textinn=tk.StringVar()
david=tk.StringVar()
esther=tk.StringVar()



def RECHERCHER():
    search = marc.get()
    connection = sqlite3.connect('david_python.db')
    cursor = connection.cursor()
    req = cursor.execute(f" SELECT * FROM fn WHERE new_user ='{search}'" )
    
    for row in req.fetchall():
        print("\n",row)
        connection.close()
boutton_qui =tk. Button(mini_projet, text="AFFICHER",command=RECHERCHER)
boutton_qui.place(x = 300, y= 450)
mini_projet.grid()
mini_projet.mainloop()






               # affichage et fermerture
mini_projet.grid()
mini_projet.mainloop()




import tkinter as tk
racine = tk.Tk()

label = tk.Label(racine, text="J'adore Python !")
bouton = tk.Button(racine, text="Quitter", fg="red",command=racine.destroy)

label.grid()
bouton.grid()

racine.grid()
racine.mainloop()


