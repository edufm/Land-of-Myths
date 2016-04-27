# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:03:18 2016

@author: Eh Nòis
"""

from tkinter import *
import numpy as np


from ClasseEnemys import Enemys
from ClasseGun import Gun
from ClasseMapa import Mapa
from ClassePlayer import Player

               
window = Tk()
window.title("Não sabemos ainda")
window.geometry("1366x728")
               
Mapa.load_map(window)

window.mainloop()