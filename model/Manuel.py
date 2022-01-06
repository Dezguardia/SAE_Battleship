# model/Manuel.py
#
from model.Joueur import getNomJoueur, type_joueur
from model.Grille import marquerCouleGrille
from model.Coordonnees import type_coordonnees
from model.Constantes import *

from view import window

def placerBateauManuel(player:dict) -> None :
    """
    Indique au joueur de placer ses bateaux et initie la phase de placement
    :param player: Le joueur qui va placer ses bateaux
    :return: None
    """
    if not type_joueur(player) :
        raise ValueError(f"Le joueur {player} n'est pas valide.")
    player_name=getNomJoueur(player)
    window.afficher(player)
    window.display_message(f"{player_name} : Placez vos bateaux.")
    window.placer_bateaux()

def choisirCaseTirManuel(player:dict) -> tuple :
    """
    Fait choisir une case au joueur et retourne ses coordonnées
    :param player: Dictionnaire représentant le joueur
    :return: Un tuple correspondant aux coordonnées de la case choisie par le joueur
    """

    if not type_joueur(player) :
        raise ValueError(f"Le joueur {player} n'est pas valide.")

    player_name = getNomJoueur(player)
    window.afficher(player)
    window.display_message(f"{player_name}: Choisissez la case où vous voulez tirer.")
    window.set_action("Choisissez la case de tir (clic gauche")
    cell = window.get_clicked_cell(2)

    #--Ce code supprime une valeur étrange se trouvant en trop dans le tuple, de la forme ((0,0),x)--#
    cell_test=list(cell)
    del cell_test[1]
    cell=tuple(cell_test[0])
    #-------#
    return cell


def traiterResultatTirManuel(player:dict,coord:tuple,rep:str) -> None :
    if not type_joueur(player) :
        raise ValueError(f"Le joueur {player} n'est pas valide.")
    if not type_coordonnees :
        raise ValueError(f"Le paramètre {coord} ne correspond pas à des coordonnées valides.")
    if type(rep) != str :
        raise ValueError(f"Le paramètre {rep} ne correspond pas à une chaîne de caractères.")
    grid=player.get(const.JOUEUR_GRILLE_TIRS)
    x=coord[0]
    y=coord[1]
    grid[x][y] = rep
    if rep == const.COULE :
        marquerCouleGrille(grid,coord)

def construireActeurManuel(player:dict) -> dict :
    if not type_joueur(player) :
        raise ValueError(f"Le joueur {player} n'est pas valide.")
    acteur = { const.ACTEUR : player,
               const.ACTEUR_PLACER_BATEAU : placerBateauManuel(player),
               const.ACTEUR_CHOISIR_CASE : choisirCaseTirManuel(player),
               const.ACTEUR_TRAITER_RESULTAT: traiterResultatTirManuel(player)}
    return acteur