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

    nbrAllumettesDepart: int = 20
    nbrAllumettes: int = 20
    nbrAllumettesJoueur1: int = 0 #Nombre d'allumettes retirées par le joueur 1
    nbrAllumettesJoueur2: int = 0 #Nombre d'allumettes retirées par le joueur 2

    nbrCoupsJoueur1: int = 0
    nbrCoupsJoueur2: int = 0

    dernierJoueur: str = ""
    avantDernierJoueur: str = ""
    vainqueur: str = ""

    scoreJoueur1: float = 0
    scoreJoueur2: float = 0


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
            avantDernierJoueur = nomJoueur2
            nbrAllumettes -= tour(nomJoueur1, nbrAllumettes)
            nbrCoupsJoueur1 += 1
        
        #Tour du joueur 2
        if nbrAllumettes > 0:
            dernierJoueur = nomJoueur2
            avantDernierJoueur = nomJoueur1
            nbrAllumettes -= tour(nomJoueur2, nbrAllumettes)
            nbrCoupsJoueur2 += 1

        if nbrAllumettes == 0:
            vainqueur = avantDernierJoueur
    

    #Calcul du score

    if vainqueur == nomJoueur1:
        scoreJoueur1 = calcul_score(nbrAllumettesDepart, nbrAllumettesJoueur1, nbrCoupsJoueur1, 1)
        scoreJoueur2 = calcul_score(nbrAllumettesDepart, nbrAllumettesJoueur2, nbrCoupsJoueur2, 0)
    else:
        scoreJoueur1 = calcul_score(nbrAllumettesDepart, nbrAllumettesJoueur1, nbrCoupsJoueur1, 0)
        scoreJoueur2 = calcul_score(nbrAllumettesDepart, nbrAllumettesJoueur2, nbrCoupsJoueur2, 1)


    #Fin du jeu
    print()
    print("/-----------------------------------------------------------\\")
    print("                        Fin du jeu")
    print()
    if vainqueur == nomJoueur1:
        print(f"Bravo {nomJoueur1} vous avez gagné en {nbrCoupsJoueur1} coups.")
        print(f"{nomJoueur2} vous avez perdu en {nbrCoupsJoueur2} coups.")
    else:
        print(f"Bravo {nomJoueur2} vous avez gagné en {nbrCoupsJoueur2} coups.")
        print(f"{nomJoueur1} vous avez perdu en {nbrCoupsJoueur1} coups.")
    print()
    print(f"Score de {nomJoueur1} : {scoreJoueur1}")
    print(f"Score de {nomJoueur2} : {scoreJoueur2}")
    print()
    print("\\-----------------------------------------------------------/")




def calcul_score(nbrAllumettes:int, nbrAllumettesJoueur:int, nbrCoups:int, victoir:int) -> float:
    """
    Cette fonction permet de calculer le score d'un joueur.

    Args:
        nbrAllumettes (int): Le nombre d'allumettes au début du jeu.
        nbrAllumettesJoueur (int): Le nombre d'allumettes retirées par le joueur.
        nbrCoups (int): Le nombre de coups joués par le joueur.

    Returns:
        (float): Le score du joueur.
    """

    #Déclaration des variables

    score: float = 0
    differenceScore: int = 0

    #Calcul du score
    differenceScore = nbrAllumettes - nbrAllumettesJoueur
    score = (differenceScore / nbrCoups) + (victoir * 5)

    return round(score,2)


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
    limite_allumettes: int = 3

    #Calcule du nombre d'allumettes restantes
    if nbrAllumettes < 3:
        limite_allumettes = nbrAllumettes

    print()
    print(f"{joueur} c'est à votre tour.")
    print(f"Il reste {nbrAllumettes} allumettes.")
    nbrAllumettesRetirees = input_entier(1, limite_allumettes, f"Combien d'allumettes voulez-vous retirer, 1, 2 ou {limite_allumettes} : ", f"Veillez saisir un nombre entre 1 et {limite_allumettes}.")

    return nbrAllumettesRetirees