import random

def jeu_devinette():
    nombre_a_trouver = random.randint(1, 100)  # Génère un nombre aléatoire entre 1 et 100
    essais = 0

    print("Bienvenue dans le jeu de devinette !")
    print("J'ai choisi un nombre entre 1 et 100. À vous de le deviner !") # Demande a l'utilisateur de deviner le nombre du joueur 

    while True:
        try:
            choix = int(input("Entrez votre proposition : "))  # Correction de la syntaxe
            essais += 1
            
            if choix < nombre_a_trouver:
                print("Trop petit ! Essayez encore.")
            elif choix > nombre_a_trouver:
                print("Trop grand ! Essayez encore.")
            else:
                print(f"Bravo ! Vous avez trouvé le nombre {nombre_a_trouver} en {essais} essais.")
                break  # Sort de la boucle quand le bon nombre est trouvé
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Exécuter le jeu
if __name__ == "__main__":
    jeu_devinette()


