from tkinter import *

app=Tk()
app.title('application de trier de nombre ')
app.geometry("600x500")
app.config(bg='blue')

def fonvtion():
    try:
        int(champ_saisir.get())
        lbl_result.config(text='tre bien ')
        champ_saisir.delete(0,'end')
    except ValueError:
        lbl_result.config(text="reessayer ")
        champ_saisir.delete(0,'end')

lbl_affiche=Label(app,text='SAISISEZ UN NOMBRE : ',font=40)
lbl_affiche.place(x=70,y=50)

champ_saisir=Entry(app,fg='black',font=30)
champ_saisir.place(x=265,y=50)

lbl_result=Label(app,text="",fg="black",bg='white',width=50,height=10,font=60)
lbl_result.place(x=50,y=200)

btn=Button(app,text='VALIDE',bg='green',fg='white',command=fonvtion)
btn.place(x=300,y=100)
app.mainloop()