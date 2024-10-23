def login_joueur() ->tuple[str, str] :
    """
    Procédure servant à attribuer un nom aux joueurs
    Args:
        (None) : rien

    Return:
        joueur1(str): Nom du joueur 1
        joueur2(str): Nom du joueur 2

    """
    joueur1 : str 
    joueur2 : str

    joueur1=str(input("Saisir le prénom du premier joueur : "))
    joueur2=str(input("Saisir le prénom du second joueur : "))
    
    return (joueur1, joueur2)
