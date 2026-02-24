# les importations 

from tkinter import *
import tkinter.messagebox as messagebox

# resolution de l'ecran 

debady=Tk()
debady.geometry("1000x1000")
debady.title("projets_debady_python")
debady.configure(background="#94f7e6")
#debady.iconbitmap('image\mp.ico')
debady.resizable(False,False)

# les fonctions

def david():
    a=str(entry_number.get())
    x=0
    s=a[1]
    s=int(s)
    try:
        if s==0 or s==1 or s==2 or s==3:
            answer_label.config(text="MOOV-CI")
            answer_num_10.config(text="+225 01 {} " .format(entry_number.get()))       
            answer_prefix.config(text="NOUVEAU PREFIX 01 ")  
            entre_apropos_new.config(text="NOM : {}\nNUMERO 8 CHIFFRE  :{}\nOPERATEUR :{}\nNEW-NUMERO : +225 01 {}".format(entre_nom.get(),entry_number.get(),"MOOV-CI",entry_number.get()))

        
        
        elif s==4 or s==5 or s==6:
            answer_label.config(text="MTN-CI")
            answer_num_10.config(text="+225 05 {} " .format(entry_number.get()))   
            answer_prefix.config(text="NOUVEAU PREFIX 05 ")  
            entre_apropos_new.config(text="NOM : {}\nNUMERO 8 CHIFFRE :{}\nOPERATEUR :{}\nNEW-NUMERO : +225 05 {}".format(entre_nom.get(),entry_number.get(),"MTN-CI",entry_number.get()))
        
        elif s==7 or s==8 or s==9:
            
            answer_label.config(text="ORANGE-CI")  
            answer_num_10.config(text="+225 07 {} " .format(entry_number.get())) 
            answer_prefix.config(text="NOUVEAU PREFIX 07 ")  
            entre_apropos_new.config(text="NOM : {}\nNUMERO 8 CHIFFRE  :{}\nOPERATEUR :{}\nNEW-NUMERO : +225 07 {}".format(entre_nom.get(),entry_number.get(),"ORANGE-CI",entry_number.get()))

    
    except IndexError:
        nom=entry_number.get()
        numero = entre_nom.get()
        if (nom==""or numero==""):
            entre_nom.focus_set()
            entry_number.focus_set()
            messagebox.showerror(("attention inserer un nom"))
            answer_erreur.config(text="numero invalide")
        else:
            messagebox.showinfo("numero \nenregistre!!")
            answer_erreur.config(text="numero enregistrer \navec succes ! ")
            
        
        # fonction de nouvea saisir    
        
def delect():
        global answer_prefix
        global entry_number
        global entre_nom
        entry_number.delete(0,END)
        entre_nom.delete(0,END)
        
        
        # l'entete de la fenetre
    
debad=Label(debady,text="WELCOME TO APPLICATION PASS 8 NUMBER TO 10 ",font=("arial",15),bg="orange", fg="white")
debad.place(x=0,y=0,width=1000,height=50)


nom_client=StringVar()


lab_nom=Label(debady,text="NOM CLIENT : ",font=("arial",15),bg="white",fg="black")
lab_nom.place(x=150,y=80)

entre_nom=Entry(debady, font=("uppercase",18),fg="#2603a7")
entre_nom.place(x=380,y=80,width=200,height=30)

answer_erreur=Label(debady,text="",fg="#46e615",font=("arial",18))
answer_erreur.place(x=600,y=68,width=400,height=100)

# message de saisir le numero
lab_numero=Label(debady,text="NUMERO 8 CHIFFRE : ",font=("arial",15),bg="white",fg="black")
lab_numero.place(x=0,y=130)

#champs de saisir le numero 
entry_number=Entry(debady,font=("arial",18),fg="#2603a7")
entry_number.place(x=380,y=130,width=200,height=30)

# boutton d'envoi du numero
btn_numer=Button(debady,text="ENREGISTRER",command=david,font=("arial",15),bg="#46e615")
btn_numer.place(x=280,y=180,width=200,height=50)

# messange sur l'operateur
lab_operateur=Label(debady,text="OPERATEUR: ",font=("arial",15),bg="white",fg="black")
lab_operateur.place(x=10,y=290)

answer_label=Label(debady,text=" ",font=("arial",18),fg="#2603a7")
answer_label.place(x=0,y=330,width=265,height=150)

# logo mtn
#answer_logo_mtn=Label(debady,text=" ",font=("arial",18),fg="#2603a7")
#answer_logo_mtn.place(x=285,y=240,width=165,height=150)

#filename=PhotoImage(file="reseau/logo_mtn_b.png")
#answer_logo=Label(debady,image=filename)
#answer_logo.place(x=285,y=240,width=165,height=150)

# logo moov
answer_logo_moov=Label(debady,text=" ",font=("arial",18),fg="#2603a7")
answer_logo_moov.place(x=485,y=240,width=165,height=150)

#moov=PhotoImage(file="reseau/logo_moov_v.png")
#nswer_logo_moov=Label(debady,image=moov)
#answer_logo_moov.place(x=485,y=240,width=165,height=150)

# logo orange
#answer_logo_orange=Label(debady,text=" ",font=("arial",18),fg="#2603a7")
#answer_logo_orange.place(x=330,y=400,width=300,height=150)

#orange=PhotoImage(file="reseau//logo_orange_v.png")
#answer_logo_orange=Label(debady,image=orange)
#answer_logo_orange.place(x=330,y=400,width=300,height=150)





# information  sur  l'operateur
lab_operateur=Label(debady,text="A PROPOS OPERATEUR",font=("arial",15),bg="white",fg="black")
lab_operateur.place(x=700,y=290)

answer_prefix=Label(debady,text=" ",font=("arial",18),fg="#2603a7")
answer_prefix.place(x=680,y=330,width=300,height=150)


# d'affiche le numero 10 chiffre
lab_affiche_10_chifr=Label(debady,text="LE NUMERO DE 10 CHIFFRE",font=("arial",15),bg="white",fg="black")
lab_affiche_10_chifr.place(x=00,y=530)


answer_num_10=Label(debady,text=" ",fg="#2603a7",font=("arial",18))
answer_num_10.place(x=0,y=580,width=480,height=150)
# nouvel info du new numero

lab_affiche_10_chifr_info=Label(debady,text="A PROPOS NEW NUMERO",font=("arial",15),bg="white",fg="black")
lab_affiche_10_chifr_info.place(x=700,y=550)

entre_apropos_new=Label(debady,text=" ", font=("arial",18),fg="#2603a7")
entre_apropos_new.place(x=500,y=580,width=500,height=150)

# bouton pour saisir un autre numero

lab_ressayer=Button(debady,text="NOUVEAU",font=("arial",15),fg="black",bg="#46e615",command= delect)
lab_ressayer.place(x=500,y=180,width=200,height=50)

# bouton pour quitter

btn_quiter=Button(debady,text="QUITTER",command=quit ,bg="red",font=("arial",15))
btn_quiter.place(x=400,y=718,width=200,height=50)

# message d'aurevoir

fin=Label(debady,text=" A BIENTOT ",font=("arial",15),bg="orange",fg="white")
fin.place(x=8,y=775,width=1000,height=50)

# affichage et maintient de la fenetre de l'appli
debady.bind('<Return>', david)


debady.mainloop()