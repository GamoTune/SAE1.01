#Importation des fonctions
import sys, os
sys.path.append("./utilitaires")
from utils import input_entier, login_joueur, clear_console #type: ignore


def devinette() :
    """
    Cette procédure est la procédure principale du jeu de la devinette. Elle permet de jouer à ce jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette preocédure.

    Returns:
        (None): Cette procédure ne retourne rien.
    """
    clear_console()
    #déclaration des variables utilisées dans cette procédure
    joueur1 : str
    joueur2 : str
    coup : int
    nombre : int
    choix : int
    scoreJ1 : int
    scoreJ2 : int
    gagné : bool
    limite : int
    choix : int
    proposition : int

    gagné = False
    coup = 0
    nombre = 0

    print("/-------------------------------------\\")
    
    print()
    joueur1, joueur2 = login_joueur()

    limite = int(input("Joueur 1 entrez la limite maximum : "))
    nombre = input_entier(0, limite, f"{joueur1} entrez votre nombre et souvenez vous en : ", "Erreur, votre nombre est supérieur à la limite, veuillez saisir un nombre valide :") 
    while nombre>limite :
        nombre= int(input(f"Erreur, {nombre} est supérieur à la limite, veuillez saisir un nombre valide :"))
    clear_console()
    print(f"La limite est : {limite}")
    while gagné == False :

        proposition = input_entier(0, limite, f"{joueur2}, faites une proposition : ", "Erreur, le nombre rentré n'est pas compris dans la limite")
        coup = coup+1

        print("---------------------------------------")
        print(f"{joueur1}, donnez une indication au Joueur 2 :")
        print("1. Trop petit")
        print("2. Trop grand")
        print("3. C'est gagné")
        
        choix = input_entier(1, 3, f"{joueur1}, comment est le nombre de {joueur2} ? :", "Erreur votre choix n'existe pas")
        
        clear_console()
        if choix == 1 :
            print(f"{joueur2}, votre nombre est trop petit")
        if choix == 2 :
            print(f"{joueur2} votre nombre est trop grand")
        if choix == 3 :
            gagné = True


    print(f"Bravo {joueur2} vous avez trouvé le nombre en {coup} coups")
    return

print(devinette())