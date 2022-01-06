# model/Jeu.py

#
#  Module mettant en place les joueurs
#
from model.Joueur import type_joueur, estPerdantJoueur, repondreTirJoueur
from model.Constantes import *
from model.Manuel import *
from random import randint

# Pour jouer, un joueur doit être capable de :
# - placer ses bateaux
# - choisir une case pour tirer
# - traiter le résultat d'un tir
# Pour cela, on crée un acteur : dictionnaire
#       const.ACTEUR : Joueur (voir construireJoueur)
#       const.ACTEUR_PLACER_BATEAUX : fonction permettant de placer les bateaux
#       const.ACTEUR_CHOISIR_CASE : fonction permettant de choisir la case où le tir aura lieu
#       const.ACTEUR_TRAITER_RESULTAT : fonction permettant de traiter le résultat d'un précédent tir

def type_acteur(agent: dict) -> bool:
    """
    Détermine si le tuple passé en paramètre peut être un agent ou non
    :param agent: Agent à tester
    :return: True si c'est un agent, False sinon
    """
    return type(agent) == dict and \
        all(k in agent for k in [const.ACTEUR,
                                 const.ACTEUR_PLACER_BATEAUX,
                                 const.ACTEUR_CHOISIR_CASE,
                                 const.ACTEUR_TRAITER_RESULTAT]) and \
        type_joueur(agent[const.ACTEUR]) and \
        callable(agent[const.ACTEUR_PLACER_BATEAUX]) and callable(agent[const.ACTEUR_CHOISIR_CASE]) and \
        callable(agent[const.ACTEUR_TRAITER_RESULTAT])

def jouerJeu(player1:dict,player2:dict) -> None :
    """
    A partir de deux joueurs, lance le jeu
    :param player1: Dictionnaire du premier joueur
    :param player2: Dictionnaire du deuxième joueur
    :return: None
    """
    if not type_joueur(player1) or not type_joueur(player2) :
        raise ValueError("Au moins un des deux paramètres ne correspond pas à un joueur")

    #Placement des bateaux#
    placerBateauManuel(player1)
    placerBateauManuel(player2)
    #Choix du premier joueur#

    deb=randint(0,1)
    if deb == 0 :
        play = player1
        play2 = player2
    else :
        play = player2
        play2 = player1

    #Début du jeu#
    while not estPerdantJoueur(play) and not estPerdantJoueur(play2) :
        window.afficher(play)
        window.display_message(f"C'est au tour de {getNomJoueur(play)}.")
        case=choisirCaseTirManuel(play)
        res=repondreTirJoueur(play2,case)
        traiterResultatTirManuel(play,case,res)
        window.refresh()
        window.display_message(f"Tir en {case} : {res}")
        #Échange des joueurs#
        tmp = play
        play = play2
        play2 = tmp
    if estPerdantJoueur(play) :
        winner=play2
    else :
        winner=play
    win_name=winner.get(const.JOUEUR_NOM)
    window.display_message(f"Le gagnant est {win_name}")

def getListeBateaux() -> list :
    """
    Renvoie la liste des bateaux
    :return:
    """
    lst_bat= [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.CROISEUR, const.TORPILLEUR]
    return lst_bat



