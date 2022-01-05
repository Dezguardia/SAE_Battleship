# model/Manuel.py
#
from model.Joueur import getNomJoueur, type_joueur

from view import window

def placerBateauManuel(player:dict) -> None :
    if not type_joueur(player) :
        raise ValueError(f"Le joueur {player} n'est pas valide.")
    player_name=getNomJoueur(player)
    window.afficher(player)
    window.display_message(f"{player_name} : Placez vos bateaux.")
    window.placer_bateaux()
