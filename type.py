import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
        self.label = tk.Label(self,border=3,relief=SUNKEN, text="BIENVENUE AKWABA SUR L'APPLICATION\n DE MISE A JOURS \n DES NUMERO DE 8 CHIFFRES A 10 ")
        self.bouton = tk.Button(self, text="Quitter", command=self.quit,bg="#e43010",width="10",height="2",border="20")
        self.label.place(x=0,y=0,width=150,height=100)
        self.bouton.pack()
        
        
        

        
        

        


if __name__ == "__main__":
    app = Application()
    app.title("GROUPE PROJETS PYTHON)")
    app.geometry("400x400")
    app.config(background="#94f7e6")
    app.mainloop()
    
    

import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
        self.label = tk.Label(self, text="BIENVENUE AKWABA SUR L'APPLICATION\n DE MISE A JOURS \n DES NUMERO DE 8 CHIFFRES A 10 ")
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.label.pack()
        self.bouton.place( x=500,y=500) 
        


if __name__ == "__main__":
    app = Application()
    app.title("GROUPE nguessan)")
    app.geometry("400x400")
    app.config(background="#94f7e6")
    app.mainloop()
    
    
    
    

import tkinter as tk
import random as rd

class AppliCanevas(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = 500
        self.creer_widgets()

    def creer_widgets(self):
        # création canevas
        self.canv = tk.Canvas(self, bg="light gray", height=self.size,
                              width=self.size)
        self.canv.pack(side=tk.LEFT)
        # boutons
        self.bouton_cercles = tk.Button(self, text="Cercle !",
                                        command=self.dessine_cercles)
        self.bouton_cercles.pack(side=tk.TOP)
        self.bouton_lignes = tk.Button(self, text="Lignes !",
                                       command=self.dessine_lignes)
        self.bouton_lignes.pack()
        self.bouton_quitter = tk.Button(self, text="Quitter",
                                        command=self.quit)
        self.bouton_quitter.pack(side=tk.BOTTOM)

    def rd_col(self):
        return rd.choice(("black", "red", "green", "blue", "yellow", "magenta",
                          "cyan", "white", "purple"))

    def dessine_cercles(self):
        for i in range(20):
            x, y = [rd.randint(1, self.size) for j in range(2)]
            diameter = rd.randint(1, 50)
            self.canv.create_oval(x, y, x+diameter, y+diameter,
                                  fill=self.rd_col())

    def dessine_lignes(self):
        for i in range(20):
            x, y, x2, y2 = [rd.randint(1, self.size) for j in range(4)]
            self.canv.create_line(x, y, x2, y2, fill=self.rd_col())


if __name__ == "__main__":
    app = AppliCanevas()
    app.title("Mon Canevas Psychédélique !")
    app.mainloop()
    
    

import tkinter as tk
import random as rd

class AppliBaballe(tk.Tk):
    def __init__(self):
        """Constructeur de l'application."""
        tk.Tk.__init__(self)
        # Coord baballe.
        self.x, self.y = 200, 200
        # Rayon baballe.
        self.size = 50
        # Pas de deplacement.
        self.dx, self.dy = 20, 20
        # Création et packing du canvas.
        self.canv = tk.Canvas(self, bg='light gray', height=400, width=400)
        self.canv.pack()
        # Création de la baballe.
        self.baballe = self.canv.create_oval(self.x, self.y,
                                             self.x+self.size,
                                             self.y+self.size,
                                             width=2, fill="blue")
        # Binding des actions.
        self.canv.bind("<Button-1>", self.incr)
        self.canv.bind("<Button-2>", self.boom)
        self.canv.bind("<Button-3>", self.decr)
        self.bind("<Escape>", self.stop)
        # Lancer la baballe.
        self.move()

    def move(self):
        """Déplace la baballe (appelée itérativement avec la méthode after)."""
        # Incrémente coord baballe.
        self.x += self.dx
        self.y += self.dy
        # Vérifier que la baballe ne sort pas du canvas (choc élastique).
        if self.x < 10:
            self.dx = abs(self.dx)
        if self.x > 400-self.size-10:
            self.dx = -abs(self.dx)
        if self.y < 10:
            self.dy = abs(self.dy)
        if self.y > 400-self.size-10:
            self.dy = -abs(self.dy)
        # Mise à jour des coord.
        self.canv.coords(self.baballe, self.x, self.y, self.x+self.size,
                         self.y+self.size)
        # Rappel de move toutes les 50ms.
        self.after(50, self.move)

    def boom(self, mclick):
        """Relance la baballe dans une direction aléatoire au point du clic."""
        self.x = mclick.x
        self.y = mclick.y
        self.canv.create_text(self.x, self.y, text="Boom !", fill="red")
        self.dx = rd.choice([-30, -20, -10, 10, 20, 30])
        self.dy = rd.choice([-30, -20, -10, 10, 20, 30])

    def incr(self, lclick):
        """Augmente la taille de la baballe."""
        self.size += 10
        if self.size > 200:
            self.size = 200

    def decr(self, rclick):
        """Diminue la taille de la baballe."""
        self.size -= 10
        if self.size < 10:
            self.size = 10

    def stop(self, esc):
        """Quitte l'application."""
        self.quit()


if __name__ == "__main__":
    myapp = AppliBaballe()
    myapp.title("Baballe !")
    myapp.mainloop()
