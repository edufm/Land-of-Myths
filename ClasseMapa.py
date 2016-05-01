
from tkinter import *
import numpy as np

class Mapa():
    def __init__(self, matriz):
        self.matriz = matriz
        
    def detect_click(X, Y, matriz, b):
        print(matriz)
        if X == 0 or Y == 0 or X == 14 or Y == 14 and X == 1000:
            if X == 0 and Y == 0:
                if matriz[X][Y] == 0 and (matriz[X+1][Y] == 1 or matriz[X][Y+1] == 1):
                    matriz[X][Y] == 1
                    b[X+1][Y+1].config(text = "X")
                if matriz[X][Y] > 0:
                    Enemys.Take_Damage(pl.weapon)
                    
            if X == 14 and Y == 0:
                if matriz[X][Y] == 0 and (matriz[X][Y+1] == 1 or matriz[X-1][Y] == 1):
                    matriz[X][Y] == 1
                    b[X+1][Y+1].config(text = "X")
                if matriz[X][Y] > 0:
                    Enemys.Take_Damage(pl.weapon)
                    
            if X == 0 and Y == 14:
                if matriz[X][Y] == 0 and (matriz[X+1][Y] == 1 or matriz[X][Y-1] == 1):
                    matriz[X][Y] == 1
                    b[X+1][Y+1].config(text = "X")
                if matriz[X][Y] > 0:
                    Enemys.Take_Damage(pl.weapon)
            
            if X == 14 and Y == 14:
                if matriz[X][Y] == 0 and (matriz[X-1][Y] == 1 or matriz[X][Y-1] == 1):
                    matriz[X][Y] == 1
                    b[X+1][Y+1].config(text = "X")
                if matriz[X][Y] > 0:
                    Enemys.Take_Damage(pl.weapon)
            
            if X == 0 and Y != 0 and Y != 14:
                if matriz[X][Y] == 0 and (matriz[X+1][Y] == 1 or matriz[X][Y-1] == 1 or matriz[X][Y+1] == 1):
                    matriz[X][Y] == 1
                    b[X+1][Y+1].config(text = "X")
                if matriz[X][Y] > 0:
                    Enemys.Take_Damage(pl.weapon)
                
            if Y == 0 and X != 0 and X != 14:
                if matriz[X][Y] == 0 and (matriz[X+1][Y] == 1 or matriz[X-1][Y] == 1 or matriz[X][Y+1] == 1):
                    matriz[X][Y] == 1
                    b[X+1][Y+1].config(text = "X")
                if matriz[X][Y] > 0:
                    Enemys.Take_Damage(pl.weapon)
                    
            if X == 14 and Y != 0 and Y != 14:
                if matriz[X][Y] == 0 and (matriz[X-1][Y] == 1 or matriz[X][Y-1] == 1 or matriz[X][Y+1] == 1):
                    matriz[X][Y] == 1
                    b[X+1][Y+1].config(text = "X")
                if matriz[X][Y] > 0:
                    Enemys.Take_Damage(pl.weapon)
                
            if Y == 14 and X != 0 and X != 14:
                if matriz[X][Y] == 0 and (matriz[X+1][Y] == 1 or matriz[X][Y-1] == 1 or matriz[X-1][Y] == 1):
                    matriz[X][Y] == 1
                    b[X+1][Y+1].config(text = "X")
                if matriz[X][Y] > 0:
                    Enemys.Take_Damage(pl.weapon)

        else:
            if matriz[X][Y] == 0:
                matriz[X][Y] == 1
                b[X+1][Y+1].config(text = "X")
            if matriz[X][Y] > 0:
                Enemys.Take_Damage(pl.weapon)
     
    def load_map(window):
           
        b00_00 = Button(window, text = "")
        b01_00 = Button(window, text = "")
        b02_00 = Button(window, text = "")
        b03_00 = Button(window, text = "")
        b04_00 = Button(window, text = "")
        b05_00 = Button(window, text = "")
        b06_00 = Button(window, text = "")
        b07_00 = Button(window, text = "")
        b08_00 = Button(window, text = "")
        b09_00 = Button(window, text = "")
        b10_00 = Button(window, text = "")
        b11_00 = Button(window, text = "")
        b12_00 = Button(window, text = "")
        b13_00 = Button(window, text = "")
        b14_00 = Button(window, text = "")
        b15_00 = Button(window, text = "")

        b00_01 = Button(window, text = "")
        b01_01 = Button(window, text = "")
        b02_01 = Button(window, text = "")
        b03_01 = Button(window, text = "")
        b04_01 = Button(window, text = "")
        b05_01 = Button(window, text = "")
        b06_01 = Button(window, text = "")
        b07_01 = Button(window, text = "")
        b08_01 = Button(window, text = "")
        b09_01 = Button(window, text = "")
        b10_01 = Button(window, text = "")
        b11_01 = Button(window, text = "")
        b12_01 = Button(window, text = "")
        b13_01 = Button(window, text = "")
        b14_01 = Button(window, text = "")
        b15_01 = Button(window, text = "")
        
        b00_02 = Button(window, text = "")
        b01_02 = Button(window, text = "")
        b02_02 = Button(window, text = "")
        b03_02 = Button(window, text = "")
        b04_02 = Button(window, text = "")
        b05_02 = Button(window, text = "")
        b06_02 = Button(window, text = "")
        b07_02 = Button(window, text = "")
        b08_02 = Button(window, text = "")
        b09_02 = Button(window, text = "")
        b10_02 = Button(window, text = "")
        b11_02 = Button(window, text = "")
        b12_02 = Button(window, text = "")
        b13_02 = Button(window, text = "")
        b14_02 = Button(window, text = "")
        b15_02 = Button(window, text = "")
        
        b00_03 = Button(window, text = "")
        b01_03 = Button(window, text = "")
        b02_03 = Button(window, text = "")
        b03_03 = Button(window, text = "")
        b04_03 = Button(window, text = "")
        b05_03 = Button(window, text = "")
        b06_03 = Button(window, text = "")
        b07_03 = Button(window, text = "")
        b08_03 = Button(window, text = "")
        b09_03 = Button(window, text = "")
        b10_03 = Button(window, text = "")
        b11_03 = Button(window, text = "")
        b12_03 = Button(window, text = "")
        b13_03 = Button(window, text = "")
        b14_03 = Button(window, text = "")
        b15_03 = Button(window, text = "")
        
        b00_04 = Button(window, text = "")
        b01_04 = Button(window, text = "")
        b02_04 = Button(window, text = "")
        b03_04 = Button(window, text = "")
        b04_04 = Button(window, text = "")
        b05_04 = Button(window, text = "")
        b06_04 = Button(window, text = "")
        b07_04 = Button(window, text = "")
        b08_04 = Button(window, text = "")
        b09_04 = Button(window, text = "")
        b10_04 = Button(window, text = "")
        b11_04 = Button(window, text = "")
        b12_04 = Button(window, text = "")
        b13_04 = Button(window, text = "")
        b14_04 = Button(window, text = "")
        b15_04 = Button(window, text = "")
        
        b00_05 = Button(window, text = "")
        b01_05 = Button(window, text = "")
        b02_05 = Button(window, text = "")
        b03_05 = Button(window, text = "")
        b04_05 = Button(window, text = "")
        b05_05 = Button(window, text = "")
        b06_05 = Button(window, text = "")
        b07_05 = Button(window, text = "")
        b08_05 = Button(window, text = "")
        b09_05 = Button(window, text = "")
        b10_05 = Button(window, text = "")
        b11_05 = Button(window, text = "")
        b12_05 = Button(window, text = "")
        b13_05 = Button(window, text = "")
        b14_05 = Button(window, text = "")
        b15_05 = Button(window, text = "")
        
        b00_06 = Button(window, text = "")
        b01_06 = Button(window, text = "")
        b02_06 = Button(window, text = "")
        b03_06 = Button(window, text = "")
        b04_06 = Button(window, text = "")
        b05_06 = Button(window, text = "")
        b06_06 = Button(window, text = "")
        b07_06 = Button(window, text = "")
        b08_06 = Button(window, text = "")
        b09_06 = Button(window, text = "")
        b10_06 = Button(window, text = "")
        b11_06 = Button(window, text = "")
        b12_06 = Button(window, text = "")
        b13_06 = Button(window, text = "")
        b14_06 = Button(window, text = "")
        b15_06 = Button(window, text = "")
        
        b00_07 = Button(window, text = "")
        b01_07 = Button(window, text = "")
        b02_07 = Button(window, text = "")
        b03_07 = Button(window, text = "")
        b04_07 = Button(window, text = "")
        b05_07 = Button(window, text = "")
        b06_07 = Button(window, text = "")
        b07_07 = Button(window, text = "")
        b08_07 = Button(window, text = "")
        b09_07 = Button(window, text = "")
        b10_07 = Button(window, text = "")
        b11_07 = Button(window, text = "")
        b12_07 = Button(window, text = "")
        b13_07 = Button(window, text = "")
        b14_07 = Button(window, text = "")
        b15_07 = Button(window, text = "")
        
        b00_08 = Button(window, text = "")
        b01_08 = Button(window, text = "")
        b02_08 = Button(window, text = "")
        b03_08 = Button(window, text = "")
        b04_08 = Button(window, text = "")
        b05_08 = Button(window, text = "")
        b06_08 = Button(window, text = "")
        b07_08 = Button(window, text = "")
        b08_08 = Button(window, text = "")
        b09_08 = Button(window, text = "")
        b10_08 = Button(window, text = "")
        b11_08 = Button(window, text = "")
        b12_08 = Button(window, text = "")
        b13_08 = Button(window, text = "")
        b14_08 = Button(window, text = "")
        b15_08 = Button(window, text = "")
        
        b00_09 = Button(window, text = "")
        b01_09 = Button(window, text = "")
        b02_09 = Button(window, text = "")
        b03_09 = Button(window, text = "")
        b04_09 = Button(window, text = "")
        b05_09 = Button(window, text = "")
        b06_09 = Button(window, text = "")
        b07_09 = Button(window, text = "")
        b08_09 = Button(window, text = "")
        b09_09 = Button(window, text = "")
        b10_09 = Button(window, text = "")
        b11_09 = Button(window, text = "")
        b12_09 = Button(window, text = "")
        b13_09 = Button(window, text = "")
        b14_09 = Button(window, text = "")
        b15_09 = Button(window, text = "")
        
        b00_10 = Button(window, text = "")
        b01_10 = Button(window, text = "")
        b02_10 = Button(window, text = "")
        b03_10 = Button(window, text = "")
        b04_10 = Button(window, text = "")
        b05_10 = Button(window, text = "")
        b06_10 = Button(window, text = "")
        b07_10 = Button(window, text = "")
        b08_10 = Button(window, text = "")
        b09_10 = Button(window, text = "")
        b10_10 = Button(window, text = "")
        b11_10 = Button(window, text = "")
        b12_10 = Button(window, text = "")
        b13_10 = Button(window, text = "")
        b14_10 = Button(window, text = "")
        b15_10 = Button(window, text = "")
        
        b00_11 = Button(window, text = "")
        b01_11 = Button(window, text = "")
        b02_11 = Button(window, text = "")
        b03_11 = Button(window, text = "")
        b04_11 = Button(window, text = "")
        b05_11 = Button(window, text = "")
        b06_11 = Button(window, text = "")
        b07_11 = Button(window, text = "")
        b08_11 = Button(window, text = "")
        b09_11 = Button(window, text = "")
        b10_11 = Button(window, text = "")
        b11_11 = Button(window, text = "")
        b12_11 = Button(window, text = "")
        b13_11 = Button(window, text = "")
        b14_11 = Button(window, text = "")
        b15_11 = Button(window, text = "")
        
        b00_12 = Button(window, text = "")
        b01_12 = Button(window, text = "")
        b02_12 = Button(window, text = "")
        b03_12 = Button(window, text = "")
        b04_12 = Button(window, text = "")
        b05_12 = Button(window, text = "")
        b06_12 = Button(window, text = "")
        b07_12 = Button(window, text = "")
        b08_12 = Button(window, text = "")
        b09_12 = Button(window, text = "")
        b10_12 = Button(window, text = "")
        b11_12 = Button(window, text = "")
        b12_12 = Button(window, text = "")
        b13_12 = Button(window, text = "")
        b14_12 = Button(window, text = "")
        b15_12 = Button(window, text = "")
        
        b00_13 = Button(window, text = "")
        b01_13 = Button(window, text = "")
        b02_13 = Button(window, text = "")
        b03_13 = Button(window, text = "")
        b04_13 = Button(window, text = "")
        b05_13 = Button(window, text = "")
        b06_13 = Button(window, text = "")
        b07_13 = Button(window, text = "")
        b08_13 = Button(window, text = "")
        b09_13 = Button(window, text = "")
        b10_13 = Button(window, text = "")
        b11_13 = Button(window, text = "")
        b12_13 = Button(window, text = "")
        b13_13 = Button(window, text = "")
        b14_13 = Button(window, text = "")
        b15_13 = Button(window, text = "")
        
        b00_14 = Button(window, text = "")
        b01_14 = Button(window, text = "")
        b02_14 = Button(window, text = "")
        b03_14 = Button(window, text = "")
        b04_14 = Button(window, text = "")
        b05_14 = Button(window, text = "")
        b06_14 = Button(window, text = "")
        b07_14 = Button(window, text = "")
        b08_14 = Button(window, text = "")
        b09_14 = Button(window, text = "")
        b10_14 = Button(window, text = "")
        b11_14 = Button(window, text = "")
        b12_14 = Button(window, text = "")
        b13_14 = Button(window, text = "")
        b14_14 = Button(window, text = "")
        b15_14 = Button(window, text = "")
        
        b00_15 = Button(window, text = "")
        b01_15 = Button(window, text = "")
        b02_15 = Button(window, text = "")
        b03_15 = Button(window, text = "")
        b04_15 = Button(window, text = "")
        b05_15 = Button(window, text = "")
        b06_15 = Button(window, text = "")
        b07_15 = Button(window, text = "")
        b08_15 = Button(window, text = "")
        b09_15 = Button(window, text = "")
        b10_15 = Button(window, text = "")
        b11_15 = Button(window, text = "")
        b12_15 = Button(window, text = "")
        b13_15 = Button(window, text = "")
        b14_15 = Button(window, text = "")
        b15_15 = Button(window, text = "")

        b = [[b00_00, b01_00, b02_00, b03_00, b04_00, b05_00, b06_00, b07_00, b08_00, b09_00, b10_00, b11_00, b12_00, b13_00, b14_00, b15_00],
        [b00_01, b01_01, b02_01, b03_01, b04_01, b05_01, b06_01, b07_01, b08_01, b09_01, b10_01, b11_01, b12_01, b13_01, b14_01, b15_01],
        [b00_02, b01_02, b02_02, b03_02, b04_02, b05_02, b06_02, b07_02, b08_02, b09_02, b10_02, b11_02, b12_02, b13_02, b14_02, b15_02],
        [b00_03, b01_03, b02_03, b03_03, b04_03, b05_03, b06_03, b07_03, b08_03, b09_03, b10_03, b11_03, b12_03, b13_03, b14_03, b15_03],
        [b00_04, b01_04, b02_04, b03_04, b04_04, b05_04, b06_04, b07_04, b08_04, b09_04, b10_04, b11_04, b12_04, b13_04, b14_04, b15_04],
        [b00_05, b01_05, b02_05, b03_05, b04_05, b05_05, b06_05, b07_05, b08_05, b09_05, b10_05, b11_05, b12_05, b13_05, b14_05, b15_05],
        [b00_06, b01_06, b02_06, b03_06, b04_06, b05_06, b06_06, b07_06, b08_06, b09_06, b10_06, b11_06, b12_06, b13_06, b14_06, b15_06],
        [b00_07, b01_07, b02_07, b03_07, b04_07, b05_07, b06_07, b07_07, b08_07, b09_07, b10_07, b11_07, b12_07, b13_07, b14_07, b15_07],
        [b00_08, b01_08, b02_08, b03_08, b04_08, b05_08, b06_08, b07_08, b08_08, b09_08, b10_08, b11_08, b12_08, b13_08, b14_08, b15_08],
        [b00_09, b01_09, b02_09, b03_09, b04_09, b05_09, b06_09, b07_09, b08_09, b09_09, b10_09, b11_09, b12_09, b13_09, b14_09, b15_09],
        [b00_10, b01_10, b02_10, b03_10, b04_10, b05_10, b06_10, b07_10, b08_10, b09_10, b10_10, b11_10, b12_10, b13_10, b14_10, b15_10],
        [b00_11, b01_11, b02_11, b03_11, b04_11, b05_11, b06_11, b07_11, b08_11, b09_11, b10_11, b11_11, b12_11, b13_11, b14_11, b15_11],
        [b00_12, b01_12, b02_12, b03_12, b04_12, b05_12, b06_12, b07_12, b08_12, b09_12, b10_12, b11_12, b12_12, b13_12, b14_12, b15_12],
        [b00_13, b01_13, b02_13, b03_13, b04_13, b05_13, b06_13, b07_13, b08_13, b09_13, b10_13, b11_13, b12_13, b13_13, b14_13, b15_13],
        [b00_14, b01_14, b02_14, b03_14, b04_14, b05_14, b06_14, b07_14, b08_14, b09_14, b10_14, b11_14, b12_14, b13_14, b14_14, b15_14],
        [b00_15, b01_15, b02_15, b03_15, b04_15, b05_15, b06_15, b07_15, b08_15, b09_15, b10_15, b11_15, b12_15, b13_15, b14_15, b15_15]]
               
        matriz = np.zeros([15, 15])
        matriz[7][7] = 1
        
        Mapa.create_button(b, matriz)
        
        return b, matriz
        
    def create_button(b, matriz):
        for i in range(0,14):
            for j in range(0,14):
                b[i][j].config(command=lambda: Mapa.detect_click(i,j, matriz, b))
                b[i][j].config( height = 2, width = 4)
                b[i][j].grid(row=i, column=j)