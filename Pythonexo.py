n = int(input("Entrez un nombre entier positif : "))
# Affiche les nombres pairs de 0 à n    

print(f"Nombres pairs de 0 à {n} :")

for i in range(0, n + 1):  # Correction ici
    if i % 2 == 0:
        print(i)



