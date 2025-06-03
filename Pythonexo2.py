# Demande à l'utilisateur un nombre entier positif
n = int(input("Entrez un nombre entier positif : "))

# Calcule la somme des chiffres de ce nombre
somme = 0
for chiffre in str(n):
    somme += int(chiffre)

print(f"La somme des chiffres de {n} est : {somme}")
