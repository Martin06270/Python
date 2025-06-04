# Gestionnaire de tâches simple

def afficher_taches(taches):
    if not taches:
        print("Aucune tâche enregistrée.")
    else:
        print("Liste des tâches :")
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")

def ajouter_tache(taches):
    tache = input("Entrez la nouvelle tâche : ")
    taches.append(tache)
    print("Tâche ajoutée.")

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

def menu():
    taches = []
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

if __name__ == "__main__":
    menu()
