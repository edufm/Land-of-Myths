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
    
Pistol = Gun(100,7,7,1,"Shoot")