# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:03:18 2016

@author: Eh Nòis
"""

from tkinter import *
import numpy as np

from ClassePlayer import Player
from ClasseMapa import Mapa
from ClasseGun import Gun

class Main:
    def __init__(self, name):
        self.name = name

    def Start_Game():
        window = Tk()
        window.title("Não sabemos ainda")
        window.configure(bg="orange")        
        
        img = PhotoImage(file=".\\download.png")
        imgPl = PhotoImage(file=".\\player.png")
        imgE = PhotoImage(file=".\\enemy.png")
        
        Map = Mapa(np.zeros([15, 15]), [], [window], 0, [])    

        Pistol = Gun(1, 100, 10, 1)        
        Lguns = [Pistol]        
        
        pl = Player(20, Lguns[0], [7,7])
        
        Map.matriz[7][7] = 1
        Mapa.load_map(Map, window, pl, img, imgPl, imgE)
        Player.set_player(pl)
        
        Mapa.gui(window, Map)
        
        window.mainloop()


Main.Start_Game()
