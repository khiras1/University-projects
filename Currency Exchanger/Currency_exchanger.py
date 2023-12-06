from tkinter import *
import tkinter
from urllib.request import urlopen
import json
import pickle
from click import clear
import requests
from tkinter import ttk
from tkinter import messagebox

def connected_to_internet(url='http://api.nbp.pl', timeout=5): #sprawdzanie dostepu do internetu
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


def bank():
    url=f'http://api.nbp.pl/api/exchangerates/tables/A/?format=json' #pobieranie informacji ze strony w json 
    web=urlopen(url)
    data=(json.loads(web.read())[0])['rates']
    dict_1=dict() #dodajemy PLN bo nie ma
    dict_1['PLN']=1
    for i in range(len(data)): #do nowego slownika dopisujemy kursy nazwa kursy wartosc
        dict_1[(data[i]['code'])]=float(data[i]['mid'])
    return dict_1

def converter(input, output, value, dict):
    to_PLN=value*dict[input] #pprzeliczanie poczatkowej waluty na zlotowki
    return round(to_PLN/dict[output],2) #zlotowki na docelowa walute

def file_importing(): #importowanie z pliku waluty.pkl
    file=open('waluty.pkl', 'rb')
    dict_1=pickle.load(file)
    file.close()
    return dict_1

def saving(dict): #zapisywanie waluty.pkl
    file=open('waluty.pkl', 'wb')
    pickle.dump(dict,file)
    file.close()

def main_function(): #glowna funkcja konwertujaca waluty
    try:
        new_value=value.get()
        convert01=converter(str(in_value.get()), str(out_value.get()), float(new_value), dictionary)
        value1.delete(0,tkinter.END)
        value1.insert(0, str(convert01))
    except:
        messagebox.showerror('BŁĄD', 'NIE WPISUJ WIĘCEJ NIŻ JEDNĄ KROPKĘ ANI LITER')
    
def clear01(): #czyszczenie okienek
    value.delete(0,tkinter.END)
    value1.delete(0,tkinter.END)
    
if connected_to_internet() == True: #sprawdzanie czy jest internet
    dictionary = bank()
    saving(dictionary)
else:
    dictionary = file_importing()

options_list = dictionary.keys()

root=Tk()
root.title("Currency Converter")
root.geometry('500x125')
root.resizable(0,0) # usuwa przyciski zmieniania wielkosci 
root.config(bg='#9370DB')
root.resizable(width=False, height=False)
Label(root, text='Początkowa waluta:',bg = "#66CDAA").grid(row=0,column=0,sticky=W)
Label(root, text='Ile:',bg = "#66CDAA").grid(row=0,column=1,sticky=W)
Label(root, text='Końcowa waluta: ',bg = "#66CDAA").grid(row=0,column=2,sticky=W)
Label(root, text='Po policzeniu:',bg = "#66CDAA").grid(row=0,column=3,sticky=W)
in_value = 1
in_value = StringVar(root)
out_value = 1
out_value = StringVar(root)
options_list = dictionary.keys()

in_value=tkinter.StringVar(root)
in_value.set("PLN")
w = ttk.Combobox(root, textvariable=in_value, values=list(options_list))
w.grid(row=1,column=0,sticky=W)
out_value=tkinter.StringVar(root)
out_value.set("PLN")
w2 = ttk.Combobox(root, textvariable=out_value, values=list(options_list))
w2.grid(row=1,column=2,sticky=W)


value=tkinter.Entry(root)
value.grid(row=1,column=1,sticky=W)

value1=tkinter.Entry(root)
value1.grid(row=1,column=3,sticky=W)


button=tkinter.Button(root, text="Policz",bg = "#66CDAA", command=main_function)
button.grid(row=2,column=2,sticky=W)
exit_button=Button(root, text="Koniec",bg = "#66CDAA", command=root.destroy)
exit_button.grid(row=2,column=3,sticky=W)
clear_button=Button(root, text="Czyść",bg = "#66CDAA", command=clear01)
clear_button.grid(row=6,column=2,sticky=W)
root.mainloop()