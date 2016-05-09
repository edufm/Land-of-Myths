import numpy as np
import random


class Gun():
    def __init__(self, ID, Ammo, Range, Damage,Type):
        self.ID = ID 
        self.Ammo = Ammo
        self.Range = Range
        self.Damage = Damage
    
    def Check_Range(self ,loc, pl):
        distanciax = pl.pos[1] - loc[1]
        distanciay = pl.pos[0] - loc[0]
        Distance = distanciax +  distanciay
        if Distance < self.Range:
            return 1
        else:
            return 0


    def Pick_Weapon(self, pl):        
        pl.inv[self.ID-100] = self.ammo
        
            
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
        if Map.Matriz[x][y] < 100:
            Enemys.Take_Damage_SG(Loc, pl, Map, 3)
        else:
            loc[1] -= 1
            loc[0] -= 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[0] += 1
            Enemys.Take_Damage_SG(Loc, pl, Map, 1)
            loc[0] += 1
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
            
            #_____________________________________________________________
            
Pistol = Gun(100,7,7,1,"Shoot")

Shotgun = Gun(101,6,3,3,"Burst")

Sniper = Gun(102,3,50,5,"LongWatch")