# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#

from model.Segment import type_segment, construireSegment
from model.Coordonnees import type_coordonnees, sontVoisins
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

        else:
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


#-----------------PLACER LES BATEAUX------------------#

def peutPlacerBateau(bateau:dict,first_case:tuple,pos:bool) -> bool :
    """
    Vérifie si un bateau peut être placé en fonction de ses coordonnées
    :param bateau: Dictionnaire représentant le bateau
    :param first_case: Coordonnées de sa première case
    :param pos: Booléen : si True, le bateau est à l'horizontale, sinon il est à la verticale
    :return: True si le bateau peut être placé aux coordonnées, False sinon
    """

    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} passé en paramètre n'est pas un bateau.")
    if not type_coordonnees(first_case) or first_case == None :
        raise ValueError(f"Les coordonnées {first_case} ne sont pas valides.")

    taille=getTailleBateau(bateau)
    res = False
    if 0 <= first_case[0] <= const.DIM and 0 <= first_case[1] <= const.DIM:
        if pos :
            if first_case[1] + taille <= const.DIM :
                res = True
        else :
            if first_case[0] + taille <= const.DIM :
                res = True
        return res
    else :
        raise ValueError(f"Les coordonnées {first_case} ne se trouvent pas dans la grille")

def estPlaceBateau(bateau:dict) -> bool :
    """
    Vérifie si un bateau est placé
    :param bateau: Dictionnaire représentant le bateau
    :return: True si le bateau est placé (aucun segment aux coordonnées none), False sinon
    """
    if not type_bateau(bateau):
        raise ValueError(f"L'objet {bateau} passé en paramètre n'est pas un bateau.")
    lst_seg=bateau.get(const.BATEAU_SEGMENTS)
    estPlace=True
    for i in range(len(lst_seg)) :
        if lst_seg[i].get(const.SEGMENT_COORDONNEES) == None :
            estPlace = False
            break
    return estPlace


def sontVoisinsBateau(bateau1:dict,bateau2:dict) -> bool :
    """
    Vérifie si deux bateaux sont voisins en analysant si leurs coordonnées sont adjacentes
    :param bateau1: Dictionnaire du premier bateau
    :param bateau2: Dictionnaire du deuxième bateau
    :return: True si les bateaux sont voisins, False sinon
    """
    if not type_bateau(bateau1) or not type_bateau(bateau2) :
        raise ValueError("Au moins l'un des deux bateaux n'est pas valide")

    res=False
    taille_1=getTailleBateau(bateau1)
    taille_2=getTailleBateau(bateau2)
    lst_seg_1 = bateau1.get(const.BATEAU_SEGMENTS)
    lst_seg_2 = bateau2.get(const.BATEAU_SEGMENTS)
    for i in range(taille_1) :
        seg= lst_seg_1[i].get(const.SEGMENT_COORDONNEES)
        for j in range(taille_2) :
            seg2=lst_seg_2[j].get(const.SEGMENT_COORDONNEES)
            if sontVoisins(seg,seg2) :
                res = True
                break
    return res



def placerBateau(bateau:dict,first_case:tuple,posHorizon:bool) -> None :
    """
    Vient placer le bateau passé en paramètre à partir de la coordonnée first_case et de son orientation
    :param bateau: Dictionnaire du bateau
    :param first_case: Tuple des coordonnées de la première case du bateau
    :param posHorizon: Bool : si True, le bateau est horizontal, sinon il est vertical
    :return: None
    """
    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} n'est pas un bateau valide.")
    if not type_coordonnees(first_case):
        raise ValueError(f"Les coordonnées {first_case} ne sont pas valides.")
    if not peutPlacerBateau(bateau,first_case,posHorizon) :
        raise RuntimeError("Le bateau ne peut pas être placé à ces coordonnées")
    taille=getTailleBateau(bateau)

    if posHorizon :
        for i in range(taille) :
            seg = getSegmentBateau(bateau,i)
            seg[const.SEGMENT_COORDONNEES]=first_case
            test=list(first_case)
            test[1]+=1
            first_case=tuple(test)

    else :
        for i in range(taille) :
            seg = getSegmentBateau(bateau,i)
            seg[const.SEGMENT_COORDONNEES]=first_case
            test=list(first_case)
            test[0]+=1
            first_case=tuple(test)

def reinitialiserBateau(bateau:dict) -> None :
    """
    Réinitialise les coordonnées et l'état d'un bateau
    :param bateau: Dictionnaire du bateau
    :return: None
    """
    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} n'est pas un bateau valide.")
    taille=getTailleBateau(bateau)
    lst_seg=bateau.get(const.BATEAU_SEGMENTS)
    for i in range(taille) :
        lst_seg[i][const.SEGMENT_COORDONNEES]=None
        lst_seg[i][const.SEGMENT_ETAT]=const.INTACT

def est_horizontal_bateau(bateau: dict) -> bool:
    """
    Retourne True si le bateau est horizontal, False si il est vertical.

    :param bateau:
    :return: True si le bateau est horizontal, False si il est vertical
    :raise ValueError si le bateau n'est pas placé ou s'il n'est ni vertical, ni horizontal
    """
    if not estPlaceBateau(bateau):
        raise ValueError("est_horizontal_bateau: Le bateau n'est pas positionné")
    pos = getCoordonneesBateau(bateau)
    res = True
    if len(pos) > 1:
        # Horizontal : le numéro de ligne ne change pas
        res = pos[0][0] == pos[1][0]
        # On vérifie que le bateau est toujours horizontal
        for i in range(1, len(pos)):
            if (res and pos[0][0] != pos[i][0]) or (not res and pos[0][1] != pos[i][1]):
                raise ValueError("est_horizontal_bateau: Le bateau n'est ni horizontal, ni vertical ??")
    return res

def contientSegmentBateau(bateau:dict,case:tuple) -> bool :
    """
    Vérifie si un bateau contient une case dont les coordonnées sont données en paramètre
    :param bateau: Dictionnaire du bateau
    :param case: Tuple des coordonnées de la case
    :return: True si le bateau contient la case, False sinon
    """
    if not type_bateau(bateau) :
        raise ValueError(f"L'objet {bateau} n'est pas un bateau valide.")
    if not type_coordonnees(case) :
        raise ValueError(f"L'objet {case} ne correspond pas à des coordonnées.")
    lst_seg=getSegmentsBateau(bateau)
    estContenu=False
    for i in range(len(lst_seg)) :
        if lst_seg[i].get(const.SEGMENT_COORDONNEES) == case :
            estContenu = True
            break
    return estContenu

