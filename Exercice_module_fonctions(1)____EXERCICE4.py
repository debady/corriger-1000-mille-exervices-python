#-----------------------------Exercice 4-----------------------------


#  Une automobile est utilisée pour un voyage. Concevoir un programme Python qui prend en
#  Entrée la distance du voyage (en km), la consommation moyenne en carburant du
#  véhicule (en L/100 km) et le prix du litre de carburant, et fournit en résultat le coût du
#  carburant pour le voyage.

distance=int(input("veuillez saisir la distance de votre voyage a parcourir (Km) :"))
cout_litre=int(input("a combien cout le litre du carburant : "))

A=distance/100
B=A*cout_litre

print("vous arai besoin de " ,A , " litre de carburant pour votre voyage ")
print(" et vous serai facturer a " ,B , "FCFA")



