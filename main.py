# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

from view import window
from model.Constantes import *
from model.Joueur import construireJoueur, repondreTirJoueur
from model.Jeu import jouerJeu, getListeBateaux
from model.Manuel import *

#def main_test():
#
#    j = construireJoueur("Test", [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.TORPILLEUR])
    # j = construireJoueur("Test", [const.PORTE_AVION, const.CUIRASSE])

#    placerBateauManuel(j)

#    res=""
#    while res != const.COULE :
#        case=choisirCaseTirManuel(j)
#        res=repondreTirJoueur(j,case)
#        window.display_message(f"{res}")
#        traiterResultatTirManuel(j,case,res)
#        window.refresh()
#   window.set_action("Pour terminer, cliquez dans la grille de DROITE")
#   window.get_clicked_cell(2)




def main() :
    lst_bat = getListeBateaux()
    player1 = construireJoueur("Patrick Jopi",lst_bat)
    player2 = construireJoueur("MVL", lst_bat)
    jouerJeu(player1,player2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/