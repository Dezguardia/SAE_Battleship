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

def choisirCaseTirManuel(player:dict) -> tuple :
    if not type_joueur(player) :
        raise ValueError(f"Le joueur {player} n'est pas valide.")
    player_name = getNomJoueur(player)
    window.afficher(player)
    window.display_message(f"{player_name}: Choisissez la case où vous voulez tirer.")
    window.set_action("Choisissez la case de tir (clic gauche")
    cell = window.get_clicked_cell(2)
    cell_test=list(cell)
    del cell_test[1]
    cell=tuple(cell_test[0])
    return cell

