from tkinter import *

debady=Tk()
debady.geometry("800x700")
debady.title("projets_debady_python")
debady.configure(background="#94f7e6")
#debady.iconbitmap('image\mp.ico')



filename=PhotoImage(file="image//img2.png")
background_label=Label(debady,image=filename)
background_label.place(x=50,y=100)



debady.mainloop()