# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:48:42 2016

@author: Eduardo
"""

class Track():
    def __init__(self, Turn, Enemies, Boss, Weaponselected, Music):
        self.Turn = Turn 
        self.Enemies = Enemies
        self.Boss = Boss
        self.Weaponselected = Weaponselected
        self.Music = Music
        
Tracker = Track(0, 0, 0, 0, 0)