# -*- coding: utf-8 -*-
"""
Created on Mon May 23 16:59:38 2016

@author: Jean Walper
"""
import threading
import time
import random

def hello():
    print ("you lost")
    print ("dont try again")
    time.sleep(999)
    
def Jogar():
    t = threading.Timer(2.5, hello) # timer in secconds, hello is the name of my function
    t.start()  # after 2,5 seconds, Hello will be played (it stops the game)

    lista = ["mummy", "dad", 'grandma', 'face-spin', 'fish', 'blue', 'orange', "Hi!I'm Brazilian",'one feet', 'scared', 'laught','anagramm','forever','squirrel','tree, two, one']

    rand = random.randint(0,15)

    y = ('write :',lista[rand])

    print("FAST!!! YOU ONLY GOT 2.5 SECCONDS!!!!")

    x = input(y)

    if x == y[1]:
        t.cancel() # If you manage to do it right, the timer is cancelled
        print('CONGRATS :), now do it again >:)')
        time.sleep(1)
        Jogar()

print ("write the words that appears fast")
time.sleep(3)

Jogar()
