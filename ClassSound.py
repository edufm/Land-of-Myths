# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:45:54 2016

@author: Hugo
"""
import ClasseTrack

import winsound as ws
import random

class sound():
    def __init__(self,play):
        self.play = play
        
    def play_music(play):
        if ClasseTrack.Tracker.Music == 0:
            ws.PlaySound(play, ws.SND_ASYNC)
            ClasseTrack.Tracker.Music = 1
        else:
            ws.PlaySound(None, ws.SND_PURGE)
            ClasseTrack.Tracker.Music = 0
    
    def Stop_All():
        ws.PlaySound(None, ws.SND_PURGE)
        ClasseTrack.Tracker.Music = 0
        
    def Choose_music():
        musics = [got.play, skyrim.play, pirates.play]
        a = random.randint(0, 2)
        
        return musics[a]
    
got = sound(".\\sounds\\got.wav")
skyrim = sound(".\\sounds\\skyrim.wav")
pirates = sound(".\\sounds\\pirates.wav")
    