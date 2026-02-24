import tkinter as tk
import random as rd


app=tk.Tk()

a=tk.IntVar(app,rd.randint(1,100))

name=tk.Entry(app,textvariable="")
name.grid()





def nom():
    name=tk.Entry(app,textvariable=name)
    n=tk.Entry(app,textvariable=name)
    
    name.setvar(n)
    
lbt_name=tk.Label(app,text=name)
lbt_name.grid()
    
    
def  init():
    g=rd.randint(1, 100)
    a.set(g)
    
    
def incre():
    c=a.get()
    c=c+1
    a.set(c)
    
    
def decre():
    b=a.get()
    b=b-1
    a.set(b)
    

    
app.geometry("600x600+300+300")
app.title("nguessan")

s=tk.Entry(app,textvariable="soit saluer ")
s.grid()


btn=tk.Button(app,text="submit",command=nom)
btn.grid()




lbt=tk.Label(app,textvariable=a)
lbt.grid(row=3,column=3)


btn_init=tk.Button(app,text="initialiser",command=init)
btn_init.grid()


btn_decr=tk.Button(app,text="decrementer",command=decre)
btn_decr.grid()

btn_incrr=tk.Button(app,text="incrementer",command=incre)
btn_incrr.grid()

app.mainloop()