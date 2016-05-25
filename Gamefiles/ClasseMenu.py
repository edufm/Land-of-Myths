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
            
            background = Label(window)           
            imagem = PhotoImage(file=".//Imagens//Sprites//background1.png")
            background.config(image = imagem )
            background.image = imagem
            background.grid(row=0,column = 0)
                        
            
            menu = Menu([])
            
            Imagemdo = Label(window)
            Imagemdo.config(image = Sniper)
            Imagemdo.image = Sniper            
            
#            lMenu = Label(window)
#            menuzinho = PhotoImage(file=".//Imagens//Sprites//titulo.png")
#            lMenu.config(image = menuzinho, bg = "black")
#            lMenu.image = menuzinho
#            lMenu.place(x=370, y=75)
    
            Play = Button(window)
            Play.config(text="Play",font=("impact",20),bg = "white")
            Play.config(height = 2 , width = 15)
            Play.configure(command = lambda : Menu.clear_start(menu))
            Play.place(x=575, y= 330)
            
            Rank = Button(window)
            Rank.configure(text="Rank",font=("impact",20),bg = "white")
            Rank.config(height = 2 , width = 15)
            Rank.place(x = 575 , y = 430)
            
            Exit = Button(window)
            Exit.config(text="Exit",font=("impact",20),bg = "white")
            Exit.config(height = 2 , width = 15)
            Exit.config(command =lambda: Mapa.Exit(window))
            Exit.place(x=575, y= 530)
            
            Music = Button(window)
            Music.config(image = MusicOn)
            Music.image = MusicOn
            Music.config(height = 48 , width = 48)
            Music.configure(command = lambda : menu.Enable_music())
            Music.place(x=1270, y= 650)
            
            menu.lista.append(Play)
            menu.lista.append(Rank)
            menu.lista.append(background)
            menu.lista.append(Exit)
            menu.lista.append(Music)
        
            window.mainloop()
            
    def Enable_music(self):
        if ClasseTrack.Tracker.Musicenabled:
            ClasseTrack.Tracker.Musicenabled = False
            self.lista[-1].config(image= MusicOff)
            self.lista[-1].image = MusicOff
            sound.Stop_All()
            
        else:
            ClasseTrack.Tracker.Musicenabled = True
            self.lista[-1].config(image=MusicOn)
            self.lista[-1].image = MusicOn
            sound.menu_music()
    
    def clear_start(menu):
        for i in menu.lista:
            i.destroy()

        ws.PlaySound(None,ws.SND_PURGE)
        Mapa.Start_Game(0, 0, window)
        
