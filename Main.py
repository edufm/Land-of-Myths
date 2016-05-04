# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:03:18 2016

@author: Eh Nòis
"""

from tkinter import *
import numpy as np

from ClassePlayer import Player
from ClasseGun import Gun
from ClasseMapa import Mapa

class Main:
    def __init__(self, name):
        self.name = name

    def Start_Game():
        img = PhotoImage(file=".\\download.png")
        imgPl = PhotoImage(file=".\\player.png")
        imgE = PhotoImage(file=".\\enemy.png")
        Map = Mapa(np.zeros([15, 15]), [], 0, [])     
        pl = Player(20, 0, [7,7])
        Map.matriz[7][7] = 1
        Mapa.load_map(Map, window, pl, img, imgPl, imgE)
        Player.set_player(pl, Map, img)
        Mapa.gui(window)
        
window = Tk()
window.title("Não sabemos ainda")
window.configure(bg="orange")

Main.Start_Game()

window.mainloop()