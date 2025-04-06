n = int(input("Entrez un nombre entier positif : "))
print(f"Nombres pairs de 0 à {n} :")
for i in range(0, n + 1):
    if i % 2 == 0:
        print(i)

        