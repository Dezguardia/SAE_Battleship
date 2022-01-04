# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#

from model.Segment import type_segment, construireSegment
from model.Constantes import *



def type_bateau(bateau: dict) -> bool:
    """
    Détermine si la liste représente un bateau

    :param bateau: Liste représentant un bateau
    :return: <code>True</code> si la liste contient bien un bateau, <code>False</code> sinon.
    """
    return type(bateau) == dict and \
        all([v in bateau for v in [const.BATEAU_NOM, const.BATEAU_SEGMENTS]]) and \
        type(bateau[const.BATEAU_NOM]) == str and \
        bateau[const.BATEAU_NOM] in const.BATEAUX_CASES and type(bateau[const.BATEAU_SEGMENTS]) == list and \
        len(bateau[const.BATEAU_SEGMENTS]) == const.BATEAUX_CASES[bateau[const.BATEAU_NOM]] and \
        all([type_segment(s) for s in bateau[const.BATEAU_SEGMENTS]])


def construireBateau(nom: str) -> dict :
    """
    Construit un objet bateau à partir de son nom
    :param nom: Le nom du bateau. S'il se trouve dans les noms valides, lui attribue un nombre de cases et
    construit autant de segments que ce nombre
    :return: Retourne un dictionnaire correspondant au bateau
    """
    if nom not in const.BATEAUX_CASES :
        raise ValueError(f"Le nom {nom} ne correspond pas à un type de bateau.")
    else:

        nb = const.BATEAUX_CASES.get(nom)
        lst_seg =[]

        for i in range(nb):
            seg = construireSegment()
            lst_seg.append(seg)

        bateau = {const.BATEAU_NOM : nom, const.BATEAU_SEGMENTS : lst_seg}
        return bateau

def getNomBateau(bateau:dict) -> str :
    """
    La fonction retourne le nom du bateau à partir du dictionnaire en paramètre
    :param bateau: Le dictionnaire représentant le bateau
    :return: le nom du bateau
    """
    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} passé en paramètre n'est pas un bateau.")
    else:
        return bateau.get(const.BATEAU_NOM)

def getTailleBateau(bateau:dict) -> int :
    """
    Donne la taille d'un bateau passé en paramètre
    :param bateau: Dictionnaire correspondant au bateau
    :return: Le nombre de segments du bateau
    """
    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} passé en paramètre n'est pas un bateau.")
    else :
        return len(bateau.get(const.BATEAU_SEGMENTS))

def getSegmentsBateau(bateau:dict) -> list :
    """
    Donne une liste des segments du bateau
    :param bateau: Le dictionnaire correspondant au bateau
    :return: la liste des segments
    """
    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} passé en paramètre n'est pas un bateau.")
    else:
        return bateau.get(const.BATEAU_SEGMENTS)


def getSegmentBateau(bateau: dict, num: object) -> dict :
    """
    Permet de sélectionner un segment d'un bateau à partir de ses coordonnées ou de sa position
    dans la liste des segments
    :param bateau: Le dictionnaire correspondant au bateau
    :param num: Les coordonnées du segment choisi OU sa position dans la liste des segments
    :return: Le segment choisi
    """

    taille = getTailleBateau(bateau)
    seg = getSegmentsBateau(bateau)

    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} passé en paramètre n'est pas un bateau.")

    elif type(num) == int :

        if num < 0 or num >= taille :
            raise ValueError(f"Le numéro de segment {num} n'est pas valide.")

        else :
            return seg[num]

    elif type(num) == tuple :
        valide = False
        cpt=0
        for i in range(taille) :
            if num == seg[i].get(const.SEGMENT_COORDONNEES) :
                valide = True
                break
            cpt+=1
        if valide :
            return seg[cpt]
        else :
            raise ValueError(f"Les coordonnées {num} ne sont pas valides.")
    else :
        raise ValueError(f"Le type du second paramètre {type(num)} ne correspond pas")

def setSegmentBateau(bateau:dict,num:int,segment:dict) -> None :
    """
    Remplace un segment choisi d'un bateau par un segment passé en paramètre
    :param bateau: Le dictionnaire correspondant au bateau
    :param num: le numéro du segment dans la liste des segments
    :param segment: Le segment qui remplacera l'ancien segment
    :return: Rien
    """

    taille = getTailleBateau(bateau)
    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} passé en paramètre n'est pas un bateau.")
    elif num < 0 or num >= taille:
        raise ValueError(f"Le numéro de segment {num} n'est pas valide.")
    elif not type_segment(segment) :
        raise ValueError(f"L'objet {segment} passé en paramètre n'est pas un segment.")
    else:
        seg_list = getSegmentsBateau(bateau)
        seg_list[num] = segment


def getCoordonneesBateau(bateau:dict) -> list :
    """
    Crée une liste contenant les coordonnées de tous les segments d'un bateau
    :param bateau: Le dictionnaire correspondant au bateau
    :return: La liste des coordonnées
    """
    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} passé en paramètre n'est pas un bateau.")
    else :
        segs = getSegmentsBateau(bateau)
        coord_list=[]
        for i in range(len(segs)) :
            coord_list.append(segs[i].get(const.SEGMENT_COORDONNEES))
        return coord_list






