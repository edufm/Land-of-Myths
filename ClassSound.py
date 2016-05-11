# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:45:54 2016

@author: Hugo
"""

import winsound as ws

class sound():
    def __init__(self,play):
        self.play = ws.PlaySound(play, ws.SND_FILENAME)
        
    
got = sound(".\\sounds\\got.wav")
skyrim = sound(".\\sounds\\skyrim.wav")
pirates = sound(".\\sounds\\pirates.wav")
    