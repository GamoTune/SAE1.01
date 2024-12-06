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
    boucle: bool = True


    #Saisie des noms des joueurs
    clear_console()

    while boucle:
        print()
        print("/---------------------------------------\\")
        print("      Saisie des noms des joueurs")
        print()
        joueur1 = str(input("Saisir le prénom du premier joueur : "))
        while joueur1 == "" :
            joueur1=str(input("Veuillez rentrer un prénom valide : "))

        joueur2 = str(input("Saisir le prénom du second joueur : "))
        while joueur2 == "" :
            joueur2=str(input("Veuillez rentrer un prénom valide : "))
        
        if joueur1 == joueur2:
            clear_console()
            print("Les noms des joueurs ne peuvent pas être identiques.")
        else:
            boucle = False

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
    boucle: bool = True

    input_ = input(message)
    while not input_.isdigit():
        print(erreur)
        input_ = input(message)
    nombre = int(input_)

    while boucle:
        if input_.isdigit():
            nombre = int(input_)
            if borneMin <= nombre <= borneMax:
                boucle = False
            else:
                print(erreur)
                input_ = input(message)
        else:
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


def sauvegarde_data(jeu:str, data:dict) -> None:
    """
    Procédure pour sauvegarder les données d'un jeu
    Args:
        jeu(str): Nom du jeu.
        data(dict): Dictionnaire contenant les données.

    Returns:
        (None) : Ne retourne rien.
    """
    
    #Déclaration des variables
    chemin: str

    #Sauvegarde des données
    chemin = os.getcwd() + "/scores/" + jeu + ".bin"
    with open(chemin, "wb") as fichier:
        pickle.dump(data, fichier)



#La fonction sauvegarde_score_joueur permet de sauvegarder les scores d'un joueur sur un jeu en particulier
def sauvegarde_score_joueur(jeu:str, joueur:str, valeur:float) -> None:
    """
    Procédure pour sauvegarder les scores d'un joueur
    Args:
        jeu(str): Nom du jeu.
        joueur(str): Nom du joueur.
        valeur(float): Valeur du score.

    Returns:
        (None) : Ne retourne rien.
    """

    #Déclaration des variables
    data: dict
    scoresJoueurs: list

    #Chargement des scores
    data = charger_score(jeu)

    #Chargement des scores du joueur
    scoresJoueurs = charger_score_joueur(jeu, joueur)

    #Sauvegarde du score
    scoresJoueurs.append(valeur)
    data[joueur] = scoresJoueurs

    #Sauvegarde des scores
    sauvegarde_data(jeu, data)



#La fonction charger_score permet de charger les scores d'un jeu en particulier
def charger_score(jeu:str) -> dict:
    """
    Fonction pour charger les scores d'un jeu en particulier
    Args:
        jeu(str): Nom du jeu.
    
    Returns:
        data(dict): Dictionnaire contenant les scores.
    """

    #Déclaration des variables
    chemin: str
    data: dict

    #Chargement des scores
    chemin = os.getcwd() + "/scores/" + jeu + ".bin"
    if os.path.exists(chemin):
        try:
            with open(chemin, "rb") as fichier:
                data = pickle.load(fichier)
        except:
            data = {}
            sauvegarde_data(jeu, data)

    else: #Si le fichier n'existe pas, on renvoie un dictionnaire vide
        data = {}
    return data

#La fonction charger_score_joueur permet de charger les scores d'un joueur sur un jeu en particulier
def charger_score_joueur(jeu:str, joueur:str) -> list:
    """
    Fonction pour charger les scores d'un joueur sur un jeu en particulier
    Args:
        jeu(str): Nom du jeu.
        joueur(str): Nom du joueur.
    
    Returns:
        scoreJoueurs(dict): Dictionnaire contenant les scores du joueur.
    """

    #Déclaration des variables
    data: dict
    scoreJoueurs: list

    #Chargement des scores
    data = charger_score(jeu)

    #Vérification de l'existence du joueur
    if joueur in data:
        scoreJoueurs = data[joueur]
    else: #Si le joueur n'existe pas, on renvoie une liste vide
        scoreJoueurs = []

    #Retourne le dictionnaire des scores du joueur (vide si le joueur n'existe pas)
    return scoreJoueurs



def reset_score():
    """
    Procédure pour réinitialiser les scores
    Args:
        (None) : Ne prend pas de paramètres.

    Returns:
        (None) : Ne retourne rien.
    """

    #Déclaration des variables
    chemin: str

    #Réinitialisation des scores
    chemin = os.getcwd() + "/scores/"
    for fichier in os.listdir(chemin): #On parcourt tous les fichiers de scores pour les réinitialiser avec un dictionnaire vide
        sauvegarde_data(fichier, {})
    print("Les scores ont été réinitialisés avec succès !")





def verification_type(value: str, type_:type) -> bool:
    """
    Fonction pour vérifier si la valeur est du type demandé
    Args:
        value(str): Valeur à vérifier.
        type_(type): Type demandé.

    Returns:
        (bool): True si la valeur est du type demandé, False sinon.
    """

    return isinstance(value, type_)


def input_choix(choix:list[str], message:str, erreur:str) -> str:
    """
    Fonction pour vérifier si l'entrée utilisateur est un choix valide
    Args:
        choix(list[str]): Liste des choix possibles.
        message(str): Message à afficher.
        erreur(str): Message d'erreur à afficher.

    Returns:
        nombre(int): Nombre entré par l'utilisateur.
    """

    #Déclaration des variables
    input_: str

    #Saisie de l'entrée utilisateur
    input_ = input(message)
    while input_ not in choix:
        print(erreur)
        input_ = input(message)
    return input_



def tri_de_liste(tab: list) -> list:
    """
    Fonction pour trier une liste par insertion
    Args:
        tab(list): Liste à trier.

    Returns:
        tab(list): Liste triée.
    """

    #Déclaration des variables
    n: int
    i: int
    cle: int
    j: int

    #Tri par insertion
    n = len(tab)
    for i in range(1, n):
        cle = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = cle
    return tab


def trier_scores(scores: dict) -> dict:
    """
    Fonction pour trier un dictionnaire de scores par ordre décroissant des scores
    Args:
        scores(dict): Dictionnaire contenant les scores des joueurs.

    Returns:
        dict: Dictionnaire trié par ordre décroissant des scores.
    """
    # Calculer la somme des scores pour chaque joueur
    scores_sommes = {joueur: sum(score) for joueur, score in scores.items()}
    
    # Trier les joueurs par ordre décroissant des scores
    joueurs_tries = tri_de_liste(list(scores_sommes.items()))
    joueurs_tries.reverse()  # Inverser pour obtenir l'ordre décroissant

    # Reconstituer le dictionnaire trié
    scores_tries = {joueur: scores[joueur] for joueur, _ in joueurs_tries}
    
    return scores_tries