
from tkinter import *
import numpy as np

class Mapa():
    def __init__(self, matriz, b):
        self.matriz = matriz
        self.b = b

    def detect_click(self, m):
        X = m[0]
        Y = m[1]
        print(X)
        print(Y)
        print(self.matriz)
        b = self.b
        if X == 0 or Y == 0 or X == 14 or Y == 14:
            if X == 0 and Y == 0:
                if self.matriz[X][Y] == 0 and (self.matriz[X+1][Y] == 1 or self.matriz[X][Y+1] == 1):
                    self.matriz[X][Y] = 1
                    b[X][Y].config(text = "X")
                if self.matriz[X][Y] > 0:
                    ClasseEnemys.Take_Damage(pl.weapon)
                    
            if X == 14 and Y == 0:
                if self.matriz[X][Y] == 0 and (self.matriz[X][Y+1] == 1 or self.matriz[X-1][Y] == 1):
                    self.matriz[X][Y] = 1
                    b[X][Y].config(text = "X")
                if self.matriz[X][Y] > 0:
                    ClasseEnemys.Take_Damage(pl.weapon)
                    
            if X == 0 and Y == 14:
                if self.matriz[X][Y] == 0 and (self.matriz[X+1][Y] == 1 or self.matriz[X][Y-1] == 1):
                    self.matriz[X][Y] = 1
                    b[X][Y].config(text = "X")
                if self.matriz[X][Y] > 0:
                    ClasseEnemys.Take_Damage(pl.weapon)
            
            if X == 14 and Y == 14:
                if self.matriz[X][Y] == 0 and (self.matriz[X-1][Y] == 1 or self.matriz[X][Y-1] == 1):
                    self.matriz[X][Y] = 1
                    b[X][Y].config(text = "X")
                if self.matriz[X][Y] > 0:
                    ClasseEnemys.Take_Damage(pl.weapon)
            
            if X == 0 and Y != 0 and Y != 14:
                if self.matriz[X][Y] == 0 and (self.matriz[X+1][Y] == 1 or self.matriz[X][Y-1] == 1 or self.matriz[X][Y+1] == 1):
                    self.matriz[X][Y] = 1
                    b[X][Y].config(text = "X")
                if self.matriz[X][Y] > 0:
                    ClasseEnemys.Take_Damage(pl.weapon)
                
            if Y == 0 and X != 0 and X != 14:
                if self.matriz[X][Y] == 0 and (self.matriz[X+1][Y] == 1 or self.matriz[X-1][Y] == 1 or self.matriz[X][Y+1] == 1):
                    self.matriz[X][Y] = 1
                    b[X][Y].config(text = "X")
                if self.matriz[X][Y] > 0:
                    ClasseEnemys.Take_Damage(pl.weapon)
                    
            if X == 14 and Y != 0 and Y != 14:
                if self.matriz[X][Y] == 0 and (self.matriz[X-1][Y] == 1 or self.matriz[X][Y-1] == 1 or self.matriz[X][Y+1] == 1):
                    self.matriz[X][Y] = 1
                    b[X][Y].config(text = "X")
                if self.matriz[X][Y] > 0:
                    ClasseEnemys.Take_Damage(pl.weapon)
                
            if Y == 14 and X != 0 and X != 14:
                if self.matriz[X][Y] == 0 and (self.matriz[X+1][Y] == 1 or self.matriz[X][Y-1] == 1 or self.matriz[X-1][Y] == 1):
                    self.matriz[X][Y] = 1
                    b[X][Y].config(text = "X")
                if self.matriz[X][Y] > 0:
                    ClasseEnemys.Take_Damage(pl.weapon)

        if self.matriz[X][Y] == 1:
            ClasseGun.Puttrap(pl.weapon)
            
        else:
            if self.matriz[X][Y] == 0 and (self.matriz[X][Y+1] == 1 or self.matriz[X+1][Y] == 1 or self.matriz[X][Y-1] == 1 or self.matriz[X-1][Y] == 1):
                self.matriz[X][Y] = 1
                b[X][Y].config(text = "X")
            if self.matriz[X][Y] > 0:
                ClasseEnemys.Take_Damage(pl.weapon)

    def load_map(self, window):
        
        for i in range(15):
            self.b.append([])
            for j in range(15):
                button = Button(window, text=' ', width=4, height=2,command= lambda m=[i,j]: self.detect_click(m))
                button.grid(row=i, column=j, sticky=W+E+S+N)
                self.b[i].append(button)