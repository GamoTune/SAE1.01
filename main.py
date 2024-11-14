#Importation des modules
import sys, os
sys.path.append("jeux")
sys.path.append("utilitaires")
sys.path.append("menus")

from allumettes import allumettes #type: ignore


from utils import input_entier, login_joueur, clear_console #type: ignore 
from menus import menu_principale, menu_score #type: ignore






if __name__ == "__main__":
    choix: int
    boucle: bool = True

    clear_console()

    choix = menu_principale()

    while boucle:
        if choix == 1:
            print("Jeu des devinettes")
        elif choix == 2:
            allumettes()
        elif choix == 3:
            print("Jeu du Morpion")
        elif choix == 4:
            print("Voir les scores")
        elif choix == 5:
            print("Voir les règles")
        elif choix == 6:
            print("Au revoir !")
            boucle = False
            continue
        choix = menu_principale()