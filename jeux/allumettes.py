#Importation des fonctions
import sys, os
sys.path.append("./utilitaires")
from utils import input_entier, login_joueur, clear_console #type: ignore


#Programme principal du jeu
def allumettes() -> None:
    """
    Cette fonction est la fonction principale du jeu des allumettes. Elle permet de jouer à ce jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette fonction.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    
    #Déclaration des variables à utilisé
    nomJoueur1: str
    nomJoueur2: str

    nbrAllumettes: int = 20
    nbrCoupsJoueur1: int = 0
    nbrCoupsJoueur2: int = 0
    dernierJoueur: str = ""

    nomJoueur1, nomJoueur2 = login_joueur()

    #Début du jeu

    clear_console()

    print("/-----------------------------------------------------------\\")
    print("                     Jeu des allumettes")
    
    #Tant qu'il reste des allumettes le jeu continue
    while nbrAllumettes > 0:

        #Tour du joueur 1
        if nbrAllumettes > 0:
            dernierJoueur = nomJoueur1
            nbrAllumettes -= tour(nomJoueur1, nbrAllumettes)
            nbrCoupsJoueur1 += 1
        
        #Tour du joueur 2
        if nbrAllumettes > 0:
            dernierJoueur = nomJoueur2
            nbrAllumettes -= tour(nomJoueur2, nbrAllumettes)
            nbrCoupsJoueur2 += 1
    
    #Calcul du score

    



    #Fin du jeu
    print()
    if dernierJoueur == nomJoueur2:
        print(f"Bravo {nomJoueur1} vous avez gagné en {nbrCoupsJoueur1} coups.")
        print(f"{nomJoueur2} vous avez perdu en {nbrCoupsJoueur2} coups.")
    else:
        print(f"Bravo {nomJoueur2} vous avez gagné en {nbrCoupsJoueur2} coups.")
        print(f"{nomJoueur1} vous avez perdu en {nbrCoupsJoueur1} coups.")
    print()


#Fonction pour afficher le tour du joueur
def tour(joueur:str, nbrAllumettes:int) -> int:
    """
    Cette fonction permet d'afficher le tour du joueur et le nombre d'allumettes restantes.

    Args:
        joueur (str): Le nom du joueur qui joue.
        nbrAllumettes (int): Le nombre d'allumettes restantes.

    Returns:
        (int): Le nombre d'allumettes retirées par le joueur
    """

    #Déclaration des variables
    nbrAllumettesRetirees: int = 0

    print()
    print(f"{joueur} c'est à votre tour.")
    print(f"Il reste {nbrAllumettes} allumettes.")
    nbrAllumettesRetirees = input_entier(1, 3, "Combien d'allumettes voulez-vous retirer, 1, 2 ou 3 : ", "ERROR")

    return nbrAllumettesRetirees




allumettes()