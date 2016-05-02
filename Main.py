# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:03:18 2016

@author: Eh Nòis
"""

from tkinter import *
import numpy as np


from ClassePlayer import Player
from ClasseEnemys import Enemys
from ClasseGun import Gun
from ClasseMapa import Mapa

class Main:
    def __init__(self, name):
        self.name = name

    def Start_Game():
        Map = Mapa(np.zeros([15, 15]))        
        Map.matriz[7][7] = 1
        b = Mapa.load_map(Map, window)
        pl = Player(20, "none", [7,7])
        Player.set_player(b)

window = Tk()
window.title("Não sabemos ainda")
window.geometry("1366x728")

Main.Start_Game()

window.mainloop()