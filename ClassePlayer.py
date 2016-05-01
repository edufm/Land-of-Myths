        
class Player():
    def __init__(self, health, weapon, pos):  #pos é a posião do player dentro da matriz
        self.health = health
        self.weapon = weapon
        self.pos = pos
        
        #abaixo as defs para o player se movimentar
    def left():
        pl.pos[1] = pl.pos[1] - 1
    def right():
        pl.pos[1] = pl.pos[1] + 1
    def down():
        pl.pos[0] = pl.pos[0] + 1
    def up():
        pl.pos[0] = pl.pos[0] - 1
        
    def set_player(b):
        b[7][7].config(text = "X")

#----------------------------------------------- TESTE---------------------------------------
#while True:
#    print (pl.pos)
#    teste = input ("que direção - up , left , right , down")
#    if teste == "left":
#        Player.left()
#    elif teste == "down":
#        Player.down()
#    elif teste == "up":
#        Player.up()
#    elif teste == "right":
#        Player.right()
#    else:
#        print ("escreve certo")