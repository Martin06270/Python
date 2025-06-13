import random
import string

def generer_mot_de_passe(longueur=12):
    # Caractères possibles : lettres, chiffres, symboles
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

if __name__ == "__main__":
    try:
        longueur = int(input("Longueur du mot de passe (par défaut 12) : ") or 12)
        mdp = generer_mot_de_passe(longueur)
        print(f"Mot de passe généré : {mdp}")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
