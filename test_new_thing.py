from tkinter import *

app=Tk()
app.geometry("800x800")
app.config(background="blue")
app.title("nex_function")


def david():
    a=str(entry_number.get())
    s=a[1]
    s=int(s)

    
    if s==0 or s==1 or s==2 or s==3:
        answer_label.config(text="the operator of thid number is MOOV-CI")
        answer_num_10.config(text="NUMERO 10 CHIFFRES +225 01 {} " .format(entry_number.get()))
        
        answer_prefix.config(text="prefix est 01 ")   
        
    elif s==4 or s==5 or s==6:
        answer_label.config(text="the operator of thid number is MTN-CI")
        answer_num_10.config(text="NUMERO 10 CHIFFRES +225 05 {} " .format(entry_number.get()))
        
        answer_prefix.config(text="prefix est 05 ")   
        
    elif s==7 or s==8 or s==9:
        answer_label.config(text="the operator of thid number is ORANGE-CI")  
        answer_num_10.config(text="NUMERO 10 CHIFFRES +225 07 {} " .format(entry_number.get())) 
         
        answer_prefix.config(text="prefix est 07 ")   
        
        
        

            

number_label=Label(app,text="entry you number")
number_label.place(x=250,y=20)

entry_number=Entry(app)
entry_number.place(x=400,y=20)



btn_numer=Button(app,text="submit",bg="orange",command=david)
btn_numer.place(x=350,y=80,width=50,height=50)

#            operateur

answer_label=Label(app,text=" ",fg="black",font=40)
answer_label.place(x=0,y=150,width=400,height=50)

# prefix de l'operateur



answer_prefix=Label(app,text=" ",fg="black",font=40)
answer_prefix.place(x=0,y=400,width=400,height=50   )

#     afficher les 10 chiffre


answer_num_10=Label(app,text=" ",fg="black",font=40)
answer_num_10.place(x=0,y=250,width=400,height=50)

quit_btn=Button(app,text="quit",command=quit,bg="red",width=10,height=5)
quit_btn.place(x=700,y=300)


app.mainloop()


