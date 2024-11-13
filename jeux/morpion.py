#Importation des fonctions
import sys, os
sys.path.append("./utilitaires")
from utils import login_joueur, input_entier, clear_console  # type: ignore


def morpion():
    """
    Cette procédure est la procédure principale du jeu du morpion. Elle permet de jouer à ce jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette preocédure.

    Returns:
        (None): Cette procédure ne retourne rien.
    """
    clear_console()

    print("/-------------------------------------\\")
    print()
    
    joueur1, joueur2 = login_joueur()


    return