# Joueur.py

from model.Bateau import *
from model.Grille import type_grille, construireGrille, marquerCouleGrille
from model.Coordonnees import type_coordonnees
from model.Constantes import *
from view.BattleCanvas import *

#
# Un joueur est représenté par un dictionnaire contenant les couples (clé, valeur) suivants :
#  const.JOUEUR_NOM : Nom du joueur de type str
#  const.JOUEUR_LISTE_BATEAUX : Liste des bateaux du joueur
#  const.JOUEUR_GRILLE_TIRS : Grille des tirs sur les bateaux adverses
#  const.JOUEUR_GRILLE_ADVERSAIRE : une grille des tirs de l'adversaire pour tester la fonction de tir
#  de l'adversaire.
#


def type_joueur(joueur: dict) -> bool:
    """
    Retourne <code>True</code> si la liste semble correspondre à un joueur,
    <code>false</code> sinon.

    :param joueur: Dictionnaire représentant un joueur
    :return: <code>True</code> si le dictionnaire représente un joueur, <code>False</code> sinon.
    """
    return type(joueur) == dict and len(joueur) >= 4 and \
        len([p for p in [ const.JOUEUR_NOM, const.JOUEUR_LISTE_BATEAUX, const.JOUEUR_GRILLE_TIRS] if p not in joueur]) == 0 and \
        type(joueur[const.JOUEUR_NOM]) == str and type(joueur[const.JOUEUR_LISTE_BATEAUX]) == list \
        and type_grille(joueur[const.JOUEUR_GRILLE_TIRS]) \
        and all(type_bateau(v) for v in joueur[const.JOUEUR_LISTE_BATEAUX])

def construireJoueur(nom: str,lst: list) -> dict :
    """
    Construction d'un joueur à partir d'un nom et d'une liste de noms de bateaux
    Le programme crée une liste de bateaux à partir de leur nom
    :param nom: Nom du joueur
    :param lst: Liste des noms des bateaux
    :return: Retourne un joueur représenté par un dictionnaire
    """

    playerGrid = construireGrille()
    advGrid = construireGrille()
    lst_bat=[]
    for i in range(len(lst)):
        lst_bat.append(construireBateau(lst[i]))

    player = {const.JOUEUR_NOM: nom,
              const.JOUEUR_LISTE_BATEAUX: lst_bat,
              const.JOUEUR_GRILLE_TIRS: playerGrid,
              const.JOUEUR_GRILLE_ADVERSAIRE: advGrid}
    return player

def getNomJoueur(player:dict) -> str :
    """
    Retourne le nom d'un joueur
    :param player: Le dictionnaire représentant le joueur
    :return: Str du nom du joueur
    """
    if not type_joueur(player):
        raise ValueError(f"L'objet {player} ne correspond pas ")
    return player.get(const.JOUEUR_NOM)

def getNombreBateauxJoueur(player:dict) -> int :
    """
    Donne le nombre de bateaux d'un joueur
    :param player: Le dictionnaire du joueur
    :return: Int du nombre de bateaux
    """
    if not type_joueur(player):
        raise ValueError(f"L'objet {player} ne correspond pas ")
    return len(player.get(const.JOUEUR_LISTE_BATEAUX))

def getBateauxJoueur(player:dict) -> list :
    """
    Donne la liste des bateaux du joueur
    :param player: dictionnaire représentant le joueur
    :return: Liste des bateaux
    """
    if not type_joueur(player):
        raise ValueError(f"L'objet {player} ne correspond pas ")
    return player.get(const.JOUEUR_LISTE_BATEAUX)

def getGrilleTirsJoueur(player:dict) -> list :
    """
    Donne la grille des tirs du joueur
    :param player: dictionnaire du joueur
    :return: la grille du joueur
    """
    if not type_joueur(player):
        raise ValueError(f"L'objet {player} ne correspond pas ")
    return player.get(const.JOUEUR_GRILLE_TIRS)

def getGrilleTirsAdversaire(player:dict) -> list :
    """
    Donne la grille des tirs de l'adversaire
    :param player: dictionnaire du joueur
    :return: la grille de l'adversaire
    """
    if not type_joueur(player):
        raise ValueError(f"L'objet {player} ne correspond pas ")
    return player.get(const.JOUEUR_GRILLE_ADVERSAIRE)


#---------------------------------------------#

def placerBateauJoueur(player:dict,bateau:dict,first_case:tuple,posHorizon:bool) -> bool :
    if not type_joueur(player):
        raise ValueError(f"L'objet {player} ne correspond pas ")
    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} n'est pas un bateau valide.")
    if not type_coordonnees(first_case):
        raise ValueError(f"Les coordonnées {first_case} ne sont pas valides.")
    if bateau not in getBateauxJoueur(player) :
        raise RuntimeError(f"Le bateau {bateau} ne fait pas partie des bateaux du joueur {player}.")

    bateauJoueur = getBateauxJoueur(player)
    taille = getTailleBateau(bateau)

    valide = True
    if peutPlacerBateau(bateau, first_case, posHorizon) == False:
        valide = False

    else :
        bateau2 = bateau.copy()
        placerBateau(bateau2, first_case, posHorizon)

        for i in range(taille):
            if getCoordonneesBateau(bateau2) == getCoordonneesBateau(bateauJoueur[i]):
                return valide

            else:
                if sontVoisinsBateau(bateau2, bateauJoueur[i]) == True :
                    valide = False

        if valide:
            placerBateau(bateau, first_case, posHorizon)

    return valide


#---------------------------------------------#

def reinitialiserBateauxJoueur(player:dict) -> None :
    """
    Réinitialise les bateaux d'un joueur
    :param player:
    :return:
    """
    if not type_joueur(player):
        raise ValueError(f"L'objet {player} ne correspond pas ")
    nbr=getNombreBateauxJoueur(player)
    for i in range(nbr) :
        reinitialiserBateau(getBateauxJoueur(player)[i])

#---------------------------------------------#


def repondreTirJoueur(player:dict,coord:tuple)-> str :
    if not type_joueur(player):
        raise ValueError(f"L'objet {player} ne correspond pas ")
    if not type_coordonnees(coord) :
        raise ValueError(f"Les coordonnées {coord} ne sont pas valides.")
    res=const.RATE
    lst_bat=getBateauxJoueur(player)
    for i in range(len(lst_bat)) :
        bateau=lst_bat[i]
        lst_seg = getSegmentsBateau(bateau)
        for j in range(len(lst_seg)) :
            segment=lst_seg[j]
            if segment.get(const.SEGMENT_COORDONNEES) == coord :
                res= const.TOUCHE
                setEtatSegmentBateau(bateau,coord,const.TOUCHE)
                if estCouleBateau(bateau) :
                    res = const.COULE
    if res == const.COULE :
        gridadv=player.get(const.JOUEUR_GRILLE_ADVERSAIRE)
        marquerCouleGrille(gridadv,coord)
    return res










