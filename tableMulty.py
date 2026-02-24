#-----------------
# ECRIRE UN PROGRAMME QUI AFFICHE LA TABLE DE MULTIPLICATION 
#-----------------

num = 1
while num <= 10:
    print(f"Table de multiplication pour {num}:")
    i = 1
    while i <= 10:
        product = num * i
        print(f"{num} x {i} = {product}")
        i += 1
    print()  # Ligne vide pour séparer les tables
    num += 1