
from numpy import random as ran

class Enemys():
    def __init__(self, ID, health, damage, pos):
        self.ID = ID        
        self.health = health
        self.damage = damage
        self.pos = pos
        
    def cria_inimigos(waves, Map, imgE):
        Map.LEnemys = []
        if waves == 1:
            for i in range(5):
                E = Enemys(1, 1, 1, [14,i])
                Map.matriz[14][i] = 2
                Map.b[14][i].config(image = imgE)
                Map.b[14][i].image = imgE
                Map.LEnemys.append(E)
                
        if waves == 2:
            for i in range(10):
                E = Enemys(1, 1, 1, [14,i])
                Map.LEnemys.append(E)

        if waves == 3:
            for i in range(0, 14):
                E = Enemys(1, 1, 1, [14,i])
                Map.LEnemys.append(E)
    
    def take_damage(self, loc):
        pass
    
    def left(self):
        self.pos[1] -= 1
    def right(self):
        self.pos[1] += 1
    def up(self):
        self.pos[0] -= 1
    def down(self):
        self.pos[0] += 1
        
    def jogada(self, pl, Map, img, imgE):
        distanciax = pl.pos[1] - self.pos[1]
        distanciay = pl.pos[0] - self.pos[0]
        if (distanciax == 0 and distanciay == 1) or (distanciax == 1 and distanciay == 0):
           self.atack(pl)
        
        elif distanciax > 0 and abs(distanciax) > abs(distanciay) and Map.matriz[self.pos[0]][self.pos[1]+1] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image=img)
            Map.b[self.pos[0]][self.pos[1]].image = img
            self.right()
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            Map.b[self.pos[0]][self.pos[1]].config(image=imgE)
            Map.b[self.pos[0]][self.pos[1]].image = imgE
            
        elif distanciax < 0 and abs(distanciax) > abs(distanciay) and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image=img)
            Map.b[self.pos[0]][self.pos[1]].image = img            
            self.left()
            Map.b[self.pos[0]][self.pos[1]].config(image=imgE)
            Map.b[self.pos[0]][self.pos[1]].image = imgE
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
        elif distanciay > 0 and abs(distanciay) > abs(distanciax) and Map.matriz[self.pos[0]]+1[self.pos[1]+1] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image=img)
            Map.b[self.pos[0]][self.pos[1]].image = img
            self.down()
            Map.b[self.pos[0]][self.pos[1]].config(image=imgE)
            Map.b[self.pos[0]][self.pos[1]].image = imgE
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
        elif distanciay < 0 and abs(distanciay) > abs(distanciax) and Map.matriz[self.pos[0]-1][self.pos[1]] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0            
            Map.b[self.pos[0]][self.pos[1]].config(image=img)
            Map.b[self.pos[0]][self.pos[1]].image = img
            self.up()
            Map.b[self.pos[0]][self.pos[1]].config(image=imgE)
            Map.b[self.pos[0]][self.pos[1]].image = imgE
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
        elif abs(distanciay) == abs(distanciax):
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image=img)
            Map.b[self.pos[0]][self.pos[1]].image = img
            Op = ran.randint(1,3)      
            if distanciay < 0 and distanciax < 0 and Map.matriz[self.pos[0]-1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
                if Op == 1:
                    self.left()
                if Op == 2:
                    self.up()
            if distanciay > 0 and distanciax < 0 and Map.matriz[self.pos[0]+1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
                if Op == 1:
                    self.left()
                if Op == 2:
                    self.down()
            if distanciay < 0 and distanciax > 0 and Map.matriz[self.pos[0]-1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]+1] == 0:
                if Op == 1:
                    self.right()
                if Op == 2:
                    self.up()
            if distanciay > 0 and distanciax > 0 and Map.matriz[self.pos[0]+1][self.pos[1]] == 0 and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
                if Op == 1:
                    self.right()
                if Op == 2:
                    self.down()
            Map.b[self.pos[0]][self.pos[1]].config(image=imgE)
            Map.b[self.pos[0]][self.pos[1]].image = imgE
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
    def atack(self, pl):
        pl.health -= self.damage
            
#if pl.pos[1] == self.pos[1]:
#    if distanciax < 0:
#        self.left()
#    if distanciax > 0:
#        self.right()
#elif pl.pos[0] == self.pos[0]:
#    if distanciay < 0:
#        self.up()
#    if distanciay > 0:
#        self.down()
