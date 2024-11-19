import sys, os
sys.path.append("./utilitaires")
from utils import input_entier, login_joueur, clear_console, charger_score #type: ignore

#Menu des choix principaux

def menu_principale() -> int:
    """
    Affiche le menu principal et renvoie le choix fait par l'utilisateur.
    
    Args:
        (None): Aucun argument n'est nécessaire pour cette preocédure.

    Returns:
        choix (int): Le choix de l'utilisateur.

    """
    #Déclaration des variables
    choix: int
    
    print()
    print("/-----------------------------------------------------------\\")
    print("                   Bienvenu dans le jeu")
    print()
    print("Veuillez faire un choix :")
    print()
    print("1. Jeu des devinettes")
    print("2. Jeu des allumettes")
    print("3. Jeu du Morpion")
    print()
    print("4. Voir les scores")
    print("5. Voir les règles")
    print()
    print("6. Quitter")
    print("\\-----------------------------------------------------------/")
    print()
    #Récupération du choix de l'utilisateur
    choix = input_entier(0, 6, "Votre choix : ", "Veuillez choisir l'un des choix possibles")

    return choix





#Menu du choix des scores

def menu_score() -> int:
    """
    Affiche le menu des scores et renvoie le choix fait par l'utilisateur.
    
    Args:
        (None): Aucun argument n'est nécessaire pour cette preocédure.

    Returns:
        choix (int): Le choix de l'utilisateur.
    """

    #Déclaration des variables
    choix: int


    #Affichage du menu
    clear_console()
    print("/------------------------------\\")
    print("           Les scores")
    print()
    print("Veuillez faire un choix :")
    print()
    print("1. Scores Devinette")
    print("2. Scores Allumettes")
    print("3. Scores Morpion")
    print()
    print("4. Retour au menu principal")
    print()
    print("\\------------------------------/")
    print()


    #Récupération du choix de l'utilisateur et test de validité
    choix = input_entier(1, 4, "Votre choix : ", "Veuillez choisir l'un des choix possibles")
    print()
    
    return choix




def affichage_score(jeu: str):
    """
    Affiche les scores d'un jeu en particulier

    Args:
        jeu(str): Nom du jeu.

    Returns:
        (None) : Ne retourne rien.
    """
    #Déclaration des variables
    scores: dict
    score_total: float = 0

    scores = charger_score(jeu)

    #Affichage des scores
    clear_console()
    if scores == {}:
        print("Aucun score pour ce jeu")
    else:
        print("/------------------------------\\")
        print("Scores du jeu :", jeu)
        print()
        for joueur, score in scores.items():
            for valeur in score:
                score_total += valeur
            print(joueur, ":", score_total, "points en", len(score), "parties")

        print()
        print("\\------------------------------/")
        print()
        print("Appuyez sur Entrée pour continuer", end="")
        input() #Pause pour laisser le temps à l'utilisateur de lire les scores


