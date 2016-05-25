import threading

import ClasseMapa
import ClasseTrack
def Timer(pl,Turn):
    if Turn == ClasseTrack.Tracker.Turn - 1 or turn == ClasseTrack.Tracker.Turn:
        print ("=",Turn,ClasseTrack.Tracker.Turn)
        ClasseMapa.Mapa.Roda_jogo(ClasseTrack.Tracker.Map,pl)
    
