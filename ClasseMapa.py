
from tkinter import *
import numpy as np

class Mapa():
    def __init__(self, matriz, b):
        self.matriz = matriz
        self.b = b

    def detect_click(self, m, pl):
        X = m[0]
        Y = m[1]
        Xp = pl.pos[0]
        Yp = pl.pos[1]
        
        print(X)
        print(Y)
        
        b = self.b
        
        if self.matriz[X][Y] == 0 and X+1 == Xp:
            self.matriz[X][Y] = 1
            b[X][Y].config(text = "X")
            self.matriz[Xp][Y] = 0
            b[Xp][Yp].config(text = "")
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] == 0 and X-1 == Xp :
            self.matriz[X][Y] = 1
            b[X][Y].config(text = "X")
            self.matriz[Xp][Y] = 0
            b[Xp][Yp].config(text = "")
            pl.pos = [X,Y]            
            
        if self.matriz[X][Y] == 0 and Y+1 == Yp :
            self.matriz[X][Y] = 1
            b[X][Y].config(text = "X")
            self.matriz[X][Yp] = 0
            b[Xp][Yp].config(text = "")
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] == 0 and Y-1 == Yp:
            self.matriz[X][Y] = 1
            b[X][Y].config(text = "X") 
            self.matriz[X][Yp] = 0
            b[Xp][Yp].config(text = "")
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] > 1:
            ClasseEnemys.Take_Damage(pl.weapon)
               
        Mapa.Aiturn()
        
    def Aiturn():
        pass        

    def load_map(self, window, pl):
        
        for i in range(15):
            self.b.append([])
            for j in range(15):
                button = Button(window, text=' ',command= lambda m=[i,j]: self.detect_click(m, pl))
                button.grid(row=i, column=j, sticky=W+E+S+N)
                img = PhotoImage(file=".\\download.png")
                button.config(image=img)
                button.configure(height = 30, width = 30,bg = "black")
                button.image = img
                self.b[i].append(button)
                
    def vida_do_jogador(x,y):
            
            return x - y #ainda n está sendo usada
                
                  
    def gui(window):
        
         vida = Label(window)
         vida.configure(text="VIDA:",font=("castelar"),bg = "orange")
         vida.configure(height = 2 , width = 4)
         vida.grid(row=16,column=0)
         botãodevida1 = Button(window)
         botãodevida1.configure(bg="light blue")
         botãodevida1.configure(height = 2 , width = 20)
         botãodevida1.grid(row= 16,columnspan = 7)
         munição = Label(window)
         munição.configure(text="MUNIÇÃO :   x{0}".format(20),font=("castelar"),bg = "orange")
         munição.configure(height = 2, width = 15)
         munição.grid(row= 16, columnspan = 22)
         time = Label(window)
         time.configure(text="Time : {0}s".format(2.5),font=("castelar"),bg = "orange")
         time.configure(height = 2, width = 7)
         time.grid(row= 16, column = 11,columnspan= 2)
         wave = Label(window)
         wave.configure(text="WAVE : {0}".format(1),font=("castelar"),bg = "orange")
         wave.configure(height = 2, width = 7)
         wave.grid(row= 0, column = 7,columnspan= 2)
         
         
         
        