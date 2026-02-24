a=0
tab_nom_matier=[]






while True:
    
    print("combien de matiere ? ")
    nbre_matiere=int(input())
    
    while a<nbre_matiere:
        
        if a==0:
            print("veuillez saisir la premiere matiere")
        else:
            print("veuillez saisir la",a+1," premiere matiere")

            
        nom_matier=input()
        tab_nom_matier.append(nom_matier)
        a=a+1
    
    # devoir interro devoir 
    
    type_eva=input("combien de type d'evaluation ? ")
    type_eva=int(type_eva)
    
    r=0
    tab_type_eva=[]
    
    while r<type_eva:
        print("entrez ",r+1," eme type d'évaluation")
        nom_type_eva=input()
        tab_type_eva.append(nom_type_eva)
        r=r+1
    
    
    z=0
    while z<nbre_matiere:
        
        print("en",tab_nom_matier[z],"combien de : ")
        e=0
        while e<type_eva:
                
            print(tab_type_eva[e])
            nbre_dinterro=input()
            nbre_dinterro=int(nbre_dinterro)
            
        
            
            
            
            e=e+1
            
        z=z+1
        
        
            
    t=0
    somme_des_note=0
    while t<nbre_dinterro:
        if t==0:
            print("veuillez saisir la premiere note de ")
        else:
            print("veuillez saisir la",t+1," eme note de")
                
        print(tab_type_eva[t])
                
                
                
        note_interro=input()
        note_interro=int(note_interro)
        somme_des_note=somme_des_note+note_interro
            
                
                    
                
        t=t+1
        
        
        
        
    
                                       
    
    print("la somme  des note est" ,somme_des_note)
    
    
    
    break       
