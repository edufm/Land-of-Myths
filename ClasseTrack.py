# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:48:42 2016

@author: Eduardo
"""

class Track():
    def __init__(self, Turn, Enemies, Boss, Weaponselected, Music,Aim):
        self.Turn = Turn 
        self.Enemies = Enemies
        self.Boss = Boss
        self.Weaponselected = Weaponselected
        self.Music = Music
        self.Aim = Aim #Aim mostra se o jogador tem  intenção e atirar nesse turno
        
Tracker = Track(0, 0, 0, 0, 0, 0)


