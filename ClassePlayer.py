        
class Player():
    def __init__(self, health, weapon, pos):  #pos é a posião do player dentro da matriz
        self.health = health
        self.weapon = weapon
        self.pos = pos
        
    def set_player(self):
        self.pos = [7,7]