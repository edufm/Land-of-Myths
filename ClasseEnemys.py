from numpy import random as ran

import ClasseImagens
from ClasseGun import Gun
import ClasseTrack

class Enemys():
    def __init__(self, ID, health, damage, pos):
        self.ID = ID
        self.health = health
        self.damage = damage
        self.pos = pos

    def cria_inimigos(waves, Map):
        Map.LEnemys = []
        if waves < 4:
            for i in range(waves*3):
                E = Enemys(0, 1, 1, [14, i])
                Map.matriz[14][i] = 2
                Map.b[14][i].config(image = ClasseImagens.enemy1[0])
                Map.b[14][i].image = ClasseImagens.enemy1[0]
                Map.LEnemys.append(E)
        if waves == 4:
            E = Enemys(1, 7, 5, [14, 13])
            Map.matriz[14][13] = 3
            Map.b[14][13].config(image = ClasseImagens.boss1[0])
            Map.b[14][13].image = ClasseImagens.boss1[0]
            Map.LEnemys.append(E)
        if waves > 4 and waves < 8:
            for i in range((waves-4)*3):
                E = Enemys(0, 2, 1, [14, i])
                Map.matriz[14][i] = 2
                Map.b[14][i].config(image = ClasseImagens.enemy1[0])
                Map.b[14][i].image = ClasseImagens.enemy1[0]
                Map.LEnemys.append(E)
        if waves == 8:
            E = Enemys(0, 14, 5, [14, 13])
            Map.matriz[14][13] = 3
            Map.b[14][13].config(image = ClasseImagens.boss1[0])
            Map.b[14][13].image = ClasseImagens.boss1[0]
            Map.LEnemys.append(E)
        if waves > 8:
            for i in range((waves-8)*3):
                E = Enemys(2, 3, 1, [14, i])
                Map.matriz[14][i] = 2
                Map.b[14][i].config(image = ClasseImagens.enemy1[0])
                Map.b[14][i].image = ClasseImagens.enemy1[0]
                Map.LEnemys.append(E)
                    
    def Take_Damage(loc, pl, Map):
        if pl.weapon.ID == 100:
            Gun.Take_Damage_P(loc,pl,Map)
        elif pl.weapon.ID == 101:
            Gun.Shotgun_Shot(pl, loc, Map)
        elif pl.weapon.ID == 102:
            Gun.Take_Damage_SN(loc,pl,Map)
    
    def left(self):
        self.pos[1] -= 1
    def right(self):
        self.pos[1] += 1
    def up(self):
        self.pos[0] -= 1
    def down(self):
        self.pos[0] += 1
        
    def jogada(self, pl, Map):
        distanciax = pl.pos[1] - self.pos[1]
        distanciay = pl.pos[0] - self.pos[0]
        if (distanciax == 0 and abs(distanciay) == 1) or (distanciax == 1 and abs(distanciay) == 0):
           self.atack(pl)
        
        elif distanciax > 0 and abs(distanciax) > abs(distanciay) and Map.matriz[self.pos[0]][self.pos[1]+1] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
            self.right()
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.enemy[self.ID][1])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][1]
            
        elif distanciax < 0 and abs(distanciax) > abs(distanciay) and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]            
            self.left()
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][2])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][2]
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
        elif distanciay > 0 and abs(distanciay) > abs(distanciax) and Map.matriz[self.pos[0]+1][self.pos[1]+1] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
            self.down()
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][3])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][3]
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
        elif distanciay < 0 and abs(distanciay) > abs(distanciax) and Map.matriz[self.pos[0]-1][self.pos[1]] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0            
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
            self.up()
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][0])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][0]
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
        elif abs(distanciay) == abs(distanciax):
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
            Op = ran.randint(1,3)
            a=0
            if distanciay < 0 and distanciax < 0 and Map.matriz[self.pos[0]-1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
                if Op == 1:
                    self.left()
                    a = 2
                if Op == 2:
                    self.up()
                    a = 0
            if distanciay > 0 and distanciax < 0 and Map.matriz[self.pos[0]+1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
                if Op == 1:
                    self.left()
                    a = 2
                if Op == 2:
                    self.down()
                    a = 3
            if distanciay < 0 and distanciax > 0 and Map.matriz[self.pos[0]-1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]+1] == 0:
                if Op == 1:
                    self.right()
                    a = 1
                if Op == 2:
                    self.up()
                    a = 0
            if distanciay > 0 and distanciax > 0 and Map.matriz[self.pos[0]+1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
                if Op == 1:
                    self.right()
                    a = 1
                if Op == 2:
                    self.down()
                    a = 3
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][a])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][a]
            Map.matriz[self.pos[0]][self.pos[1]] = 2
    
    def atack(self, pl):
        pl.health -= self.damage