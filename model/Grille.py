# Grille.py

from model.Constantes import *
from model.Case import type_case
from model.Coordonnees import type_coordonnees
from view.BattleCanvas import *

#
# - Définition de la grille des tirs
#       - tableau 2D (const.DIM x const.DIM) contenant des cases de type type_case.
#
# Bien qu'on pourrait créer une autre grille contenant les bateaux, ceux-ci seront stockés dans une liste
# et chaque bateau contiendra sa liste de coordonnées.
#


def type_grille(g: list) -> bool:
    """
    Détermine si le paramètre est une grille de cases dont le type est passé en paramètre ou non
    :param g: paramètre à tester
    :return: True s'il peut s'agir d'une grille du type voulu, False sinon.
    """
    res = True
    if type(g) != list or len(g) != const.DIM:
        res = False
    else:
        i = 0
        while res and i < len(g):
            res = type(g[i]) == list and len(g[i]) == const.DIM
            j = 0
            while res and j < len(g[i]):
                res = type_case(g[i][j])
                j += 1
            i += 1
    return res

def construireGrille() -> list :
    """
    Crée une grille de taille const.DIM x const.DIM
    :return: Retourne la grille
    """
    grille=[]
    for i in range(const.DIM) :
        row=[]
        for j in range(const.DIM) :
            row.append(None)
        grille.append(row)
    return grille

def marquerCouleGrille(grid:list,coord:tuple) -> None :
    """
    A FINIR
    :param grid:
    :param coord:
    :return:
    """
    if not type_grille(grid) :
        raise ValueError(f"Le paramètre {grid} ne correspond pas à une grille.")
    if not type_coordonnees(coord) :
        raise ValueError(f"Le paramètre {coord} ne correspond pas à des coordonnées.")

    lst = [coord]
    while lst:
        case = lst[0]
        del lst[0]
        x = case[0]
        y = case[1]
        grid[x][1] = const.COULE

        lst_vois=[(x,y+1),(x,y-1),(x+1,y),(x-1,y)]

        for i in range(len(lst_vois)) :
            case2=lst_vois[i]
            x2 = case2[0]
            y2 = case2[1]
            if grid[x2][y2] == const.TOUCHE :
                lst.append(case2)

