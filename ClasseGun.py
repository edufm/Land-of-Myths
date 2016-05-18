import random

import ClasseImagens
import ClasseTrack

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

        print (distanciax, distanciay)
        Distance = distanciax +  distanciay
        print (Distance, self.Range)
        if Distance < self.Range:
            return 1
        else:
            return 0

    def Pick_Weapon(ID, pl):
        Ammo = pl.inv[ID]
        Ammo += WeaponList[ID].Ammo
        if Ammo >= WeaponList[ID].Ammo * 3:
            pl.inv[ID] = WeaponList[ID].Ammo * 3
        else:
            pl.inv[ID] += WeaponList[ID].Ammo
    
    def Weapon_Swap(ID,pl):
        Weapon = ID - 100
        pl.Weapon = WeaponList[Weapon]        
            
    def Shotgun_Shot(pl, loc, Map):
    
        if loc[1] == (pl.pos[1] - 1) and loc[0] == pl.pos[0]:
            Gun.Shotgun_Left([loc[0], pl.pos[1] - 1], Map, pl)
        if loc[1] == (pl.pos[1] + 1) and loc[0] == pl.pos[0]:
            Gun.Shotgun_Right([loc[0], pl.pos[1] + 1], Map, pl)
        if loc[0] == (pl.pos[0] - 1) and loc[1] == pl.pos[1]:
            Gun.Shotgun_Up([pl.pos[0] - 1, loc[1]], Map, pl)
        if loc[0] == (pl.pos[0] + 1) and loc[1] == pl.pos[1]:
            Gun.Shotgun_Down([pl.pos[0] + 1, loc[1]], Map, pl)
        
#___________________________________________Shotgun____________________________
    
    def Shotgun_Left(loc,Map,pl):
        Ammo = Gun.Ammo_Count(pl)
        if Ammo == 1:  
            x = loc[0]
            y = loc[1]
            if Map.matriz[x][y] < 100 and Map.matriz[x][y] != 0:
                Gun.Take_Damage_SG(loc, pl, Map, 3)
            else:
                loc[1] -= 1
                loc[0] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
                
            
    def Shotgun_Right(loc,Map,pl):
        Ammo = Gun.Ammo_Count(pl)
        if Ammo == 1:  
            x = loc[0]
            y = loc[1]
            if Map.matriz[x][y] < 100 and Map.matriz[x][y] != 0:
                Gun.Take_Damage_SG(loc, pl, Map, 3)
            else:
                loc[1] += 1
                loc[0] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
            
    def Shotgun_Down(loc,Map,pl):
        Ammo = Gun.Ammo_Count(pl)
        if Ammo == 1:          
            x = loc[0]
            y = loc[1]
            if Map.matriz[x][y] < 100 and Map.matriz[x][y] != 0:
                Gun.Take_Damage_SG(loc, pl, Map, 3)
            else:
                loc[0] += 1
                loc[1] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
            
    def Shotgun_Up(loc, Map, pl):
        Ammo = Gun.Ammo_Count(pl)
        if Ammo == 1:        
            x = loc[0]
            y = loc[1]
            if Map.matriz[x][y] < 100 and Map.matriz[x][y] != 0:
                Gun.Take_Damage_SG(loc, pl, Map, 3)
            else:
                loc[0] -= 1
                loc[1] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1)
            
    

    #_______________________________Sniper___________________________
    
    def Sniper_X(loc,Map,pl,Damage,First,count):
        
        print ("count =",count)
        ammo = pl.weapon.ID - 100
        count += 1
        if pl.inv[ammo] == 0 and count == 1:
            pl.inv[ammo] = 1

        if count == 1:  
            Ammo = pl.inv[ammo]
            if pl.inv[ammo] > 0: 
                pl.inv[ammo] -= 1
            RangeTest =Gun.Check_Range(Sniper, loc, pl) 
        else: 
            RangeTest = 1
            ammo = pl.weapon.ID - 100
            Ammo = pl.inv[ammo]
            
        if RangeTest == 1:
            x = pl.pos[0]
            y = pl.pos[1]
            if loc[0] == x and loc[1] > y: # right
                if loc[1] < 27:
                    if Map.matriz[loc[0]][loc[1]] == 0 or Map.matriz[loc[0]][loc[1]] > 100:
                        loc[1] += 1
                        print (loc)
                        Gun.Sniper_X(loc,Map,pl,Damage,0,count)
                    else:
                        Gun.Take_Damage_SN(loc, pl, Map,Damage,count,Ammo)
                        Damage -= 1
                        print (Damage)
                        loc[1] += 1
                        print ("pierce",loc)
                        Gun.Take_Damage_SN(loc, pl, Map,Damage,count,Ammo)
            if loc[0] == x and loc[1] < y: # left
                if loc[1] >= 0:
                    if Map.matriz[loc[0]][loc[1]] == 0 or Map.matriz[loc[0]][loc[1]] > 100:
                        loc[1] -= 1
                        print (loc)
                        Gun.Sniper_X(loc,Map,pl,Damage,0,count)
                    else:
                        Gun.Take_Damage_SN(loc, pl, Map,Damage,count,Ammo)
                        Damage -= 1
                        print("DAma",Damage)
                        loc[1] -= 1
                        print ("pierce",loc)
                        Gun.Sniper_X(loc,Map,pl,Damage, 0, count)
            if loc[0] < x and loc[1] == y: # up
                if loc[0] >= 0:
                    if Map.matriz[loc[0]][loc[1]] == 0 or Map.matriz[loc[0]][loc[1]] > 100:
                        loc[0] -= 1
                        print (loc)
                        Gun.Sniper_X(loc,Map,pl,Damage,0,count)
                    else:
                        Gun.Take_Damage_SN(loc, pl, Map,Damage,count,Ammo)
                        Damage -= 1
                        print("DAma",Damage)
                        loc[0] -= 1
                        print ("pierce",loc)
                        Gun.Sniper_X(loc,Map,pl,Damage, 0, count)
            if loc[0] > x and loc[1] == y: # down
                if loc[0] >= 0:
                    if Map.matriz[loc[0]][loc[1]] == 0 or Map.matriz[loc[0]][loc[1]] > 100:
                        loc[0] += 1
                        print (loc)
                        Gun.Sniper_X(loc,Map,pl,Damage,0,count)
                    else:
                        Gun.Take_Damage_SN(loc, pl, Map,Damage,count,Ammo)
                        Damage -= 1
                        print("DAma",Damage)
                        loc[0] += 1
                        print ("pierce",loc)
                        Gun.Sniper_X(loc,Map,pl,Damage, 0, count)
                        
        #_______________________GErador armas_____________________
        

    def Gerar_Guns(Map):
        a = 0
        b = 0
        c = 0
        for i in range(15):
            for j in range(27):
                if Map.matriz[i][j] == 100:           
                    a += 1
                if Map.matriz[i][j] == 101:
                    b += 1
                if Map.matriz[i][j] == 101:
                    c += 1
                
        x = random.randint(1,101)
        
        if a < 3:
            if x <= 10:
                Gun.Gerar_Pistol(Map)
        x = random.randint(1,101)
        if b <= 2:
            if x <= 4:
                Gun.Gerar_Shotgun(Map)
        x = random.randint(1,101)
        if c < 2:
            if x <= 1:
                Gun.Gerar_Sniper(Map)
        
    def Gerar_Pistol(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 100
            Map.b[x][y].config(image = ClasseImagens.guns[0])
            Map.b[x][y].image = ClasseImagens.guns[0]
        else:
            Gun.Gerar_Pistol(Map)
        
    def Gerar_Shotgun(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 101
            Map.b[x][y].config(image = ClasseImagens.guns[1])
            Map.b[x][y].image = ClasseImagens.guns[1]
        else:
            Gun.Gerar_Shotgun(Map)

    def Gerar_Sniper(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 102
            Map.b[x][y].config(image = ClasseImagens.guns[2])
            Map.b[x][y].image = ClasseImagens.guns[2]
        else:
            Gun.Gerar_Sniper(Map)
            
            #______________________Dano_______________________________________
        
    
    def Take_Damage_P(loc, pl, Map):
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
                            Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                            Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]

    def Take_Damage_SG(loc, pl, Map, Damage): #Função exclusiva do shotgun       
            for i in Map.LEnemys:
                if i.pos == loc:
                    i.health -= Damage
                    if i.health <= 0:
                        Map.LEnemys.remove(i)    
                        Map.matriz[i.pos[0]][i.pos[1]] = 0
                        Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                        Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
    
    def Take_Damage_SN(loc, pl, Map, Damage,count,Ammo):
        if Ammo > 0:
            for i in Map.LEnemys:
                if i.pos == loc:
                    i.health -= Damage
                    if i.health <= 0:
                        print ("dano =", Damage)
                        Damage -= i.health
                        Map.LEnemys.remove(i)    
                        Map.matriz[i.pos[0]][i.pos[1]] = 0
                        Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                        Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
  
                    
            #________________________________Ammo__________________________________________
                    
    def Ammo_Count(pl):
        Ammo = pl.weapon.ID - 100
        if pl.inv[Ammo] > 0:    
            pl.inv[Ammo] -= 1
            return 1

        
Pistol = Gun(100,7,7,1,"Shoot")

Shotgun = Gun(101,6,3,3,"Burst")

Sniper = Gun(102,3,2,5,"LongWatch")

WeaponList = [Pistol,Shotgun,Sniper]