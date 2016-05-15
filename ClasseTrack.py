# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:48:42 2016

@author: Eduardo
"""

class Track():
    def __init__(self, Turn, Weaponselected, Enemies, Boss):
        self.Turn = Turn 
        self.Weaponselected = Weaponselected
        self.Enemies = Enemies
        self.Boss = Boss
        
Tracker = Track(0, 0, 0, 0)