import firecall
from tkinter import *
from tkinter import messagebox
import ClasseMapa



my_firebase = firecall.Firebase("https://resplendent-inferno-7886.firebaseio.com/")

def SubmmitScore (nome,pontuação, turnos):
    
    dicio = {'Info': [pontuação , turnos]}
    a = True
    records = eval(my_firebase.get_sync(point="/records"))
    
    lista = []
    for i in records:
        lista.append(i)
    if "{0}".format(nome) in lista:
        a = False
    if a == True:
        my_firebase.put_sync(point="/records/{0}".format(nome) , data = dicio)
        ConstruirRank(nome,pontuação,turnos)
    if a == False:
        messagebox.showinfo("Attention", "This name already exists!")
        
def ConstruirRank (nome,pontuação,turnos):
    records = eval(my_firebase.get_sync(point="/records"))   
    ranquear = []
    for i in records:
        ranquear.append((i,records[i]['Info'][0],records[i]['Info'][1]))
    print(ranquear)
    wmax = 0
    tmax = 1000000000000000000000000000000000000000
    primeiro = ("hugo",1,0)
    
    for i in range(len(ranquear)):
        if ranquear[i][1] > wmax:
            wmax = ranquear[i][1]
            tmax=  ranquear[i][2]
            primeiro = (ranquear[i][0],ranquear[i][1],ranquear[i][2])
        if ranquear[i][1] == wmax and ranquear[i][2] < tmax :
            wmax = ranquear[i][1]
            tmax=  ranquear[i][2]
            primeiro = (ranquear[i][0],ranquear[i][1],ranquear[i][2])
            
    mostrardados = Tk()
    mostrardados.config(bg="black")
    mostrardados.title("Magic Trap Scores")
    recordemundial = Label(mostrardados)
    recordemundial.config(text=" Recorde mundial : {0} : {1} waves : {2} turns".format(primeiro[0],primeiro[1],primeiro[2]) ,font = ("Impact",20),bg="black",foreground="red")
    recordemundial.grid(row=0,column =0)
    seuscore= Label(mostrardados)
    seuscore.config(text= "Seu Score : {0} : {1} waves : {2} turns".format(nome,pontuação,turnos),font = ("Impact",20),bg="black",foreground="red")
    seuscore.grid(row=1,column=0)
    ClasseMapa.updategui.submmit.destroy()
    ClasseMapa.updategui.submmitscore.destroy()
    
    mostrardados.mainloop()
    
def Ranquear(ranquear): 
    wmax = 0
    tmax = 1000000000000000000000000000000000000000 
    a = len(ranquear)
    primeiro = ("Hugo",1,900)
    for i in range(0,a):
        if ranquear[i][1] > wmax:
            wmax = ranquear[i][1]
            tmax=  ranquear[i][2]
            primeiro = (ranquear[i][0],ranquear[i][1],ranquear[i][2])                        
        if ranquear[i][1] == wmax and ranquear[i][2] < tmax :
            wmax = ranquear[i][1]
            tmax=  ranquear[i][2]
            primeiro = (ranquear[i][0],ranquear[i][1],ranquear[i][2])
                       
    return primeiro
    
    
def Construir_Rank_Menu():
    records = eval(my_firebase.get_sync(point="/records"))  
    ranquear = []
    for i in records:
        ranquear.append((i,records[i]['Info'][0],records[i]['Info'][1]))    
    primeiro = Ranquear(ranquear)
    ranquear.remove(primeiro)
    segundo= Ranquear(ranquear)
    ranquear.remove(segundo)
    terceiro = Ranquear(ranquear)
    ranquear.remove(terceiro)
    quarto= Ranquear(ranquear)
    ranquear.remove(quarto)
    quinto = Ranquear(ranquear)
    Ranking = Tk()
    l1 = Label(Ranking)
    l1.config(text=" 1º Place : {0} : {1} waves : {2} turns".format(primeiro[0],primeiro[1],primeiro[2]) ,font = ("Impact",20),bg="black",foreground="red")
    l1.grid(row=0,column =0)
    l2 = Label(Ranking)
    l2.config(text=" 2º Place : {0} : {1} waves : {2} turns".format(segundo[0],segundo[1],segundo[2]) ,font = ("Impact",20),bg="black",foreground="red")
    l2.grid(row=1,column =0)
    l3 = Label(Ranking)
    l3.config(text=" 3º Place : {0} : {1} waves : {2} turns".format(terceiro[0],terceiro[1],terceiro[2]) ,font = ("Impact",20),bg="black",foreground="red")
    l3.grid(row=2,column =0)
    l4 = Label(Ranking)
    l4.config(text=" 4º Place : {0} : {1} waves : {2} turns".format(quarto[0],quarto[1],quarto[2]) ,font = ("Impact",20),bg="black",foreground="red")
    l4.grid(row=3,column =0)
    l5 = Label(Ranking)
    l5.config(text=" 5º Place : {0} : {1} waves : {2} turns".format(quinto[0],quinto[1],quinto[2]) ,font = ("Impact",20),bg="black",foreground="red")
    l5.grid(row=4,column =0)
    Ranking.config(bg="black")
    Ranking.mainloop()
    
    
         
    
    
    
    
    
