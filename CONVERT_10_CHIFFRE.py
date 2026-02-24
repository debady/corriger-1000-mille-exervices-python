


from tkinter import *

aicha=Tk()

#resolution de l'ecran


aicha.geometry("800x600")
aicha.config(background="blue")
aicha.resizable(0,0)
aicha.title('david_fonction')

# notre fonction

def aicha_commande(): 

    a=str(entry_numer.get())
    s=a[1]
    s=int(s)
    5
    # pour moov

    
    if s==0 or s==1 or s==2 or s==3:
        answer_label.config(text="the operator of thid number is MOOV-CI")
        answer_num_10.config(text="NUMERO 10 CHIFFRES +225 01 {} " .format(entry_numer.get()))
        answer_prefix.config(text="prefix est 01 ")  
         
    # pour mtn
    
    elif s==4 or s==5 or s==6:
        answer_label.config(text="the operator of thid number is MTN-CI")
        answer_num_10.config(text="NUMERO 10 CHIFFRES +225 05 {} " .format(entry_numer.get()))     
        answer_prefix.config(text="prefix est 05 ")   
        
    # pour orange
        
    elif s==7 or s==8 or s==9:
        answer_label.config(text="the operator of thid number is ORANGE-CI")  
        answer_num_10.config(text="NUMERO 10 CHIFFRES +225 07 {} " .format(entry_numer.get()))       
        answer_prefix.config(text="prefix est 07 ") 
    
    
    






# message de tache

number_label=Label(aicha,text="ENTREZ LE NUMERO : ",width=20,height=3)
number_label.place(x=250,y=20)

# champs de saisir

entry_numer=Entry(aicha,width=40,font=50)
entry_numer.place(x=400,y=30)

# button d'anvoi

btn_numer=Button(aicha,text="VALIDER",bg="green",command=aicha_commande)
btn_numer.place(x=690,y=80,width=80,height=50)

#            operateur

answer_label=Label(aicha,text=" ",fg="black",font=40)
answer_label.place(x=0,y=150,width=400,height=50)

# prefix de l'operateur



answer_prefix=Label(aicha,text=" ",fg="black",font=40)
answer_prefix.place(x=0,y=400,width=400,height=50   )

#     afficher les 10 chiffre


answer_num_10=Label(aicha,text=" ",fg="black",font=40)
answer_num_10.place(x=0,y=250,width=400,height=50)

# bouton pour quiter

quit_btn=Button(aicha,text="TERMINER",command=quit,bg="yellow",width=10,height=2,background="red")
quit_btn.place(x=690,y=500)


aicha.mainloop()