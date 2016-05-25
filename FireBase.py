import firecall
from tkinter import *
from tkinter import messagebox




my_firebase = firecall.Firebase("https://resplendent-inferno-7886.firebaseio.com/")

def SubmmitScore (nome,pontuação, turnos):
    dicio = {"Info": [pontuação , turnos]}
    a = True
    records = eval(my_firebase.get_sync(point="/records"))
    
    lista = []
    for i in records:
        lista.append(i)
        print(lista)
    if "laranja" in lista:
        a = False
    if a == True:
        my_firebase.put_sync(point="/records/laranja" , data = dicio)
        ConstruirRank(nome,pontuação,turnos)
    if a == False:
        messagebox.showinfo("Attention", "This name already exists!")
        
def ConstruirRank (nome,pontuação,turnos):
    records = eval(my_firebase.get_sync(point="/records"))
    ranquear = []
    for i in records:
        ranquear.append((i,records[i]['Info'][0],records[i]['Info'][1]))
    wmax = 0
    tmax = 0
    primeiro = ("hugo",1,0)
    for i in range(len(ranquear)):
        if ranquear[i][1] >= wmax and ranquear[i][2] > tmax :
            wmax = ranquear[i][1]
            tmax=  ranquear[i][1]
            primeiro = (ranquear[i][0],ranquear[i][1],ranquear[i][2])
    print(primeiro)
    
    
    
    
          
   
            
            
    
            
            

        

#a = my_firebase.get_sync(point="/records/{0}".format(dicio["Nome"]), data = dicio)

