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


    def Pick_Weapon(ID, pl):        
        pl.inv[ID] = WeaponList[ID].Ammo
    
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
            Enemys.Take_Damage_SG(loc, pl, Map, 3)
        else:
            loc[1] -= 1
            loc[0] -= 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            loc[0] += 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            loc[0] += 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            
    def Shotgun_Right(loc,Map,pl):
        x = loc[0]
        y = loc[1]
        if Map.Matriz[x][y] < 100 and Map.Matriz[x][y] != 0:
            Enemys.Take_Damage_SG(loc, pl, Map, 3)
        else:
            loc[1] += 1
            loc[0] -= 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            loc[0] += 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            loc[0] += 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            
    def Shotgun_Down(loc,Map,pl):
        x = loc[0]
        y = loc[1]
        if Map.Matriz[x][y] < 100 and Map.Matriz[x][y] != 0:
            Enemys.Take_Damage_SG(loc, pl, Map, 3)
        else:
            loc[0] += 1
            loc[1] -= 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            loc[1] += 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            loc[1] += 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            
    def Shotgun_Up(loc,Map,pl):
        x = loc[0]
        y = loc[1]
        if Map.Matriz[x][y] < 100 and Map.Matriz[x][y] != 0:
            Enemys.Take_Damage_SG(loc, pl, Map, 3)
        else:
            loc[0] -= 1
            loc[1] -= 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            loc[1] += 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            loc[1] += 1
            Enemys.Take_Damage_SG(loc, pl, Map, 1)
            
    

    #_______________________________Sniper___________________________
    
    def Sniper_X(loc,Map,pl):
        x = loc[0]
        y = loc[1]
        Damage = 7
        if loc[0] == x and loc[1] > y:
            if Mapa.Matriz[0] == 0:
                loc[1] += 1
                Gun.Sniper_X(loc)
            else:
                Gun.Take_Damage_Sn(loc, pl, Map,Damage)
                Damage -= 1
            
        
            
            
        
        #_______________________GErador armas_____________________
        

    def Gerar_Guns(Map, imgguns):
        x = random.randint(1,101)
        if x <= 10:
            Gun.Gerar_Pistol(Map, imgguns)
        x = random.randint(1,101)
        if x <= 5:
            Gun.Gerar_Shotgun(Map, imgguns)
        x = random.randint(1,101)
        if x <= 2:
            Gun.Gerar_Sniper(Map, imgguns)
        
    def Gerar_Pistol(Map, imgguns):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 100
            Map.b[x][y].config(image = imgguns[0])
            Map.b[x][y].image = imgguns[0]
        else:
            Gun.Gerar_Pistol(Map, imgguns)
        
    def Gerar_Shotgun(Map, imgguns):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 101
            Map.b[x][y].config(image = imgguns[1])
            Map.b[x][y].image = imgguns[1]
        else:
            Gun.Gerar_Shotgun(Map, imgguns)

    def Gerar_Sniper(Map, imgguns):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 102
            Map.b[x][y].config(image = imgguns[2])
            Map.b[x][y].image = imgguns[2]
        else:
            Gun.Gerar_Sniper(Map, imgguns)
            
            #______________________Dano_______________________________________
        
    
    def Take_Damage_P(loc, pl, Map):
        print ("tomou")
        
        RangeTest =Gun.Check_Range(Pistol, loc, pl)
        
        if RangeTest == 1:
            Ammo = Gun.Ammo_Count(pl)
            for i in Map.LEnemys:     
                if Ammo == 1:
                    if i.pos == loc:
                        i.health -= pl.weapon.Damage
                        if i.health <= 0:
                            Map.LEnemys.remove(i)    
                            Map.matriz[i.pos[0]][i.pos[1]] = 0
                            Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[Map.Waves])
                            Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[Map.Waves]
            
                    
            
    def Take_Damage_SG(loc, pl, Map, Damage): #Função exclusiva do shotgun
        for i in Map.LEnemys:
            if i.pos == loc:
                i.health -= Damage
                if i.health <= 0:
                       Map.LEnemys.remove(i)    
                       Map.matriz[i.pos[0]][i.pos[1]] = 0
                       Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[Map.Waves])
                       Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[Map.Waves]
        
                    
            #________________________________Ammo__________________________________________
                    
    def Ammo_Count(pl):
        Ammo = pl.weapon.ID - 100
        if pl.inv[Ammo] > 0:    
            pl.inv[Ammo] -= 1
            print (pl.inv[Ammo])
            return 1
        else:
            print ("acabou a munição")

        
Pistol = Gun(100,7,7,1,"Shoot")

Shotgun = Gun(101,6,3,3,"Burst")

Sniper = Gun(102,3,50,5,"LongWatch")

WeaponList = [Pistol,Shotgun,Sniper]