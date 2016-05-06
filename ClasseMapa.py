
from tkinter import *
import numpy as np
from ClasseEnemys import Enemys

class Mapa():
    def __init__(self, matriz, b, gadjets, Waves, LEnemys):
        self.matriz = matriz
        self.b = b
        self.gadjets = gadjets
        self.Waves = Waves
        self.LEnemys = LEnemys
        

    def detect_click(self, m, pl, img, imgPl, imgE):
        
        X = m[0]
        Y = m[1]
        Xp = pl.pos[0]
        Yp = pl.pos[1]
        
        b = self.b
        
        if self.matriz[X][Y] == 0 and X+1 == Xp and Y == Yp:
            #Adiciona o player no novo lugar
            self.matriz[X][Y] = 1
            b[X][Y].config(image=imgPl)
            b[X][Y].image = imgPl
            #Remove o "Rastro" do player
            self.matriz[Xp][Y] = 0
            b[Xp][Yp].config(image=img)
            b[Xp][Yp].image = img
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] == 0 and X-1 == Xp and Y == Yp:
            self.matriz[X][Y] = 1
            b[X][Y].config(image=imgPl)
            b[X][Y].image = imgPl
            self.matriz[Xp][Y] = 0
            b[Xp][Yp].config(image=img)
            b[Xp][Yp].image = img
            pl.pos = [X,Y]

        if self.matriz[X][Y] == 0 and Y+1 == Yp and X == Xp:
            self.matriz[X][Y] = 1
            b[X][Y].config(image=imgPl)
            b[X][Y].image = imgPl
            self.matriz[X][Yp] = 0
            b[Xp][Yp].config(image=img)
            b[Xp][Yp].image = img
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] == 0 and Y-1 == Yp and X == Xp:
            self.matriz[X][Y] = 1
            b[X][Y].config(image=imgPl)
            b[X][Y].image = imgPl
            self.matriz[X][Yp] = 0
            b[Xp][Yp].config(image=img)
            b[Xp][Yp].image = img
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] == 2:
            Enemys.Take_Damage([X,Y], pl, self, img)
        
        if ((len(self.LEnemys)) == 0):
            self.Waves += 1
            Enemys.cria_inimigos(self.Waves, self, imgE)
        
        Mapa.Aiturn(self.LEnemys, pl ,self, img, imgE)
        
        Mapa.updategui(self.gadjets, pl.health, pl.weapon.Ammo, self.Waves)
        
    def Aiturn(enemys, pl, Map, img, imgE):
        for i in enemys:
            Enemys.jogada(i, pl, Map, img, imgE)

    def load_map(self, window, pl, img, imgPl, imgE):
        for i in range(15):
            self.b.append([])
            for j in range(15):
                button = Button(window, text=' ',command= lambda m=[i,j]: self.detect_click(m, pl, img, imgPl, imgE))
                button.grid(row=i+1, column=j, sticky=W+E+S+N)
                button.config(image=img)
                button.configure(height = 30, width = 30,bg = "black")
                button.image = img
                self.b[i].append(button)
                
        self.b[7][7].config(image=imgPl)
        self.b[7][7].image = imgPl
                
    def gui(window, Map):
        
         vida = Label(window)
         vida.configure(text="VIDA:",font=("castelar"),bg = "black",foreground = "white")
         vida.configure(height = 2 , width = 4)
         vida.grid(row=16,column=0)
         botãodevida1 = Button(window)
         botãodevida1.configure(bg="light blue")
         botãodevida1.configure(height = 2 , width = 20)
         botãodevida1.grid(row= 16,columnspan = 7)
         munição = Label(window)
         munição.configure(text="MUNIÇÃO :   x{0}".format(20),font=("castelar"),bg = "black",foreground = "white")
         munição.configure(height = 2, width = 15)
         munição.grid(row= 16, columnspan = 22)
         time = Label(window)
         time.configure(text="Time : {0}s".format(2.5),font=("castelar"),bg = "black",foreground="white")
         time.configure(height = 2, width = 8)
         time.grid(row= 16, column = 11,columnspan= 2)
         wave = Label(window)
         wave.configure(text="WAVE : {0}".format(1),font=("castelar"),bg = "black",foreground="white")
         wave.configure(height = 2, width = 7)
         wave.grid(row= 0, column = 7,columnspan= 2)
         
         Map.gadjets.append(vida)
         Map.gadjets.append(botãodevida1)
         Map.gadjets.append(munição)
         Map.gadjets.append(time)
         Map.gadjets.append(wave)
         
    def updategui(gadjets, vida, ammo, wave):
         
         gadjets[2].configure(height = 2 , width = vida)
         gadjets[3].configure(text="MUNIÇÃO :   x{0}".format(ammo),font=("castelar"),bg = "black",foreground = "white")         
         gadjets[4].configure(text="Time : {0}s".format(2.5),font=("castelar"),bg = "black",foreground="white")
         gadjets[5].configure(text="WAVE : {0}".format(wave),font=("castelar"),bg = "black",foreground="white")