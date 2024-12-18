########################################################################################
#Ce fichier contient le jeu du morpion
########################################################################################

#Importation des fonctions
import sys
sys.path.append("./")
from utilitaires.utils import input_entier, login_joueur, clear_console, input_choix, sauvegarde_score_joueur

#Programme principal du jeu
def morpion() -> None:
    """
    Cette fonction est la fonction principale du jeu du morpion. Elle permet de jouer à ce jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette fonction.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    
    #Déclaration des variables à utilisé
    boucle: bool = True

    nomJoueur1: str
    nomJoueur2: str

    signeJoueur1: str
    signeJoueur2: str

    nbrCoupsJoueur1: int = 0
    nbrCoupsJoueur2: int = 0

    dernierJoueur: str = ""
    vainqueur: str = ""

    scoreJoueur1: float = 0
    scoreJoueur2: float = 0

    grille = [[" " for _ in range(3)] for _ in range(3)]


    #Initialisation du jeu

    nomJoueur1, nomJoueur2 = login_joueur()
    signeJoueur1 = input_choix(["X", "O"], f"Veuillez choisir un signe pour {nomJoueur1} (X, O) : ", f"Veuillez choisir un signe pour {nomJoueur1} (X, O) : ")
    signeJoueur2 = "X" if signeJoueur1 == "O" else "O"

    #Début du jeu


    #Tant que la grille n'est pas pleine
    while (nbrCoupsJoueur1 + nbrCoupsJoueur2) < 9 and boucle:

        clear_console()
        print("/-----------------------------------------------------------\\")
        print("                      Jeu du morpion")

        dernierJoueur = nomJoueur1 if (nbrCoupsJoueur1 + nbrCoupsJoueur2) % 2 == 0 else nomJoueur2

        if dernierJoueur == nomJoueur1:
            grille = tour(nomJoueur1, signeJoueur1, grille)
            nbrCoupsJoueur1 += 1
        else:
            grille = tour(nomJoueur2, signeJoueur2, grille)
            nbrCoupsJoueur2 += 1
        
        boucle = verification_jeu_continue(grille)


    #Détermination du vainqueur
    if not boucle:
        vainqueur = dernierJoueur
    else:
        vainqueur = "Personne"


    #Calcul du score
    scoreJoueur1 = calcul_score(vainqueur, nomJoueur1, nbrCoupsJoueur1)
    scoreJoueur2 = calcul_score(vainqueur, nomJoueur2, nbrCoupsJoueur2)


    #Sauvegarde du score
    sauvegarde_score_joueur("morpion", nomJoueur1, scoreJoueur1)
    sauvegarde_score_joueur("morpion", nomJoueur2, scoreJoueur2)





    #Fin du jeu
    clear_console()
    affichage_grille(grille)
    print()
    print("/-----------------------------------------------------------\\")
    print("                        Fin du jeu")
    print()
    if vainqueur == nomJoueur1:
        print(f"Bravo {nomJoueur1} vous avez gagné en {nbrCoupsJoueur1} coups.")
        print(f"{nomJoueur2} vous avez perdu en {nbrCoupsJoueur2} coups.")
    elif vainqueur == nomJoueur2:
        print(f"Bravo {nomJoueur2} vous avez gagné en {nbrCoupsJoueur2} coups.")
        print(f"{nomJoueur1} vous avez perdu en {nbrCoupsJoueur1} coups.")
    else:
        print("Match nul")
        print(f"{nomJoueur1} a joué {nbrCoupsJoueur1} coups et à gagné {scoreJoueur1} points.")
        print(f"{nomJoueur2} a joué {nbrCoupsJoueur2} coups et à gagné {scoreJoueur2} points.")
    print()
    print(f"Score de {nomJoueur1} : {scoreJoueur1}")
    print(f"Score de {nomJoueur2} : {scoreJoueur2}")
    print()
    print("\\-----------------------------------------------------------/")




def calcul_score(vainqueur: str, nomJoueur: str, nbrCoups: int) -> float:
    """
    Cette fonction permet de calculer le score d'un joueur.

    Args:
        vainqueur (str): Nom du joueur vainqueur.
        nomJoueur (str): Nom du joueur.
        nbrCoups (int): Nombre de coups du joueur.


    Returns:
        (float): Le score du joueur.
    """

    #Déclaration des variables
    score: float = 0


    #Calcul du score
    if vainqueur == nomJoueur:
        score = 5*(nbrCoups - 1/nbrCoups)
    else:
        score = 2.5*(nbrCoups - 1/nbrCoups)


    return round(score, 2)



def affichage_grille(grille: list[list[str]]) -> None:
    """
    Cette fonction permet d'afficher la grille du jeu.

    Args:
        grille (list[list[str]]): Grille du jeu.

    Returns:
        (None): Cette fonction ne retourne rien.
    """

    #Déclaration des variables
    i: int

    #Affichage de la grille
    print(f"|-  1  -|-  2  -|-  3  -|")
    for i in range(3):
        print(f"        |       |       |")
        print(f"{i+1}   {grille[i][0]}   |   {grille[i][1]}   |   {grille[i][2]}   |")
        print(f"        |       |       |")
        print(f"|-------|-------|-------|")


    return




#Fonction pour afficher le tour du joueur
def tour(joueur:str, signe:str, grille: list[list[str]]) -> list[list[str]]:
    """
    Cette fonction permet d'afficher le tour du joueur et le nombre d'allumettes restantes.

    Args:
        joueur (str): Nom du joueur.
        signe (str): Signe du joueur.
        grille (list[list[str]]): Grille du jeu.

    Returns:
        grille (list[list[str]]): Grille du jeu.
    """

    #Déclaration des variables
    ligne: int
    colonne: int

    #Affichage du tour du joueur
    print(f"Tour de {joueur}")
    print()
    affichage_grille(grille)
    print()
    print("Veuillez choisir une case")
    print()
    ligne, colonne = input_entier(1, 3, "Veuillez choisir une ligne (1, 2, 3) : ", "Veuillez choisir une ligne (1, 2, 3) : "), input_entier(1, 3, "Veuillez choisir une colonne (1, 2, 3) : ", "Veuillez choisir une colonne (1, 2, 3) : ")

    #Vérification de la case
    while grille[ligne-1][colonne-1] != " ":
        print("Case déjà occupée")
        ligne, colonne = input_entier(1, 3, "Veuillez choisir une ligne (1, 2, 3) : ", "Veuillez choisir une ligne (1, 2, 3) : "), input_entier(1, 3, "Veuillez choisir une colonne (1, 2, 3) : ", "Veuillez choisir une colonne (1, 2, 3) : ")

    #Modification de la grille
    grille[ligne-1][colonne-1] = signe

    return grille


def verification_jeu_continue(grille: list[list[str]]) -> bool:
    """
    Cette fonction permet de vérifier si le jeu doit continuer ou non.
    
    Args:
        grille: List[List[str]]: La grille du jeu
        
    Returns:
        bool: True si le jeu doit continuer, False sinon
    """

    #Déclaration des variables
    lignes: list[str]
    boucle: bool = True
    taille: int = 3
    i: int

    #Vérification de la grille
    #Vérification des lignes 
    for lignes in grille:
        if lignes.count(lignes[0]) == taille and lignes[0] != " ":
            boucle = False

    #Vérification des colonnes
    for i in range(taille):
        if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] != " ":
            boucle = False

    #Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != " ":
        boucle = False

    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] != " ":
        boucle = False

    return boucle