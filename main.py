#Importation des modules
import sys, os
sys.path.append("jeux")
sys.path.append("utilitaires")
sys.path.append("menus")

from allumettes import allumettes #type: ignore
from morpion import morpion #type: ignore
from devinette import devinette #type: ignore

from utils import input_entier, login_joueur, clear_console, charger_score #type: ignore
from menus import menu_principale, menu_score, menu_regle, affichage_score, affichage_relges #type: ignore


#La fonction rejouer permet de demander à l'utilisateur s'il veut rejouer
def rejouer() -> bool:
    """
    Demande à l'utilisateur s'il veut rejouer à un jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette fonction.
    
    Returns:
        valeur (bool): True si l'utilisateur veut rejouer, False sinon.
    """

    #Déclaration de la variable
    valeur: bool

    #Demande à l'utilisateur s'il veut rejouer
    valeur = True if input("Voulez-vous rejouer ? (o/n) : ").casefold() == "o" else False
    clear_console()
    return valeur






if __name__ == "__main__":
    choix: int
    boucle: bool = True
    boucle_de_jeu: bool = True

    clear_console()

    while boucle:
        choix = menu_principale()

        match choix:
            case 1:
                while boucle_de_jeu:
                    devinette()
                    boucle_de_jeu = rejouer()
                boucle_de_jeu = True
            case 2:
                while boucle_de_jeu:
                    allumettes()
                    boucle_de_jeu = rejouer()
                boucle_de_jeu = True
            case 3:
                while boucle_de_jeu:
                    morpion()
                    boucle_de_jeu = rejouer()
                boucle_de_jeu = True
            case 4: 
                while boucle_de_jeu:
                    match menu_score():
                        case 1:
                            affichage_score("devinettes")
                        case 2:
                            affichage_score("allumettes")
                        case 3:
                            affichage_score("morpion")
                        case 4:
                            boucle_de_jeu = False
                        case _:
                            clear_console()
                            print("Erreur de choix")
                clear_console()
                boucle_de_jeu = True
            case 5:
                while boucle_de_jeu:
                    match menu_regle():
                        case 1:
                            affichage_relges("devinettes")
                        case 2:
                            affichage_relges("allumettes")
                        case 3:
                            affichage_relges("morpion")
                        case 4:
                            boucle_de_jeu = False
                        case _:
                            clear_console()
                            print("Erreur de choix")
                clear_console()
                boucle_de_jeu = True
            case 6:
                boucle = False
            case _:
                clear_console()
                print("Erreur de choix")
    clear_console()
    print("Merci d'avoir joué !")
