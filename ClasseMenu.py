# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:50:21 2016

@author: Hugo
"""
from tkinter import *

window = Tk()
window.title("Magic Trap")
window.configure(bg="black")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(),window.winfo_screenheight()))

from ClasseMapa import Mapa
from ClasseImagens import *
from ClassSound import *

class Menu():
    def __init__(self, lista):
        self.lista = lista
        
        
    def Construir_menu():
            
            sound.menu_music()
            
            menu = Menu([])
            
            Imagemdo = Label(window)
            Imagemdo.config(image = Sniper)
            Imagemdo.image = Sniper            
            
            lMenu = Label(window)
            lMenu.config(text = "MENU", height = 5, width = 36,bg="black",foreground="red",font=("castelar",40))
            lMenu.place(x=130, y=40)
    
            Play = Button(window)
            Play.config(text="Play",font=("castelar",20))
            Play.config(height = 2 , width = 15)
            Play.configure(command = lambda : Menu.clear_start(menu))
            Play.place(x=575, y= 300)
            
            Rank = Button(window)
            Rank.configure(text="Rank",font=("castelar",20))
            Rank.config(height = 2 , width = 15)
            Rank.place(x = 575 , y = 400)
            
            Exit = Button(window)
            Exit.config(text="Exit",font=("castelar",20))
            Exit.config(height = 2 , width = 15)
            Exit.config(command =lambda: Mapa.Exit(window))
            Exit.place(x=575, y= 500)
            
            menu.lista.append(Play)
            menu.lista.append(Rank)
            menu.lista.append(lMenu)
            menu.lista.append(Exit)
        
            window.mainloop()
    
    def clear_start(menu):
        for i in menu.lista:
            i.destroy()
        ws.PlaySound(None,ws.SND_PURGE)
        Mapa.Start_Game(0, 0, window)
        
