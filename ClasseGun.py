import numpy as np
import random
from ClasseMapa import Mapa   #REmover Dps

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
            
    def Shotgun_Shoot(self, pl):
        pl.pos

    def Gerar_Pistol(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 100
        else:
            Gun.Gerar_Pistol(Map)
            
            
Pistol = Gun(100,7,7,1,"Shoot")

Mapa.Start_Game()

x = 0
while x <= 12:
    x +=1
    Gun.Gerar_Pistol(Map)
    Print(Map.matriz)