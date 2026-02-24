print()
print("            PROGRAMME DE SAVOIR QUEL TYPE DE TRIANGLE ")
print()
print()



a = float(input("veullez entrer la longueur du cote A du triangle : "))
b = float(input("veullez entrer la longueur du cote B du triangle : "))
c = float(input("veullez entrer la longueur du cote C du triangle : "))


#                        premiere condition 








if c>b and c>a and a==b:
    print("le triangle est isocele.")
    if (c**2)==(a**2)+(b**2):
        print("triangle rectangle. ")
    elif a==b and (c**2)==(a**2)+(b**2) :
        print("triangle isocele rectangle.")
    else:
        print("triangle quelquonc.")
    

    
    
    
    
else:
    print("cas impossible.")
    
    
    
#if c>b and c>a:
 #   if a==B:
  #      print("le triangle est isocele.")
  #  else:
   #     if (c**2)==(a**2)+(b**2):
    #        print("triangle rectangle.")
     #   else:
      #      if a==b and (c**2)==(a**2)+(b**2):
       #         print("triangle isocele rectangle.")
        #    else:
         #       print("triangle quelquonc.")
          #      
#else:
 #   print("cas impossible.")