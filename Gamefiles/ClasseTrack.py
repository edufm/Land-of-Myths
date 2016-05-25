class Track():
    def __init__(self, Turn, Enemies, Boss, Weaponselected, Music, Musicenabled, Map, pl, Timername):
        self.Turn = Turn 
        self.Enemies = Enemies
        self.Boss = Boss
        self.Weaponselected = Weaponselected
        self.Music = Music
        self.Musicenabled = Musicenabled
        self.Map = Map
        self.pl = pl
        self.Timername = Timername
        
Tracker = Track(0, 0, 0, 0, 0, True, 0, 0, 0)
