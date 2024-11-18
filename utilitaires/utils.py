########################################################################################
# Ce fichier contient les fonctions utilitaires qui seront utilisées dans le programme #
########################################################################################

import os, pickle


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
    while joueur1 == "" :
        joueur1=str(input("Veuillez rentrer un prénom valide : "))

    joueur2 = str(input("Saisir le prénom du second joueur : "))
    while joueur2 == "" :
        joueur2=str(input("Veuillez rentrer un prénom valide : "))

    return (joueur1, joueur2)


def input_entier(borneMin:int, borneMax:int, message:str, erreur:str) -> int:
    """
    Fonction pour vérifier si l'entrée utilisateur est un entier et qu'il est compris entre les bornes données
    Args:
        borneMin(int): Borne inférieure.
        borneMax(int): Borne supérieure.
        message(str): Message à afficher.
        erreur(str): Message d'erreur à afficher.

    Returns:
        nombre(int): Nombre entré par l'utilisateur.
    """

    input_: str
    nombre: int

    input_ = input(message)
    while not input_.isdigit():
        print(erreur)
        input_ = input(message)
    nombre = int(input_)

    while nombre < borneMin or nombre > borneMax:
        print(erreur)
        nombre = int(input(message))
    return nombre


def clear_console() -> None:
    """
    Procédure pour effacer la console
    Args:
        (None) : Ne prend pas de paramètres.

    Returns:
        (None) : Ne retourne rien.

    """
    print("\033c", end="")


def sauvegarde_score(chemin:str, data:dict) -> None:
    with open(chemin, "wb") as fichier:
        pickle.dump(data, fichier)

def charger_score(chemin:str) -> dict:
    with open(chemin, "rb") as fichier:
        data = pickle.load(fichier)
    return data