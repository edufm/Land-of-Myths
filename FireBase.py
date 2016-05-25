import firecall
from tkinter import *
from tkinter import messagebox




my_firebase = firecall.Firebase("https://resplendent-inferno-7886.firebaseio.com/")

def SubmmitScore (nome,pontuação, turnos):
    dicio = {"Info": [pontuação , turnos]}
    a = True
    records = eval(my_firebase.get_sync(point="/records"))
    print(records)
    lista = []
    for i in records:
        lista.append(i)
        print(lista)
    if "laranja" in lista:
        a = False
    if a == True:
        my_firebase.put_sync(point="/records/laranja" , data = dicio)
    if a == False:
        messagebox.showinfo("Attention", "This name already exists!")
        
        
        
print(eval(my_firebase.get_sync(point="/records")))
#a = my_firebase.get_sync(point="/records/{0}".format(dicio["Nome"]), data = dicio)

