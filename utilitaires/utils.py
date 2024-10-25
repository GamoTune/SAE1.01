########################################################################################
# Ce fichier contient les fonctions utilitaires qui seront utilisées dans le programme #
########################################################################################

import os


#Fonction pour demander le nom des joueurs
def login_joueur() -> tuple[str, str]:
    """
    Procédure servant à attribuer un nom aux joueurs
    Args:
        (None) : Ne prend pas de paramètres.

    Returns:
        (tuple[str, str]) : tuple contenant les noms des 2 joueurs.

    """
    
    #Déclaration des variables
    joueur1 : str
    joueur2 : str


    #Saisie des noms des joueurs
    print()
    print("/---------------------------------------\\")
    print("      Saisie des noms des joueurs")
    joueur1 = str(input("Saisir le prénom du premier joueur : "))
    joueur2 = str(input("Saisir le prénom du second joueur : "))
    
    return (joueur1, joueur2)


def input_entier(borneMin:int, borneMax:int, message:str) -> int:
    """
    Fonction pour vérifier si l'entrée utilisateur est un entier et qu'il est compris entre les bornes données
    Args:
        borneMin(int): Borne inférieure.
        borneMax(int): Borne supérieure.
        message(str): Message à afficher.

    Returns:
        nombre(int): Nombre entré par l'utilisateur.
    """

    nombre: int
    nombre = int(input(message))
    while nombre < borneMin or nombre > borneMax:
        nombre = int(input(message))
    return nombre


def clear_console():
    """
    Procédure pour effacer la console
    Args:
        (None) : Ne prend pas de paramètres.

    Returns:
        (None) : Ne retourne rien.

    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')