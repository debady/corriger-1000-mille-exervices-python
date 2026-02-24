



class application(object):
    def __init__(self):
        

       
        
# construction de la premiere fenetre
        
        self.root=Tk()
        self.root.title("appli de code de couleurs")
        self.root.geometry("600x600+300+300")
        
        
        Label(self.root,text="entez la valeurs de la resistance en ohms :",fg="red").\
            grid(row=2,column=1,columnspan=3)
            
        Button(self.root,text="montrer",width=5,height=5,fg='ivory',bg="green").\
            grid(row=3,column=1)
            #,command=self.ChangeCouleurs

    
            
        Button(self.root,text="quitter",command=self.root.quit ,width=5,height=5,fg='ivory',bg="green").\
            grid(row=3,column=3)
            
            
        
        self.entree=Entry(self.root,width=50,highlightthickness=50)
        self.entree.grid(row=3,column=2)
        
# code des couleurs de 0 a 9

        self.cc=["black","brown","red","orange","yellow","green","blue","purple","grey","white"]
        self.root.mainloop()

        
        def designeResistance(self):
# canevas avec un modele de resistance a trois lignes coloré 

            
            self.can = canvas(self.root,width=250,height=100,bg="ivory")
            self.can.grid(row=1,column=1,columnspan=3,pady=5,pax=5)
            
            self.can.create_line(10,50,240,50,width=5)
            self.can.create_rectangle(65,30,185,70,fill="ligth grey ",width=2)
            
 # dessin des trois lignes colore noir par defaut 
            self.ligne=[]
            for x in range(85,150,24):
                self.ligne.append(self.can.create_rectangle(x,30,x+12,70,fill="black",whidth=0))
                
        def ChangeCouleurs(self):
            self.v1ch = self.entree.get()  # methode qui renvoie une chaine de caracter
            try:
                v =float(self.v1ch)
            except:
                err = 1
            else:
                err = 0
            if err==1 or v<10 or v>1e11:
                self.signalError()
            else:
                li=[0]*3
                logv=int(log10(v))
                ordgr = 10**logv
                
                # extraction du premiere chifffre significatif :
                
                li[0]=int(v/ordgr)
                decim=v/ordgr-li[0]
                
                # extraction des 2eme chiffre significatifs 
                
                li[1]= int(decim*10+.5) # + .5 pour arrondir correctement
                
                # nombre de zero a accoler au deux chiffre significatif s
                
                li[2]=logv-1
                
                # coloraation des 3 lignes 
                for n in range(3):
                    self.can.itemconfigure(self.ligne[n],fill=self.cc[li[n]])
                    
        

                    
                    
        def signaleError(self):
            self.entree.configure(bg='red')  # colorer le fond de champs 
            self.root.after(1000,self.videEntree)  # apres 1 seconde effecé
                
        
        def videEntree(self):
            self.entree.configure(bg='white')  # retabli le fond blanc
            self.root.delecte(0,len(self.v1ch))  # enlever le car.present
            
            
# ----------------------PROGRAMME PRINCIPALES------------


if __name__ == '__main__':
    
    from tkinter import *
    from math import log10  # loga base 10
    
    f = application()   # instanciaton de l'object application 
    f.root.mainloop()
    
                    
                