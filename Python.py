import random

def jeu_devinette():
    nombre_a_trouver = random.randint(1, 100) # Génère un nombre aléatoire entre 1 et 100
    essais = 0 


    print("Bienvenue dans le jeu de devinette !")
    print("J'ai choisi un nombre entre 1 et 100. À vous de le deviner !")

    while True:

        try:

            choix = int(input("Entrez votre proposition : "))