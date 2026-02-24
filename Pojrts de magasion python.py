from tkinter import *
from tkinter import messagebox,ttk
import tempfile
import random 
from time import strftime
from PIL import ImageTk,Image
import os

# notre classe pour la config de la fentre
class SuperMarche:
    def __init__(self,apk):
        self.apk =apk
        self.apk.title('Gouabo markets')
        self.apk.geometry('1320x750+0+0')
        self.apk.resizable(False,False)

        title=Label(self.apk,text="Super marché gouabo",font=("Algerian",45),bg="gray30",fg="white")
        title.pack(side=TOP,fill=X)

        def heure():
            varheure=strftime("%H:%M:%S")
            labelheur.config(text=varheure)
            labelheur.after(1000,heure)
            
        labelheur=Label(self.apk,text="HH:MM:SS",font=('times new roman',15, "bold"),bg="gray30",fg="white")
        labelheur.place(x=0,y=25,width=120,height=45)
        heure()

        # declaration des variablr---------------
        self.c_phone=StringVar()
        self.c_nom=StringVar()
        
        self.n_facture=StringVar()
        z= random.randint(1000,9999)
        self.n_facture.set(z)

        self.c_email=StringVar()
        self.rech_facture=StringVar()
        self.c_produit=StringVar()
        self.c_prix=IntVar()
        self.qt=IntVar()
        self.totalprix=StringVar()
        self.taxe=StringVar()
        self.totalnet=StringVar()
        #fin declaration variable--------------

        # DECLARATION DES VARIABLES LISTE-------------
        self.liste_categorie=['selection','vetement',"style de vie","telephone"]

        # sous categorie liste vetement
        self.liste_souscategorievetemnet=['panthalon','T-shirt',"shirt"]

        self.pantalon=['levis','mufti',"skykar"]
        self.prixlevice=5000
        self.prixmufti=1000
        self.prixskykar=3000

        self.t_shirt=['polo','roader',"jackjonas"]
        self.prixpolo=15000
        self.prixroader=10000
        self.prixjackjonas=3500

        self.shirt=['peter England','louis vuitton',"culotte"]
        self.prixpeter=5890
        self.prixlouis=6300
        self.prixcollote=6800

        # sous categorie liste style de vie
        self.liste_souscategoriestylevie=['bath soap','creme',"Huile cheveux"]
        self.bath_soap=['liveBuy','lux',"saltoor","fearl"]
        self.prixliveBuy=850
        self.prixlux=270
        self.prixsaltoor=992
        self.prixsfearl=7845

        self.creme=['fairelovely','ponds',"olay","ghanea"]
        self.prixfaire_lovely=1500
        self.prixrponds=1000
        self.prixolay=350
        self.prixghanea=897

        self.huile_cheveux=['panachute','jacsmith',"bajaj"]
        self.prixpanachute=4890
        self.prixjacsmith=300
        self.prixbajaj=3800

        # sous categorie telephone
        self.liste_souscategorietelephone=['iphone','samsung',"huawei", "techno"]

        self.samsung=['samsung m6','samsung m7',"samsung m8"]
        self.prixsamsumg6=875000
        self.prixsamsumg7=255000
        self.prixsamsumg8=210000

        self.iphone=['iphone x','iphone 8',"iphone pro"]
        self.prixiphone_x=1500
        self.prixiphone8=1000
        self.prixiphone_pro=350

        self.huawei=['huaweix1','huaweix2',"huaweix3"]
        self.huaweix1=5300
        self.huaweix2=8500
        self.huaweix3=1800

        self.techno=['technot1','technot2',"technot3"]
        self.technot1=5300
        self.technot2=8500
        self.technot3=18000
        # FIN LIQTE MOIS--------------

        # GRANDE FRAME
        main_Frame=Frame(self.apk,bd=2,relief=GROOVE,bg="gray30")
        main_Frame.place(x=10,y=130,width=1300,height=600)

        #INFO CLIENT**********************
        #debut label-----------
        client_frame = LabelFrame(main_Frame,text='Client',font=("times new roman",15),bg="white",fg='black')
        client_frame.place(x=10,y=5,width=330,height=150)

        #contact
        self.lbl_conatct=Label(client_frame,text="Contact",font=('times new roman',15,"bold"),bg="white")
        self.lbl_conatct.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        #nom
        self.lbl_nomclient=Label(client_frame,text="Nom Clinet",font=('times new roman',15,"bold"),bg="white")
        self.lbl_nomclient.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        #email
        self.lbl_emailclient=Label(client_frame,text="Email",font=('times new roman',15,"bold"),bg="white")
        self.lbl_emailclient.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        # fin labelle-------

        #debut saisir ------------------------------------------
        # contact
        self.txt_contactclient=Entry(client_frame,textvariable=self.c_phone,font=('times new roman',15,"bold"),bg="white")
        self.txt_contactclient.grid(row=0,column=1,sticky=W,padx=5,pady=2)   

        #SAISIR nom
        self.txt_nomclient=Entry(client_frame,textvariable=self.c_nom,font=('times new roman',15,"bold"),bg="white")
        self.txt_nomclient.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        #SAISIR email
        self.txt_emailclient=Entry(client_frame,textvariable=self.c_email,font=('times new roman',15,"bold"),bg="white")
        self.txt_emailclient.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        #fin saisir--------

        #debut label-----------
        produit_frame = LabelFrame(main_Frame,text='Produits',font=("times new roman",15),bg="white",fg='black')
        produit_frame.place(x=350,y=5,width=600,height=150 )

        self.lbl_categorie=Label(produit_frame,text="categorie",font=('times new roman',15,"bold"),bg="white")
        self.lbl_categorie.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.lbl_souscategorie=Label(produit_frame,text="sous categorie",font=('times new roman',15,"bold"),bg="white")
        self.lbl_souscategorie.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.lbl_nomproduite=Label(produit_frame,text="Nom produit",font=('times new roman',15,"bold"),bg="white")
        self.lbl_nomproduite.grid(row=2  ,column=0,sticky=W,padx=5,pady=2)

        self.lbl_prix=Label(produit_frame,text="Prix",font=('times new roman',15,"bold"),bg="white")
        self.lbl_prix.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.qte=Label(produit_frame,text="quantité",font=('times new roman',15,"bold"),bg="white")
        self.qte.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        #1er sous liste categorie
        self.text_categorie =ttk.Combobox(produit_frame,font=('times new roman',10),values=self.liste_categorie,width=24,state="readonly")
        self.text_categorie.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.text_categorie.current(0)
        self.text_categorie.bind("<<comboboxSelected>>",self.fonct_cat)


        # 2eme sous liste sous categorie
        self.text_souscategorie =ttk.Combobox(produit_frame,font=('times new roman',10),values=[''],width=24,state="readonly")
        self.text_souscategorie.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.text_souscategorie.current(0)
        self.text_souscategorie.bind("<<ComboboxSelected>>",self.fonct_sous_cat)
        #----

        # 3eme sous liste  nom prod
        self.text_nomprod =ttk.Combobox(produit_frame,font=('times new roman',10),textvariable=self.c_produit ,width=24,state="readonly")
        self.text_nomprod.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.text_nomprod.bind("<<comboboxSelected>>",self.fonct_nomprod)
        #----

        # 4eme sous liste prix
        self.text_prix =ttk.Combobox(produit_frame,font=('times new roman',10),textvariable=self.c_prix ,width=24,state="readonly")
        self.text_prix.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        #----

        # 4eme  sous liste quantité
        self.qte =ttk.Combobox(produit_frame,font=('times new roman',10),textvariable=self.qt,width=20 ,state="readonly")
        self.qte.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #----
        self.btn_sort = Button(self.apk,text='terminer',bg="red",fg='white',width=20,font=('bold',10),command=quit)
        self.btn_sort.place(x=670,y=325)

# LES FONCTION
        # def categorie soi

        def  fonct_cat(self,even=""):
            if self.text_categorie.get()=="vetement":
                self.text_souscategorie.config(values=self.liste_souscategorievetemnet)
                self.text_souscategorie.current(0)

            if self.text_categorie.get()=="style de vie":
                self.text_souscategorie.config(values=self.liste_souscategoriestylevie)
                self.text_souscategorie.current(0)


            if self.text_categorie.get()=="telephone":
                self.text_souscategorie.config(values=self.liste_souscategorietelephone)
                self.text_souscategorie.current(0)
                

        # def sous categorie'selection','vetement',"style de vie","telephone"]
        def fonct_sous_cat(self,even=''):
            
            # vet
            if (self.text_souscategorie.get=='panthalon'):
               self.txt_nomprod.config(values=self.pantalon)
               self.text_nomprod.current(0)

            if self.text_souscategorie.get=="T-shirt":
               self.text_nomprod.config(values=self.shirt)
               self.nomprod.curent(0)

            if self.text_souscategorie.get=="shirt":
               self.text_nomprod.config(values=self.shirt)
               self.nomprod.curent(0)

            # style vie
            if (self.text_souscategorie.get=='bath soap'):
               self.txt_nomprod.config(values=self.bath_soap)
               self.text_nomprod.current(0)

            if self.text_souscategorie.get=="creme":
               self.text_nomprod.config(values=self.creme)
               self.nomprod.curent(0)

            if self.liste_souscategoriestylevie.get=="Huile cheveux":
               self.text_nomprod.config(values=self.creme)
               self.nomprod.curent(0)  

            #telephone---  
            if self.text_souscategorie.get=="iphone":
               self.text_nomprod.config(values=self.iphone)
               self.nomprod.curent(0)

            if self.liste_souscategoriestylevie.get=="samsung":
               self.text_nomprod.config(values=self.samsung)
               self.nomprod.curent(0) 

            if self.liste_souscategoriestylevie.get=="tecno":
               self.text_nomprod.config(values=self.tecno)
               self.nomprod.curent(0)

            if (self.liste_souscategorietelephone.get=='huawei'):
                self.txt_nomprod.config(values=self.huawei)
                self.text_nomprod.current(0)

        def fonct_nomprod(self,event=""):
           # pantalon

            if (self.text_nomprod.get=='levis'): 
               self.prixlevice.config(values=self.prixlevice)
               self.prixlevice.current(0)
               self.qte.set(1)

            if (self.text_nomprod.get=='mufti'):
                self.prixmufti.config(values=self.prixmufti)
                self.prixmufti.current(0)
                self.qte.set(1)      

            if (self.text_nomprod.get=='skykar'):
                self.prixskykar.config(values=self.prixskykar)
                self.prixskykar.current(0)
                self.qte.set(1)   

            # chemise
            if (self.text_nomprod.get=='polo'): 
               self.prixpolo.config(values=self.prixlevice)
               self.prixpolo.current(0)
               self.qte.set(1)

            if (self.text_nomprod.get=='roader'):
                self.prixroader.config(values=self.prixmufti)
                self.prixroader.current(0)
                self.qte.set(1)      

            if (self.text_nomprod.get=='jackjonas'):
                self.prixjackjonas.config(values=self.prixskykar)
                self.prixjackjonas.current(0)
                self.qte.set(1)

            # cullote
            if (self.text_nomprod.get=='peter England'): 
               self.prixpeter.config(values=self.prixpeter)
               self.prixpeter.current(0)
               self.qte.set(1)

            if (self.text_nomprod.get=='louis vuitton'):
                self.prixlouis.config(values=self.prixlouis)
                self.prixlouis.current(0)
                self.qte.set(1)      

            if (self.text_nomprod.get=='culotte'):
                self.prixcollote.config(values=self.prixcollote)
                self.prixcollote.current(0)
                self.qte.set(1)

            # style vie
            if (self.text_nomprod.get=='liveBuy'): 
               self.prixliveBuy.config(values=self.prixliveBuy)
               self.prixliveBuy.current(0)
               self.qte.set(1)

            if (self.text_nomprod.get=='lux'):
                self.prixlux.config(values=self.prixlux)
                self.prixlux.current(0)
                self.qte.set(1)      

            if (self.text_nomprod.get=='saltoor'):
                self.prixsaltoor.config(values=self.prixsaltoor)
                self.prixsaltoor.current(0)
                self.qte.set(1)

            if (self.text_nomprod.get=='fearl'):
                self.prixsfearl.config(values=self.prixsfearl)
                self.prixsfearl.current(0)
                self.qte.set(1)

            # 2em  style vie
            if (self.text_nomprod.get=='fairelovely'): 
               self.prixfaire_lovely.config(values=self.prixfaire_lovely)
               self.prixfaire_lovely.current(0)
               self.qte.set(1)

            if (self.text_nomprod.get=='ponds'):
                self.prixrponds.config(values=self.prixrponds)
                self.prixrponds.current(0)
                self.qte.set(1)      

            if (self.text_nomprod.get=='olay'):
                self.prixolay.config(values=self.prixolay)
                self.prixolay.current(0)
                self.qte.set(1)

            # 3eme style vie
            if (self.text_nomprod.get=='ghanea'):
                self.prixghanea.config(values=self.prixghanea)
                self.prixghanea.current(0)
                self.qte.set(1)
            
            if (self.text_nomprod.get=='panachute'):
                self.prixpanachute.config(values=self.prixpanachute)
                self.prixpanachute.current(0)
                self.qte.set(1)      

            if (self.text_nomprod.get=='jacsmith'):
                self.prixjacsmith.config(values=self.prixjacsmith)
                self.prixjacsmith.current(0)
                self.qte.set(1)

            if (self.text_nomprod.get=='bajaj'):
                self.prixbajaj.config(values=self.prixbajaj)
                self.prixbajaj.current(0)
                self.qte.set(1)

            # telephone-------------
            #samsung
            if (self.text_nomprod.get=='samsung m6'): 
               self.prixsamsumg6.config(values=self.prixsamsumg6)
               self.prixsamsumg6.current(0)
               self.qte.set(1)

            if (self.text_nomprod.get=='samsung m7'):
                self.prixsamsumg7.config(values=self.prixsamsumg7)
                self.prixsamsumg7.current(0)
                self.qte.set(1)      

            if (self.text_nomprod.get=='samsung m8'):
                self.prixsamsumg8.config(values=self.prixsamsumg8)
                self.prixsamsumg8.current(0)
                self.qte.set(1)

            #iphone
            if (self.text_nomprod.get=='iphone x'):
                self.prixiphone_x.config(values=self.prixiphone_x)
                self.prixiphone_x.current(0)
                self.qte.set(1)

            if (self.text_nomprod.get=='iphone 8'): 
               self.prixiphone8.config(values=self.prixiphone8)
               self.prixiphone8.current(0)
               self.qte.set(1)

            if (self.text_nomprod.get=='iphone pro'):
                self.prixiphone_pro.config(values=self.prixiphone_pro)
                self.prixiphone_pro.current(0)
                self.qte.set(1)      

            #huawei
            if (self.text_nomprod.get=='huaweix1'):
                self.huaweix1.config(values=self.huaweix1)
                self.huaweix1.current(0)
                self.qte.set(1)

            if (self.text_nomprod.get=='huaweix2'):
                self.huaweix2.config(values=self.huaweix2)
                self.huaweix2.current(0)
                self.qte.set(1)   

            if (self.text_nomprod.get=='huaweix3'):
                self.huaweix3.config(values=self.huaweix3)
                self.huaweix3.current(0)
                self.qte.set(1)    

            #techno
            if (self.text_nomprod.get=='technot1'):
                self.technot1.config(values=self.huaweix2)
                self.huaweix2.current(0)
                self.qte.set(1)   

            if (self.text_nomprod.get=='technot2'):
                self.technot2.config(values=self.technot2)
                self.technot2.current(0)
                self.qte.set(1)

            if (self.text_nomprod.get=='technot3'):
                self.technot2.config(values=self.technot2)
                self.technot2.current(0)
                self.qte.set(1)
                          
        # FIN INFO PRODUITS
if __name__=="__main__":
    apk=Tk()
    obj = SuperMarche(apk)
    apk.mainloop()