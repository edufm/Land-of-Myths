
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
                img = PhotoImage(file="C:\\Users\\Hugo\\Desktop\\nova\\download.png")
                button.config(image=img)
                button.image = img
                self.b[i].append(button)
                
                
    def gui(window):
        
         vida = Label(window)
         vida.configure(text="VIDA:",bg = "orange")
         vida.configure(height = 2 , width = 4)
         vida.grid(row=16,column=0)
         botãodevida1 = Button(window)
         botãodevida1.configure(bg="light blue")
         botãodevida1.configure(height = 2 , width = 20)
         botãodevida1.grid(row= 16,columnspan = 6)