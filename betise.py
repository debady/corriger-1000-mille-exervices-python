from  tkinter import *

app=Tk()
app.geometry("800x600")
app.config(background="blue")
app.resizable(0,0)
app.title('david_fonction')



def commande():
    prendre.set("NOM :  {} NUMERO : 05 {} ".format(nom_client.get(),
                                          numero_client.get() ))
    
    


labelle_nom = Label(app,text="ENTREZ LE NOM :")
labelle_nom.place(x=0,y=0)

labelle_numero = Label(app,text="ENTREZ LE NUMERO :")
labelle_numero.place(x=0,y=70)

nom_client=StringVar()
numero_client=StringVar()

saisir_nom=Entry(app,textvariable=nom_client)
sair_numero=Entry(app,textvariable=numero_client)


saisir_nom.place(x=0,y=50)
sair_numero.place(x=0,y=100)







btn_affiche=Button(app,text="afficher tout",command=commande,bg="red")
btn_affiche.place(x=0,y=150)

label_operateur=Label(app,text="")
label_operateur.place(x=10,y=300)

label_prefix=Label(app,text="")
label_prefix.place(x=10,y=400)

prendre=StringVar()

rsultat=Label(app,textvariable=prendre)
rsultat.place(x=100,y=300)


app.mainloop()
