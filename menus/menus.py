import sys, os
sys.path.append("./utilitaires")
from utils import input_entier, login_joueur, clear_console #type: ignore

#Menu des choix principaux

def menu_principale() ->int:
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
    print()
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
    print("5. Quitter")
    print("\\------------------------------/")
    print()


    #Récupération du choix de l'utilisateur et test de validité
    choix = int(input("Votre choix : "))
    while choix < 1 or choix > 5:
        print("Veuillez choisir l'un des choix possibles")
        choix = int(input("Votre choix : "))
    print()
    
    return choix