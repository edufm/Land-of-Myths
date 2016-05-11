# -*- coding: utf-8 -*-
"""
Created on Fri May  6 07:34:13 2016

@author: Hugo
"""
from tkinter import *

class Imagem:
    def __init__(self,ImagemFront,ImagemRight,ImagemLeft,ImagemBack):
        self.Imagem = Imagem
        self.ImagemDir= ImagemDir
        self.ImagemEsq = ImagemEsq
        self.ImagemCost = ImagemCost
        


player_front = PhotoImage(file=".//Imagens//Sprites//player_front.png")
player_right = PhotoImage(file=".//Imagens//Sprites//player_right.png")
player_left =  PhotoImage(file=".//Imagens//Sprites//player_left.png")
player_back =  PhotoImage(file=".//Imagens//Sprites//player_back.png")

player = [player_front, player_right, player_left, player_back]
        
enemy1_front = PhotoImage(file=".//Imagens//Sprites//enemy1_front.png")
enemy1_right = PhotoImage(file=".//Imagens//Sprites//enemy1_right.png")
enemy1_left = PhotoImage(file=".//Imagens//Sprites//enemy1_left.png")
enemy1_back = PhotoImage(file=".//Imagens//Sprites//enemy1_back.png")

enemy1 = [enemy1_front, enemy1_right, enemy1_left, enemy1_back]  

boss1_front = PhotoImage(file=".//Imagens//Sprites//boss1_front.png")
boss1_right = PhotoImage(file=".//Imagens//Sprites//boss1_right.png")
boss1_left = PhotoImage(file=".//Imagens//Sprites//boss1_left.png")
boss1_back = PhotoImage(file=".//Imagens//Sprites//boss1_back.png")

boss1 = [boss1_front,boss1_right,boss1_left,boss1_back]

enemy2_front = PhotoImage(file=".//Imagens//Sprites//enemy2_front.png")
enemy2_right = PhotoImage(file=".//Imagens//Sprites//enemy2_right.png")
enemy2_left = PhotoImage(file=".//Imagens//Sprites//enemy2_left.png")
enemy2_back = PhotoImage(file=".//Imagens//Sprites//enemy2_back.png")

enemy2 = [enemy2_front, enemy2_right, enemy2_left, enemy2_back] 

enemy=[enemy1, boss1, enemy2]

grass = PhotoImage(file=".//Imagens//Tiles//grass.png")
dirt = PhotoImage(file=".//Imagens//Tiles//dirt.png")
stone = PhotoImage(file=".//Imagens//Tiles//stone.png")
snow = PhotoImage(file=".//Imagens//Tiles//snow.png")
wood = PhotoImage(file=".//Imagens//Tiles//wood.png")

Tiles = [grass, grass, dirt, stone, snow, wood, wood, wood, wood, wood]

Pistol = PhotoImage(file=".//Imagens//Sprites//revolver.png")
Shotgun = PhotoImage(file=".//Imagens//Sprites//shotgun.png")
Sniper = PhotoImage(file=".//Imagens//Sprites//sniper.png")

guns = [Pistol,Shotgun,Sniper]



