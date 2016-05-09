from numpy import random as ran
import ClasseImagens

class Enemys():
    def __init__(self, ID, health, damage, pos):
        self.ID = ID        
        self.health = health
        self.damage = damage
        self.pos = pos
        
    def cria_inimigos(waves, Map):
        Map.LEnemys = []
        for i in range(waves*3):
            E = Enemys(1, 1, 1, [14,i])
            Map.matriz[14][i] = 2
            Map.b[14][i].config(image = ClasseImagens.enemy1[0])
            Map.b[14][i].image = ClasseImagens.enemy1[0]
            Map.LEnemys.append(E)
            
        if waves%5 == 0:
            E = Enemys(1, 10, 3, [14,27])
            Map.matriz[14][27] = 2
            Map.b[14][27].config(image = ClasseImagens.enemy1[0])
            Map.b[14][27].image = ClasseImagens.enemy1[0]
            Map.LEnemys.append(E)
                    
    def Take_Damage(loc, pl, Map):
        for i in Map.LEnemys:
            if i.pos == loc:
                i.health -= pl.weapon.Damage
                if i.health <= 0:
                    Map.LEnemys.remove(i)    
                    Map.matriz[i.pos[0]][i.pos[1]] = 0
                    Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[Map.Waves])
                    Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[Map.Waves]
    
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
            Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.Tiles[Map.Waves])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[Map.Waves]
            self.right()
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.enemy1[1])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy1[1]
            
        elif distanciax < 0 and abs(distanciax) > abs(distanciay) and Map.matriz[self.pos[0]][self.pos[1]-1] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.Tiles[Map.Waves])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[Map.Waves]            
            self.left()
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy1[2])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy1[2]
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
        elif distanciay > 0 and abs(distanciay) > abs(distanciax) and Map.matriz[self.pos[0]+1][self.pos[1]+1] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[Map.Waves])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[Map.Waves]
            self.down()
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy1[3])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy1[3]
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
        elif distanciay < 0 and abs(distanciay) > abs(distanciax) and Map.matriz[self.pos[0]-1][self.pos[1]] == 0:
            Map.matriz[self.pos[0]][self.pos[1]] = 0            
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[Map.Waves])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[Map.Waves]
            self.up()
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy1[0])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy1[0]
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
        elif abs(distanciay) == abs(distanciax):
            Map.matriz[self.pos[0]][self.pos[1]] = 0
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[Map.Waves])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[Map.Waves]
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
            Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy1[a])
            Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy1[a]
            Map.matriz[self.pos[0]][self.pos[1]] = 2
            
    def atack(self, pl):
        pl.health -= self.damage