# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:50:21 2016

@author: Hugo
"""
import ClasseMapa
from ClasseImagens import *
from tkinter import *

class Menu():
    def __init__(self,criar):
        self.criar = criar
        
        
    def Construir_menu(window):
            window.configure(image = background_menu  )
            window.image = background_menu
            Menu = Label(window)
            Menu.config(text = "MENU", height = 5, width = 36,bg="black",foreground="red",font=("castelar",40))
            
            Menu.place(x=130, y=40)
    
            Play = Button(window)
            Play.place(x=525, y= 300)
            
            Rank = Button(window)
            Rank.configure(text="Rank")
            Rank.place(x = 525 , y = 500)
            
            Exit = Button(window)
            Exit.config(command =lambda: Mapa.Exit())
            Exit.place(x=525, y= 700)
    

