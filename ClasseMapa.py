
from tkinter import *
import numpy as np

window = Tk()
window.title("Magic Trap")
window.configure(bg="black")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(),window.winfo_screenheight()))

from ClasseEnemys import Enemys
import ClasseGun
from ClassePlayer import Player
import ClasseImagens
import ClasseTrack
from ClassSound import *

class Mapa():
    def __init__(self, matriz, b, gadjets, Waves, LEnemys):
        self.matriz = matriz
        self.b = b
        self.gadjets = gadjets
        self.Waves = Waves
        self.LEnemys = LEnemys
        
    def Start_Game(X, L):
        if X == 1:
            L[0].destroy()
            L[1].destroy()
            L[2].destroy()
        
        Map = Mapa(np.zeros([15, 27]), [], [], 0, [])   
        
        pl = Player(20, ClasseGun.Pistol, [7,13], [7, 0, 0])
        
        ClasseTrack.Tracker.Map = Map
        ClasseTrack.Tracker.pl = pl
        
        Map.matriz[7][13] = 1
        Mapa.load_map(Map, window, pl)
        Player.set_player(pl)
        
        Mapa.gui(window, Map, pl)
        
        window.bind("<Key>", Mapa.key)
        
        window.mainloop()
        
    def load_map(self, window, pl):
        
        for i in range(15):
            self.b.append([])
            for j in range(27):
                button = Button(window, text=' ',command= lambda m=[i,j]: self.Atira(m, pl))
                button.grid(row=i+1, column=j, sticky=W+E+S+N)
                button.config(image=ClasseImagens.Tiles[0])
                button.configure(height = 36, width = 36,bg = "black")
                button.image = ClasseImagens.Tiles[0]
                self.b[i].append(button)
                        
        self.b[7][13].config(image = ClasseImagens.player[0])
        self.b[7][13].image = ClasseImagens.player[0]

    def key(event):
        if repr(event.char) == "'w'":
            m = [ClasseTrack.Tracker.pl.pos[0]-1, ClasseTrack.Tracker.pl.pos[1]]
            Mapa.Andar(ClasseTrack.Tracker.Map, m, ClasseTrack.Tracker.pl)
        if repr(event.char) == "'s'":
            m = [ClasseTrack.Tracker.pl.pos[0]+1, ClasseTrack.Tracker.pl.pos[1]]
            Mapa.Andar(ClasseTrack.Tracker.Map, m, ClasseTrack.Tracker.pl)
        if repr(event.char) == "'a'":
            m = [ClasseTrack.Tracker.pl.pos[0], ClasseTrack.Tracker.pl.pos[1]-1]
            Mapa.Andar(ClasseTrack.Tracker.Map, m, ClasseTrack.Tracker.pl)
        if repr(event.char) == "'d'":
            m = [ClasseTrack.Tracker.pl.pos[0], ClasseTrack.Tracker.pl.pos[1]+1]
            Mapa.Andar(ClasseTrack.Tracker.Map, m, ClasseTrack.Tracker.pl)
        if repr(event.char) == "'x'":
            m = [ClasseTrack.Tracker.pl.pos[0], ClasseTrack.Tracker.pl.pos[1]]
            Mapa.Andar(ClasseTrack.Tracker.Map, m, ClasseTrack.Tracker.pl)
        if repr(event.char) == "'1'" and ClasseTrack.Tracker.pl.inv[0] > 0:
            Mapa.Botão_de_arma(ClasseTrack.Tracker.Map, ClasseTrack.Tracker.pl, 0)
        if repr(event.char) == "'2'" and ClasseTrack.Tracker.pl.inv[1] > 0:
            Mapa.Botão_de_arma(ClasseTrack.Tracker.Map, ClasseTrack.Tracker.pl, 1)
        if repr(event.char) == "'3'" and ClasseTrack.Tracker.pl.inv[2] > 0:
            Mapa.Botão_de_arma(ClasseTrack.Tracker.Map, ClasseTrack.Tracker.pl, 2)
            
    def Andar(self, m, pl):
        
        click_errado = 0  
        X = m[0]
        Y = m[1]
        Xp = pl.pos[0]
        Yp = pl.pos[1]
        
        if (X < 15 and X >= 0) and (Y < 27 and Y >= 0):
        
            b = self.b
            V = self.matriz[X][Y] == 0
            G = self.matriz[X][Y] > 99
            GN = int(self.matriz[X][Y]) - 100

            if (G or V) and X+1 == Xp and Y == Yp:
                if G:
                    ClasseGun.Gun.Pick_Weapon(GN, pl)
                #Adiciona o player no novo lugar
                self.matriz[X][Y] = 1
                b[X][Y].config(image=ClasseImagens.player[3])
                b[X][Y].image = ClasseImagens.player[3]
                #Remove o "Rastro" do player
                self.matriz[Xp][Y] = 0
                b[Xp][Yp].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                b[Xp][Yp].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
                pl.pos = [X,Y]
                
            elif (G or V) and X-1 == Xp and Y == Yp:
                if G:
                    ClasseGun.Gun.Pick_Weapon(GN, pl)         
                self.matriz[X][Y] = 1
                b[X][Y].config(image=ClasseImagens.player[0])
                b[X][Y].image = ClasseImagens.player[0]
                self.matriz[Xp][Y] = 0
                b[Xp][Yp].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                b[Xp][Yp].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
                pl.pos = [X,Y]
    
            elif (G or V) and Y+1 == Yp and X == Xp:
                if G:
                    ClasseGun.Gun.Pick_Weapon(GN, pl)
                self.matriz[X][Y] = 1
                b[X][Y].config(image=ClasseImagens.player[2])
                b[X][Y].image = ClasseImagens.player[2]
                self.matriz[X][Yp] = 0
                b[Xp][Yp].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                b[Xp][Yp].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
                pl.pos = [X,Y]
                
            elif (G or V) and Y-1 == Yp and X == Xp:
                if G:
                    ClasseGun.Gun.Pick_Weapon(GN, pl)
                self.matriz[X][Y] = 1
                b[X][Y].config(image= ClasseImagens.player[1])
                b[X][Y].image = ClasseImagens.player[1]
                self.matriz[X][Yp] = 0
                b[Xp][Yp].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                b[Xp][Yp].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
                pl.pos = [X,Y]
    
            elif self.matriz[X][Y] == 1:
                click_errado = 0
                
            else:
                click_errado = 1
            
            if click_errado == 0:
                self.Roda_jogo(pl)
            
    def Atira(self, m, pl):
        X = m[0]
        Y = m[1]
        Enemys.Take_Damage([X,Y], pl, self)
        self.Roda_jogo(pl)
        sound.play_sound(shot.play)
        
    
    def Roda_jogo(self, pl):
        # Limpa o range se ele estiver ligado        
        if ClasseTrack.Tracker.Weaponselected == 1:
            self.Limpa_range(pl)
        #informa ao tracker que passou um turno
        ClasseTrack.Tracker.Turn += 1
        #faz a jogada dos inimigos para cada inimigo vivo
        for i in self.LEnemys:
            Enemys.jogada(i, pl, self)
        # atualiza as informações do Gui
        Mapa.updategui(self, self.gadjets, pl)
        #se acabaram os inimigos, gera uma nova onda
        if ((len(self.LEnemys)) == 0):
            self.Waves += 1
            Enemys.cria_inimigos(self.Waves, self)
            Mapa.update_map(self, pl)        
        #Gera aos itens no mapa
        ClasseGun.Gun.Gerar_Guns(self)

    def update_map(Map, pl):
        if (Map.Waves) % 4 == 0:
            ClasseTrack.Tracker.Boss += 1
            for i in range (15):
                for j in range(27):
                    if Map.matriz[i][j] == 0:
                        Map.b[i][j].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                        Map.b[i][j].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
                
    def gui(window, Map, pl):

        vida = Label(window)
        vida.configure(text="Life:",font=("castelar"),bg = "black",foreground = "white")
        vida.configure(height = 2 , width = 4)
        vida.grid(row=16,column=0)
        botãodevida1 = Button(window)
        botãodevida1.configure(bg="light blue")
        botãodevida1.configure(height = 2 , width = 20)
        botãodevida1.grid(row= 16,columnspan = 7)
        time = Label(window)
        time.configure(text="Time : {0}s".format(2.5),font=("castelar"),bg = "black",foreground="white")
        time.configure(height = 2, width = 8)
        time.grid(row= 16, column = 11,columnspan=100)
        wave = Label(window)
        wave.configure(text="Wave : {0}".format(1),font=("castelar"),bg = "black",foreground="white")
        wave.configure(height = 2, width = 7)
        wave.grid(row= 1, column = 28, columnspan= 2)
        nomejogo = Label(window)
        nomejogo.configure(text="I´ll survive" , font= ("Times",20),bg = "black",foreground="white")
        nomejogo.grid(row = 0 ,columnspan =100)

        Map.gadjets.append(vida)
        Map.gadjets.append(botãodevida1)
        Map.gadjets.append(time)
        Map.gadjets.append(wave)
        Map.gadjets.append(nomejogo)
        #Botões de armas
        Pistolb = Button(window)
        Pistolb.configure(height = 36, width = 36, state = 'disabled')
        Pistolb.configure(image = ClasseImagens.guns[0], command= lambda: Mapa.Botão_de_arma(Map, pl, 0))
        Pistolb.image = ClasseImagens.guns[0]
        Pistolb.grid(row = 5, column = 28, columnspan = 2)

        Pammo = Label(window)
        Pammo.configure(text="Ammo :   x{0}".format(0),font=("castelar"),bg = "black",foreground = "white")
        Pammo.configure(height = 2, width = 15)
        Pammo.grid(row= 5, column = 30)

        shotgunb = Button(window)
        shotgunb.configure(height = 36, width = 36, state = 'disabled')
        shotgunb.configure(image = ClasseImagens.guns[1], command= lambda: Mapa.Botão_de_arma(Map, pl, 1))
        shotgunb.image = ClasseImagens.guns[1]
        shotgunb.grid(row = 7, column = 28, columnspan = 2)

        shotammo = Label(window)
        shotammo.configure(text="Ammo :   x{0}".format(0),font=("castelar"),bg = "black",foreground = "white")
        shotammo.configure(height = 2, width = 15)
        shotammo.grid(row= 7, column = 30)

        Sniperb = Button(window)
        Sniperb.configure(height = 36, width = 36, state = 'disabled')
        Sniperb.configure(image = ClasseImagens.guns[2], command= lambda: Mapa.Botão_de_arma(Map, pl, 2))
        Sniperb.image = ClasseImagens.guns[2]
        Sniperb.grid(row = 9, column = 28, columnspan = 2)

        snipeammo = Label(window)
        snipeammo.configure(text="Ammo :   x{0}".format(0),font=("castelar"),bg = "black",foreground = "white")
        snipeammo.configure(height = 2, width = 15)
        snipeammo.grid(row= 9, column = 30)
        
        musicbutton = Button(window)
        musicbutton.configure(text = " Play Music",bg = "white",font=("castelar"),command = lambda : sound.play_music(sound.Choose_music()) )
        musicbutton.grid(row =12,column = 30)
        
        exitbutton = Button(window)
        exitbutton.configure(text = "Exit",bg = "white",font=("castelar"),command = lambda : Mapa.Exit())
        exitbutton.grid(row = 16,column = 30)
        
        Map.gadjets.append(Pistolb)
        Map.gadjets.append(Pammo)
        Map.gadjets.append(shotgunb)
        Map.gadjets.append(shotammo)
        Map.gadjets.append(Sniperb)
        Map.gadjets.append(snipeammo)
         
    def updategui(Map, gadjets, pl):
        if pl.health <= 0:
            for i in range(15):
                for j in range(27):
                    Map.b[i][j].destroy()
            for i in gadjets:
                i.destroy()
            
            youdied = Label(window)
            youdied.config(text = "Whatta shame, you died!!", height = 5, width = 36,bg="black",foreground="red",font=("castelar",40))
            
            youdied.place(x=130, y=40)
    
            giveup = Button(window)
            giveup.config(command =lambda: Mapa.Exit())
            exiit = PhotoImage(file=".\\Imagens\\Sprites\\exit.png")
            giveup.image = exiit
            giveup.config(image=exiit,bg="black")
            giveup.place(x=525, y= 300)
            
            restart = Button(window)
            restart.config(command =lambda: Mapa.Start_Game(1, [youdied, restart, giveup]))
            restartt = PhotoImage(file=".\\Imagens\\Sprites\\reset-button-hi.png")
            restart.image = restartt
            restart.config(image=restartt,bg="black")
            restart.place(x=525, y= 500)
        
        else:
            gadjets[1].configure(height = 2 , width = pl.health)
            gadjets[2].configure(text="Time : {0}s".format(2.5),font=("castelar"),bg = "black",foreground="white")
            gadjets[3].configure(text="Wave : {0}".format(Map.Waves),font=("castelar"),bg = "black",foreground="white")
            
            if pl.inv[0] > 0:
                gadjets[5].config(state = 'active')
            
            if pl.inv[1] > 0:
                gadjets[7].config(state = 'active')
                
            if pl.inv[2] > 0:
                gadjets[9].config(state = 'active')
            
            gadjets[6].config(text = 'Ammo X{0}'.format(pl.inv[0]))        
            gadjets[8].config(text = 'Ammo X{0}'.format(pl.inv[1]))
            gadjets[10].config(text = 'Ammo X{0}'.format(pl.inv[2]))
            
    def Botão_de_arma(Map, pl, X):
        if ClasseTrack.Tracker.Weaponselected == 1:
            Map.Limpa_range(pl)
        else:
            Mapa.mostrarange(pl, Map, X)
        pl.weapon = ClasseGun.WeaponList[X]
        
        
    def Limpa_range(self, pl):
        for i in range(8):
            for j in range(8):
                if i + j != 0:
                    if pl.pos[0] - i >= 0 and pl.pos[1] - j >= 0 and self.matriz[pl.pos[0]-i][pl.pos[1]-j] == 0:
                        self.b[pl.pos[0]-i][pl.pos[1]-j].config(image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                        self.b[pl.pos[0]-i][pl.pos[1]-j].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
                    if pl.pos[0] + i < 15 and pl.pos[1] - j >= 0 and self.matriz[pl.pos[0]+i][pl.pos[1]-j] == 0:
                        self.b[pl.pos[0]+i][pl.pos[1]-j].config(image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                        self.b[pl.pos[0]+i][pl.pos[1]-j].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
                    if pl.pos[1] + j < 27 and pl.pos[0] - i >= 0 and self.matriz[pl.pos[0]-i][pl.pos[1]+j] == 0:
                        self.b[pl.pos[0]-i][pl.pos[1]+j].config(image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                        self.b[pl.pos[0]-i][pl.pos[1]+j].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
                    if pl.pos[0] + i < 15 and pl.pos[1] + j < 27 and self.matriz[pl.pos[0]+i][pl.pos[1]+j] == 0:
                        self.b[pl.pos[0]+i][pl.pos[1]+j].config(image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                        self.b[pl.pos[0]+i][pl.pos[1]+j].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
        ClasseTrack.Tracker.Weaponselected = 0

    def mostrarange(pl, Map, X):
        ClasseTrack.Tracker.Weaponselected = 1
        if X == 0:
            for i in range(7):
                for j in range(7):
                    if i + j < 7 and pl.pos[0] - i >= 0 and pl.pos[1] - j >= 0 and Map.matriz[pl.pos[0]-i][pl.pos[1]-j] == 0:
                        Map.b[pl.pos[0]-i][pl.pos[1]-j].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                        Map.b[pl.pos[0]-i][pl.pos[1]-j].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
                    if i + j < 7 and pl.pos[0] + i < 15 and pl.pos[1] - j >= 0 and Map.matriz[pl.pos[0]+i][pl.pos[1]-j] == 0:
                        Map.b[pl.pos[0]+i][pl.pos[1]-j].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                        Map.b[pl.pos[0]+i][pl.pos[1]-j].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
                    if i + j < 7 and pl.pos[1] + j < 27 and pl.pos[0] - i >= 0 and Map.matriz[pl.pos[0]-i][pl.pos[1]+j] == 0:
                        Map.b[pl.pos[0]-i][pl.pos[1]+j].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                        Map.b[pl.pos[0]-i][pl.pos[1]+j].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
                    if i + j < 7 and pl.pos[0] + i < 15 and pl.pos[1] + j < 27 and Map.matriz[pl.pos[0]+i][pl.pos[1]+j] == 0:
                        Map.b[pl.pos[0]+i][pl.pos[1]+j].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                        Map.b[pl.pos[0]+i][pl.pos[1]+j].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
            Map.b[pl.pos[0]][pl.pos[1]].config(image = ClasseImagens.player[0])
            Map.b[pl.pos[0]][pl.pos[1]].image = ClasseImagens.player[0]
            
        if X == 1:
            if pl.pos[0]+1 < 15 and pl.pos[1] and Map.matriz[pl.pos[0]+1][pl.pos[1]] == 0:
                Map.b[pl.pos[0]+1][pl.pos[1]].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]+1][pl.pos[1]].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]+2 < 15 and pl.pos[1]-1 >= 0 and Map.matriz[pl.pos[0]+2][pl.pos[1]-1] == 0:
                Map.b[pl.pos[0]+2][pl.pos[1]-1].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]+2][pl.pos[1]-1].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]+2 < 15 and pl.pos[1]+1 < 27 and Map.matriz[pl.pos[0]+2][pl.pos[1]+1] == 0:
                Map.b[pl.pos[0]+2][pl.pos[1]+1].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]+2][pl.pos[1]+1].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]-1 >= 0 and Map.matriz[pl.pos[0]-1][pl.pos[1]] == 0:
                Map.b[pl.pos[0]-1][pl.pos[1]].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]-1][pl.pos[1]].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]-2 >= 0 and pl.pos[1]-1 >= 0 and Map.matriz[pl.pos[0]-2][pl.pos[1]-1] == 0:
                Map.b[pl.pos[0]-2][pl.pos[1]-1].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]-2][pl.pos[1]-1].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]-2 >= 0 and pl.pos[1]+1 < 27 and Map.matriz[pl.pos[0]-2][pl.pos[1]+1] == 0:
                Map.b[pl.pos[0]-2][pl.pos[1]+1].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]-2][pl.pos[1]+1].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[1]+1 < 27 and Map.matriz[pl.pos[0]][pl.pos[1]+1] == 0:
                Map.b[pl.pos[0]][pl.pos[1]+1].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]][pl.pos[1]+1].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]+1 < 15 and pl.pos[1]+2 < 27 and Map.matriz[pl.pos[0]+1][pl.pos[1]+2] == 0:
                Map.b[pl.pos[0]+1][pl.pos[1]+2].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]+1][pl.pos[1]+2].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]-1 >= 0 and pl.pos[1]+2 < 27 and Map.matriz[pl.pos[0]-1][pl.pos[1]+2] == 0:
                Map.b[pl.pos[0]-1][pl.pos[1]+2].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]-1][pl.pos[1]+2].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[1]-1 >= 0 and Map.matriz[pl.pos[0]][pl.pos[1]-1] == 0:
                Map.b[pl.pos[0]][pl.pos[1]-1].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]][pl.pos[1]-1].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]-1 >= 0 and pl.pos[1]-2 >= 0 and Map.matriz[pl.pos[0]-1][pl.pos[1]-2] == 0:
                Map.b[pl.pos[0]-1][pl.pos[1]-2].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]-1][pl.pos[1]-2].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]+1 < 15 and pl.pos[1]-2 >= 0 and Map.matriz[pl.pos[0]+1][pl.pos[1]-2] == 0:
                Map.b[pl.pos[0]+1][pl.pos[1]-2].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]+1][pl.pos[1]-2].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
        
        if X == 2:
            if pl.pos[0]+1 < 15 and pl.pos[1] and Map.matriz[pl.pos[0]+1][pl.pos[1]] == 0:
                Map.b[pl.pos[0]+1][pl.pos[1]].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]+1][pl.pos[1]].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[0]-1 >= 0 and Map.matriz[pl.pos[0]-1][pl.pos[1]] == 0:
                Map.b[pl.pos[0]-1][pl.pos[1]].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]-1][pl.pos[1]].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[1]+1 < 27 and Map.matriz[pl.pos[0]][pl.pos[1]+1] == 0:
                Map.b[pl.pos[0]][pl.pos[1]+1].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]][pl.pos[1]+1].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
            if pl.pos[1]-1 >= 0 and Map.matriz[pl.pos[0]][pl.pos[1]-1] == 0: 
                Map.b[pl.pos[0]][pl.pos[1]-1].config(image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss])
                Map.b[pl.pos[0]][pl.pos[1]-1].image = ClasseImagens.rangedTiles[ClasseTrack.Tracker.Boss]
                
            for i in range(2, 8):
                if pl.pos[0]+i < 15 and pl.pos[1] and Map.matriz[pl.pos[0]+i][pl.pos[1]] == 0:
                    Map.b[pl.pos[0]+i][pl.pos[1]].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                    Map.b[pl.pos[0]+i][pl.pos[1]].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
                if pl.pos[0]-i >= 0 and Map.matriz[pl.pos[0]-i][pl.pos[1]] == 0:
                    Map.b[pl.pos[0]-i][pl.pos[1]].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                    Map.b[pl.pos[0]-i][pl.pos[1]].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
                if pl.pos[1]+i < 27 and Map.matriz[pl.pos[0]][pl.pos[1]+i] == 0:
                    Map.b[pl.pos[0]][pl.pos[1]+i].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                    Map.b[pl.pos[0]][pl.pos[1]+i].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
                if pl.pos[1]-i >= 0 and Map.matriz[pl.pos[0]][pl.pos[1]-i] == 0: 
                    Map.b[pl.pos[0]][pl.pos[1]-i].config(image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss])
                    Map.b[pl.pos[0]][pl.pos[1]-i].image = ClasseImagens.subrangedTiles[ClasseTrack.Tracker.Boss]
        
    def Exit():
        sound.Stop_All()
        window.destroy()