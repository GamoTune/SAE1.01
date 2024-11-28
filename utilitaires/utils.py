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
    chemin: str
    data: dict
    scoresJoueurs: list

    #Chargement des scores
    chemin = os.getcwd() + "/scores/" + jeu + ".txt"
    data = charger_score(jeu)

    #Chargement des scores du joueur
    scoresJoueurs = charger_score_joueur(jeu, joueur)

    #Sauvegarde du score
    scoresJoueurs.append(valeur)
    data[joueur] = scoresJoueurs

    #Sauvegarde des scores
    with open(chemin, "wb") as fichier:
        pickle.dump(data, fichier)



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
    chemin = os.getcwd() + "/scores/" + jeu + ".txt"
    if os.path.exists(chemin):
        with open(chemin, "rb") as fichier:
            data = pickle.load(fichier)
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
    for fichier in os.listdir(chemin):
        with open(chemin + fichier, "wb") as fichier:
            pickle.dump({}, fichier)
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

    #Déclaration des variables

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