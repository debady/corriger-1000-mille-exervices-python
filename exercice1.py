import os 

os.getcwd()

os.chdir("c:\\TD_PYTHON_FICHIER_DICT")

def saisir(NCIN,NOM,PRENOM,AGE,DECISION):
    
    donne = NCIN + " : " + NOM + " : " + PRENOM  + " : " + AGE  + " : " + +DECISION  + " : "
    return donne
i=0

# connaitre le nombre de candidats 


nbre_candidact=int(input("combien de candidat ? :"))
tab_info_etud=[]
o=0
while i<nbre_candidact:
    
    #  consigne 1 qui permet de recolter les information 
    # consernants les candidats
    
    print("veuilez saisir le NCIN du ",i+1," eme candidat")
    NCIN=input()
    print("veuilez saisir le NOM du ",i+1," eme candidat")
    NOM=input()
    print("veuilez saisir le PRENOM du ",i+1," eme candidat")
    PRENOM=input()
    print("veuilez saisir L'AGE du ",i+1," eme candidat")
    AGE=input()
    print("quel est la decision par raports a mr/mme",NOM,PRENOM," eme candidat")
    DECISION=input()
    
    open("coucours.txt","a")
    a=open("coucours.txt","a")
    a.write("NCIN : "+NCIN + "\n")
    a.write("NOM : "+NOM + "\n" )
    a.write("PENOM : "+PRENOM + "\n" )
    a.write("AGE : "+AGE + "ans" + "\n" )
    a.write("DECISION : "+DECISION + "\n" )
    a.write("\n")
    a.write(" ")
    a.close()
    
    if DECISION=="admis" or DECISION=="ADMIS":
        open("admis.txt","a")
        b=open("admis.txt","a")
        b.write("NCIN : "+NCIN + "\n" )
        b.write("NOM : "+NOM + "\n" )
        b.write("PRENOM : "+PRENOM + "\n" )
        b.write("AGE : "+AGE + "  ans" + "\n" )
        b.write("DECISION : "+DECISION + "\n" )
        b.write("\n ")
        b.close()
        if (DECISION=="admis" or DECISION=="ADMIS") and AGE>="30":
            open("attente.txt","a")
            b=open("attente.txt","a")
            b.write("NCIN : "+NCIN + "\n" )
            b.write("NOM : "+NOM + "\n" )
            b.write("PENOM : "+PRENOM + "\n" )
            b.write("AGE : "+AGE + "ans" + "\n" )
            b.write("DECISION : "+DECISION + "\n" )
            b.write(" ")
            b.close()
            
    else:
        open("refuser.txt","a")
        c=open("refuser.txt","a")
        c.write("NCIN : "+NCIN + "\n" )
        c.write("NOM : "+NOM + "\n" )
        c.write("PENOM : "+PRENOM + "\n" )
        c.write("AGE : "+AGE + "  ans" + "\n" )
        c.write("DECISION : "+DECISION + "\n" )
        c.write(" ")
        c.write("\n ")
        c.write("\n ")

        c.close()

    i=i+1
