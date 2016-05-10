import numpy as np
import random

import ClasseEnemys
import ClasseImagens

class Gun():
    def __init__(self, ID, Ammo, Range, Damage,Type):
        self.ID = ID 
        self.Ammo = Ammo
        self.Range = Range
        self.Damage = Damage
    
    def Check_Range(self ,loc, pl):
        distanciax = pl.pos[1] - loc[1]
        if distanciax < 0:
            distanciax = loc[1] - pl.pos[1]
        distanciay = pl.pos[0] - loc[0]
        if distanciay < 0:
            distanciay = loc[0] - pl.pos[0]

        Distance = distanciax +  distanciay
        if Distance < self.Range:
            return 1
        else:
            return 0


    def Pick_Weapon(self, pl):        
        pl.inv[self.ID-100] = self.ammo
    
    def Weapon_Swap(ID):
        Weapon = ID - 100
        pl.Weapon = WeaponList[Weapon]
        
        
            
    def Shotgun_Shoot(self, pl, loc,Map):
        if loc[1] == (pl.pos[1] - 1) and loc[0] == pl.pos[0]:
            Gun.Shotgun_Left(pl.pos[1] - 1,Map,pl)
        if loc[1] == (pl.pos[1] + 1) and loc[0] == pl.pos[0]:
            Gun.Shotgun_Right(pl.pos[1] + 1,Map,pl)
        if loc[0] == (pl.pos[0] - 1) and loc[1] == pl.pos[1]:
            Gun.Shotgun_Up(pl.pos[0] - 1,Map,pl)
        if loc[0] == (pl.pos[0] + 1) and loc[1] == pl.pos[1]:
            Gun.Shotgun_Down(pl.pos[0] + 1,Map,pl)
        
#___________________________________________Shotgun____________________________
    
    def Shotgun_Left(loc,Map,pl):
        x = loc[0]
        y = loc[1]
        if Map.Matriz[x][y] < 100 and Map.Matriz[x][y] != 0:
            Enemys.Take_Damage_SG(Loc, pl, Map, 3)
        else:
            loc[1] -= 1
            loc[0] -= 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[0] += 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[0] += 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            
    def Shotgun_Right(loc,Map,pl):
        x = loc[0]
        y = loc[1]
        if Map.Matriz[x][y] < 100 and Map.Matriz[x][y] != 0:
            Enemys.Take_Damage_SG(Loc, pl, Map, 3)
        else:
            loc[1] += 1
            loc[0] -= 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[0] += 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[0] += 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            
    def Shotgun_Down(loc,Map,pl):
        x = loc[0]
        y = loc[1]
        if Map.Matriz[x][y] < 100 and Map.Matriz[x][y] != 0:
            Enemys.Take_Damage_SG(Loc, pl, Map, 3)
        else:
            loc[0] += 1
            loc[1] -= 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[1] += 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[1] += 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            
    def Shotgun_Up(loc,Map,pl):
        x = loc[0]
        y = loc[1]
        if Map.Matriz[x][y] < 100 and Map.Matriz[x][y] != 0:
            Enemys.Take_Damage_SG(Loc, pl, Map, 3)
        else:
            loc[0] -= 1
            loc[1] -= 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[1] += 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[1] += 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            
    
        
        #_______________________GErador armas_____________________
        

    def Gerar_Guns(Map):
        x = random.randint(1,101)
        if x <= 20:
            Gun.Gerar_Pistol(Map)
        x = random.randint(1,101)
        if x <= 10:
            Gun.Gerar_Shotgun(Map)
        x = random.randint(1,101)
        if x <= 5:
            Gun.Gerar_Sniper(Map)
        
    def Gerar_Pistol(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 100
        else:
            Gun.Gerar_Pistol(Map)
        
    def Gerar_Shotgun(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 101
        else:
            Gun.Gerar_Shotgun(Map)

    def Gerar_Sniper(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 102
        else:
            Gun.Gerar_Sniper(Map)
            
            #______________________Dano_______________________________________
        
    
    def Take_Damage_P(loc, pl, Map):
        
        RangeTest =Gun.Check_Range(Pistol, loc, pl)
        ammo = Gun.Ammo_Count(pl)
        
        if RangeTest == 1 and ammo == 1:
            for i in Map.LEnemys:
                if i.pos == loc:
                    i.health -= pl.weapon.Damage
                    if i.health <= 0:
                        Map.LEnemys.remove(i)    
                        Map.matriz[i.pos[0]][i.pos[1]] = 0
                        Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[Map.Waves])
                        Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[Map.Waves]
        Gun.Ammo_Count(pl)
                    
            
    def Take_Damage_SG(loc, pl, Map, Damage): #Função exclusiva do shotgun
        for i in Map.LEnemys:
            if i.pos == loc:
                i.health -= Damage
                if i.health <= 0:
                       Map.LEnemys.remove(i)    
                       Map.matriz[i.pos[0]][i.pos[1]] = 0
                       Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[Map.Waves])
                       Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[Map.Waves]
        Gun.Ammo_Count(pl)
                    
            #________________________________Ammo__________________________________________
                    
    def Ammo_Count(pl):
        Ammo = pl.weapon.ID - 100
        if pl.inv[Ammo] > 0:    
            pl.inv[Ammo] -= 1
            return 1
        else:
            print ("acabou a munição")
            return 0
        
Pistol = Gun(100,7,7,1,"Shoot")

Shotgun = Gun(101,6,3,3,"Burst")

Sniper = Gun(102,3,50,5,"LongWatch")

WeaponList = [Pistol,Shotgun,Sniper]