from numpy import random as ran

import ClasseImagens
from ClasseGun import Gun
import ClasseTrack
from ClassSound import *

class Enemys():
    def __init__(self, ID, health, damage, pos):
        self.ID = ID
        self.health = health
        self.damage = damage
        self.pos = pos

    def cria_inimigos(waves, Map):
        level = 0
        if waves > 12:
            level = 2
        Map.LEnemys = []
        if waves%4 != 0:
            N = ClasseTrack.Tracker.Boss
            for i in range((waves%4)*3):
                E = Enemys(0+level, 1+N, 1, [14, i])
                Map.matriz[14][i] = 2
                Map.b[14][i].config(image = ClasseImagens.enemy1[0])
                Map.b[14][i].image = ClasseImagens.enemy1[0]
                Map.LEnemys.append(E)
                
        if waves%4 == 0:
            N = ClasseTrack.Tracker.Boss
            E = Enemys(1+level, 7 + N-1*3, 5, [14, 13])
            Map.matriz[14][13] = 3
            Map.b[14][13].config(image = ClasseImagens.boss1[0])
            Map.b[14][13].image = ClasseImagens.boss1[0]
            Map.LEnemys.append(E)
                    
    def Take_Damage(loc, pl, Map):
        if pl.weapon.ID == 100:
            Gun.Take_Damage_P(loc,pl,Map)
            
        elif pl.weapon.ID == 101:
            Gun.Shotgun_Shot(pl, loc, Map)
            
        elif pl.weapon.ID == 102:
            if pl.inv[2] > 0: 
                pl.inv[2] -= 1
                Gun.Sniper_X(loc,Map,pl,7, 1, 0)
            
    
    def left(self, Map):
        Map.matriz[self.pos[0]][self.pos[1]] = 0
        Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]            
        self.pos[1] -= 1
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][2])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][2]
        Map.matriz[self.pos[0]][self.pos[1]] = 2
        
    def right(self, Map):
        Map.matriz[self.pos[0]][self.pos[1]] = 0
        Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
        self.pos[1] += 1
        Map.matriz[self.pos[0]][self.pos[1]] = 2
        Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.enemy[self.ID][1])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][1]
            
    def up(self, Map):
        Map.matriz[self.pos[0]][self.pos[1]] = 0            
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
        self.pos[0] -= 1
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][0])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][0]
        Map.matriz[self.pos[0]][self.pos[1]] = 2        
        
    def down(self, Map):
        Map.matriz[self.pos[0]][self.pos[1]] = 0
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
        self.pos[0] += 1
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][3])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][3]
        Map.matriz[self.pos[0]][self.pos[1]] = 2
        
        
    def jogada(self, pl, Map):
        distanciax = pl.pos[1] - self.pos[1]
        distanciay = pl.pos[0] - self.pos[0]
        if (distanciax == 0 and abs(distanciay) == 1) or (distanciax == 1 and abs(distanciay) == 0):
           self.atack(pl)
        
        elif distanciax > 0 and abs(distanciax) > abs(distanciay) and Map.matriz[self.pos[0]][self.pos[1]+1] == 0:
            
            self.right(Map)
            
        elif distanciax < 0 and abs(distanciax) > abs(distanciay) and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
            
            self.left(Map)
            
        elif distanciay > 0 and abs(distanciay) > abs(distanciax) and Map.matriz[self.pos[0]+1][self.pos[1]+1] == 0:
           
            self.down(Map)
            
        elif distanciay < 0 and abs(distanciay) > abs(distanciax) and Map.matriz[self.pos[0]-1][self.pos[1]] == 0:
            
            self.up(Map)
            
            
        elif abs(distanciay) == abs(distanciax):
            Op = ran.randint(1,3)
            if distanciay < 0 and distanciax < 0 and Map.matriz[self.pos[0]-1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
                if Op == 1:
                    self.left(Map)
                if Op == 2:
                    self.up(Map)
                    
            if distanciay > 0 and distanciax < 0 and Map.matriz[self.pos[0]+1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
                if Op == 1:
                    self.left(Map)
                if Op == 2:
                    self.down(Map)
                    
            if distanciay < 0 and distanciax > 0 and Map.matriz[self.pos[0]-1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]+1] == 0:
                if Op == 1:
                    self.right(Map)
                if Op == 2:
                    self.up(Map)

            if distanciay > 0 and distanciax > 0 and Map.matriz[self.pos[0]+1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]+1] == 0:
                if Op == 1:
                    self.right(Map)
                if Op == 2:
                    self.down(Map)
            
        else:
            if distanciay < 0 and Map.matriz[self.pos[0]-1][self.pos[1]] == 0:
                self.up(Map)
                
            elif distanciay > 0 and Map.matriz[self.pos[0]+1][self.pos[1]] == 0:
                self.down(Map)
                
            elif distanciax < 0 and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
                self.left(Map)
            
            elif distanciax > 0 and Map.matriz[self.pos[0]][self.pos[1]+1] == 0:
                self.right(Map)
    
    def atack(self, pl):
        pl.health -= self.damage