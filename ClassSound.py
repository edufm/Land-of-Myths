# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:45:54 2016

@author: Hugo
"""

import winsound as ws
import threading
import random

class sound():
    def __init__(self,play):
        self.play = play
        
    def play_music(play):
        playSound = lambda: ws.PlaySound(play,ws.SND_FILENAME)
        t = threading.Thread(target = playSound)
        t.start()
        
    def Choose_music():
        musics = [ got.play,skyrim.play, pirates.play]
        a= random.randint(0,2)
        
        return musics[a]
    
got = sound(".\\sounds\\got.wav")
skyrim = sound(".\\sounds\\skyrim.wav")
pirates = sound(".\\sounds\\pirates.wav")
    