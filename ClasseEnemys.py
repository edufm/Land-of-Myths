
class Enemys():
    def __init__(self, ID, health, damage, pos):
        self.ID = ID        
        self.health = health
        self.damage = damage
        self.pos = pos
        
    def left():
        self.pos[0] -= 1
    def right():
        self.pos[0] += 1
    def up():
        self.pos[1] -= 1
    def down():
        self.pos[1] += 1
        
    def jogada():
        distanciax = pl.pos[1] - self.pos[1]
        distanciay = pl.pos[0] - self.pos[0]
        if pl.pos[1] == self.pos[1]:
            if distanciax < 0:
                self.left()
            if distanciax > 0:
                self.right()
        elif pl.pos[0] == self.pos[0]:
            if distanciay < 0:
                self.up()
            if distanciay > 0:
                self.down()
        