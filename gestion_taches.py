# Gestionnaire de tâches simple

# Fonction pour afficher la liste des tâches
def afficher_taches(taches):
    if not taches:
        print("Aucune tâche enregistrée.")
    else:
        print("Liste des tâches :")
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")

# Fonction pour ajouter une nouvelle tâche à la liste
def ajouter_tache(taches):
    tache = input("Entrez la nouvelle tâche : ")
    taches.append(tache)
    print("Tâche ajoutée.")

# Fonction pour supprimer une tâche de la liste selon son numéro
def supprimer_tache(taches):
    afficher_taches(taches)
    try:
        num = int(input("Numéro de la tâche à supprimer : "))
        if 1 <= num <= len(taches):
            taches.pop(num - 1)
            print("Tâche supprimée.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Fonction principale qui affiche le menu et gère les choix de l'utilisateur
def menu():
    taches = []  # Liste qui contiendra les tâches
    while True:
        print("\n--- Gestionnaire de tâches ---")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        choix = input("Votre choix : ")
        if choix == "1":
            afficher_taches(taches)
        elif choix == "2":
            ajouter_tache(taches)
        elif choix == "3":
            supprimer_tache(taches)
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

# Point d'entrée du programme
if __name__ == "__main__":
    menu()
# Ce script permet de gérer une liste de tâches avec des options pour afficher, ajouter et supprimer des tâches.