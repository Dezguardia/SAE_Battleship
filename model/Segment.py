# model/Segment.py

from model.Coordonnees import type_coordonnees
from model.Etat import type_etat_segment
from model.Constantes import *
#
# définit un segment de bateau :
# Un segment de bateau est un dictionnaire contenant les couples (clé, valeur) suivants :
#   - const.SEGMENT_COORDONNEES : Les coordonnées du segment sur la grille
#   - ccnst.SEGMENT_ETAT : L'état du segment (const.RATE ou const.TOUCHE)
#


def type_segment(objet: dict) -> bool:
    """
    Détermine si l'objet passé en paramètre peut être interprété ou non
    comme un segment de bateau.

    :param objet: Objet à analyser
    :return: True si l'objet peut correspondre à un segment
    False sinon.
    """
    return type(objet) == dict and \
           all([k in objet for k in [const.SEGMENT_COORDONNEES, const.SEGMENT_ETAT]]) \
           and type_coordonnees(objet[const.SEGMENT_COORDONNEES]) \
           and type_etat_segment(objet[const.SEGMENT_ETAT])


def construireSegment(coord: tuple = None) -> dict:
    """
    Construit un segment à partir de coordonnées (initialisées à None)
    :param coord: coordonnées du segment
    :return: Le segment construit, comprenant 2 couples
    """
    if not type_coordonnees(coord):
        raise ValueError("Les coordonnées ne sont pas correctes.")
    else:
        d = {const.SEGMENT_COORDONNEES: coord, const.SEGMENT_ETAT: const.INTACT}
        return d


def getCoordonneesSegment(segment: dict) -> tuple :
    """
    Donne les coordonnées d'un segment passé en paramètre.
    :param segment: Segment
    :return: le tuple indiquant les coordonnées
    """
    if not type_segment(segment):
        raise ValueError(f"Le paramètre {segment} n'est pas de type Segment.")
    else:
        coord=segment.get(const.SEGMENT_COORDONNEES)
        return coord

def getEtatSegment(segment: dict) -> str :
    """
    Renvoie l'état d'un segment passé en paramètre (Touché ou Intact)
    :param segment: Segment
    :return: l'état du segment
    """
    if not type_segment(segment):
        raise ValueError(f"Le paramètre {segment} n'est pas de type Segment.")
    else:
        etat=segment.get(const.SEGMENT_ETAT)
        return etat

def setCoordonneesSegment(segment: dict, coord: tuple) -> None :
    """
    Remplace les coordonnées d'un segment par les coordonnées passées en paramètre
    :param segment: Le segment
    :param coord: Nouvelles coordonnées
    :return: Rien, ne fait que changer les coordonnées
    """
    if not type_segment(segment) :
        raise ValueError(f"Le paramètre {segment} n'est pas de type Segment.")
    elif not type_coordonnees(coord):
        raise ValueError(f"Les coordonnées {coord} ne sont pas correctes.")
    else :
        segment[const.SEGMENT_COORDONNEES] = coord

def setEtatSegment(segment:dict, etat:str) -> None :
    """
    Remplace l'état d'un segment par l'état passé en paramètre
    :param segment: Le segment passé en paramètre
    :param etat: Le nouvel état
    :return: Rien, ne fait que changer l'état
    """
    if not type_segment(segment) :
        raise ValueError(f"Le paramètre {segment} n'est pas de type Segment.")
    elif not type_etat_segment(etat):
        raise ValueError(f"Le paramètre {etat} n'est pas un état valide")
    else:
        segment[const.SEGMENT_ETAT] = etat