import random as rd
import tkinter as tk 

app=tk.Tk()
app.geometry("600x600+300+300")
app.title("debady chatu nguessan")


a=tk.IntVar(app,rd.randint(100, 500))

def reini():
    b=rd.randint(100,500)
    a.set(b)
    
def inc():
    c=a.get()
    c+=1
    a.set(c)

def dec():
    d=a.get()
    d-=1
    a.set(d)
    






#b=tk.IntVar(app,rd.randint(100, 500))

lbl_1=tk.Label(app,textvariable=a,fg='Blue',font=("green",25))
lbl_1.grid()

btn_reini=tk.Button(app,text=" reinitialiser ",command=reini)
btn_reini.grid()


btn_inc=tk.Button(app,text="incrementer",command=inc)
btn_inc.grid()

btn_dec=tk.Button(app,text="decrementer",command=dec)
btn_dec.grid()

app.mainloop()
# recuperer 

#text=tk.Entry(app,text="",bg="green")
#text.grid()



#lbl_3=tk.Label(app,textvariable=text)
#lbl_3.grid()




#btn_envoyer=tk.Button(app,text="envoi")
#btn_envoyer.grid()




# afficher recuperer 





#ent1=tk.Entry(app,text="",bg="Blue")
#ent1.grid()

#btn_valide=tk.Button(app,text="VALIDE",fg="green",command=valider)
#btn_valide.grid()


# partie pour afficher les ecrits 

#ent2=tk.Entry(app,text="")
#ent2.grid()

#btn_valider2=tk.Button(app,text="velider2",background="yellow",command=valider2)
#btn_valider2.grid()

#lbl_2=tk.Label(app,textvariable=ent2)
#lbl_2.grid


#a=tk.StringVar(app,"BONJOUR ",)
#lbl_1=tk.Label(app,textvariable=a)
#lbl_1.Grid() row=3,columnspan=3,padx=10,pady=10

