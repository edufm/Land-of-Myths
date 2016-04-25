# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:03:18 2016

@author: Eh Nòis
"""
import numpy as np

class Mapa():
    def __init__(self, matriz):
        self.matriz = np.zeros([15,15])
        
class Player():
    def __init__(self, health, weapon):
        self.health = 20
        self.weapon = None

class Gun():
    def __init__(self, ID, Ammo, Range, Damage):
        self.ID = ID 
        self.Ammo = Ammo
        self.Range = Range
        self.Damage = Damage

class Enemys():
    def __init__(self, ID, health, damage):
        self.ID = ID        
        self.health = health
        self.damage = damage