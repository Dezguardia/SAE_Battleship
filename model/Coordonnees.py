# Coordonnees.py

#
# - Définit les coordonnées d'une case
#
#  Une coordonnée est un tuple de deux entiers compris entre 0 (inclus) et const.DIM (exclus)
#  Elle peut aussi être None si elle est non définie
#

from model.Constantes import *


def type_coordonnees(c: tuple) -> bool:
    """
    Détermine si le tuple correspond à des coordonnées
    Les coordonnées sont sous la forme (ligne, colonne).
    Malheureusement, il n'est pas possible de tester si une inversion est faite entre ligne et colonne...

    :param c: coordonnées
    :return: True s'il s'agit bien de coordonnées, False sinon
    """
    return c is None or (type(c) == tuple and len(c) == 2 and 0 <= c[0] < const.DIM and 0 <= c[1] < const.DIM)


def sontVoisins(coord1:tuple,coord2:tuple) -> bool :
    """
    Vérifie si deux coordonnées sont voisines en calculant la différence entre les coordonnées x et y
    :param coord1: Tuple des coordonnées 1
    :param coord2: Tuple des coordonnées 2
    :return: True si voisines, False sinon
    """

    if not type_coordonnees(coord1) or not type_coordonnees(coord2) or coord1 == None or coord2 == None:
        raise ValueError("Les coordonnées entrées ne sont pas correctes")

    res = False

    if coord1[0] == coord2[0] and coord1[1] == coord2[1]:
        res = False

    elif (coord1[0] - coord2[0] == 1 or coord1[0] - coord2[0] == -1 or coord1[0] - coord2[0] == 0) \
            and (coord1[1] - coord2[1] == 1 or coord1[1] - coord2[1] == -1 or coord1[1] - coord2[1] == 0):
        res = True

    return res
