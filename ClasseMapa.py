
from tkinter import *
import numpy as np

window = Tk()
window.title("Magic Trap")
window.configure(bg="black")

from ClasseEnemys import Enemys
from ClasseGun import Gun
from ClassePlayer import Player
import ClasseImagens

class Mapa():
    def __init__(self, matriz, b, gadjets, Waves, LEnemys):
        self.matriz = matriz
        self.b = b
        self.gadjets = gadjets
        self.Waves = Waves
        self.LEnemys = LEnemys
    
    def Start_Game():
        
        Map = Mapa(np.zeros([15, 27]), [], [window], 0, [])    

        Pistol = Gun(1, 100, 10, 1)        
        Lguns = [Pistol]
        
        pl = Player(20, Lguns[0], [7,13])
        
        Map.matriz[7][13] = 1
        Mapa.load_map(Map, window, pl)
        Player.set_player(pl)
        
        Mapa.gui(window, Map)
        
        window.mainloop()

    def detect_click(self, m, pl):
        
        if ((len(self.LEnemys)) == 0):
            self.Waves += 1
            Enemys.cria_inimigos(self.Waves, self)
            Mapa.update_map(self, pl)
        
        X = m[0]
        Y = m[1]
        Xp = pl.pos[0]
        Yp = pl.pos[1]
        
        b = self.b
        
        if self.matriz[X][Y] == 0 and X+1 == Xp and Y == Yp:
            #Adiciona o player no novo lugar
            self.matriz[X][Y] = 1
            b[X][Y].config(image=ClasseImagens.player[1])
            b[X][Y].image = ClasseImagens.player[1]
            #Remove o "Rastro" do player
            self.matriz[Xp][Y] = 0
            b[Xp][Yp].config(image=ClasseImagens.Tiles[self.Waves])
            b[Xp][Yp].image = ClasseImagens.Tiles[self.Waves]
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] == 0 and X-1 == Xp and Y == Yp:
            self.matriz[X][Y] = 1
            b[X][Y].config(image=ClasseImagens.player[2])
            b[X][Y].image = ClasseImagens.player[2]
            self.matriz[Xp][Y] = 0
            b[Xp][Yp].config(image=ClasseImagens.Tiles[self.Waves])
            b[Xp][Yp].image = ClasseImagens.Tiles[self.Waves]
            pl.pos = [X,Y]

        if self.matriz[X][Y] == 0 and Y+1 == Yp and X == Xp:
            self.matriz[X][Y] = 1
            b[X][Y].config(image=ClasseImagens.player[3])
            b[X][Y].image = ClasseImagens.player[3]
            self.matriz[X][Yp] = 0
            b[Xp][Yp].config(image= ClasseImagens.Tiles[self.Waves])
            b[Xp][Yp].image = ClasseImagens.Tiles[self.Waves]
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] == 0 and Y-1 == Yp and X == Xp:
            self.matriz[X][Y] = 1
            b[X][Y].config(image= ClasseImagens.player[0])
            b[X][Y].image = ClasseImagens.player[0]
            self.matriz[X][Yp] = 0
            b[Xp][Yp].config(image= ClasseImagens.Tiles[self.Waves])
            b[Xp][Yp].image = ClasseImagens.Tiles[self.Waves]
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] == 2:
            Enemys.Take_Damage([X,Y], pl, self)
        
        Mapa.Aiturn(self.LEnemys, pl ,self)
        
        Mapa.updategui(self.gadjets, pl.health, pl.weapon.Ammo, self.Waves)
        

    def Aiturn(enemys, pl, Map):
        for i in enemys:
            Enemys.jogada(i, pl, Map)

    def update_map(Map, pl):
        for i in range (15):
            for j in range(27):
                Map.b[i][j].config(image=ClasseImagens.Tiles[Map.Waves])
                Map.b[i][j].image = ClasseImagens.Tiles[Map.Waves]
                
        Map.b[pl.pos[0]][pl.pos[1]].config(image = ClasseImagens.player[1])
        Map.b[pl.pos[0]][pl.pos[1]].image = ClasseImagens.player[1]

    def load_map(self, window, pl):
        
        for i in range(15):
            self.b.append([])
            for j in range(27):
                button = Button(window, text=' ',command= lambda m=[i,j]: self.detect_click(m, pl))
                button.grid(row=i+1, column=j, sticky=W+E+S+N)
                button.config(image=ClasseImagens.Tiles[0])
                button.configure(height = 36, width = 36,bg = "black")
                button.image = ClasseImagens.Tiles[0]
                self.b[i].append(button)
                        
        self.b[7][13].config(image = ClasseImagens.player[0])
        self.b[7][13].image = ClasseImagens.player[0]
                
    def gui(window, Map):
        
         vida = Label(window)
         vida.configure(text="Life:",font=("castelar"),bg = "black",foreground = "white")
         vida.configure(height = 2 , width = 4)
         vida.grid(row=16,column=0)
         botãodevida1 = Button(window)
         botãodevida1.configure(bg="light blue")
         botãodevida1.configure(height = 2 , width = 20)
         botãodevida1.grid(row= 16,columnspan = 7)
         munição = Label(window)
         munição.configure(text="Ammo :   x{0}".format(20),font=("castelar"),bg = "black",foreground = "white")
         munição.configure(height = 2, width = 15)
         munição.grid(row= 16, columnspan = 22)
         time = Label(window)
         time.configure(text="Time : {0}s".format(2.5),font=("castelar"),bg = "black",foreground="white")
         time.configure(height = 2, width = 8)
         time.grid(row= 16, column = 11,columnspan= 2)
         wave = Label(window)
         wave.configure(text="Wave : {0}".format(1),font=("castelar"),bg = "black",foreground="white")
         wave.configure(height = 2, width = 7)
         wave.grid(row= 1, column = 28, columnspan= 2)
         
         Map.gadjets.append(vida)
         Map.gadjets.append(botãodevida1)
         Map.gadjets.append(munição)
         Map.gadjets.append(time)
         Map.gadjets.append(wave)
         
    def updategui(gadjets, vida, ammo, wave):
         
         gadjets[2].configure(height = 2 , width = vida)
         gadjets[3].configure(text="Ammo :   x{0}".format(ammo),font=("castelar"),bg = "black",foreground = "white")         
         gadjets[4].configure(text="Time : {0}s".format(2.5),font=("castelar"),bg = "black",foreground="white")
         gadjets[5].configure(text="Wave : {0}".format(wave),font=("castelar"),bg = "black",foreground="white")