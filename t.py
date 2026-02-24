import tkinter
from tkinter import *

app =tkinter.Tk()
app.title('Bonjour')
app.geometry('800x600')
app.config(bg='black')


lble = Label(app,text='Salut',width='10',bg='red')
lble.pack()

btn = Button(app,text='Quitter',command=quit)
btn.pack()


app.mainloop()