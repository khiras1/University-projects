from tkinter import *
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root=Tk()
root.config(bg='#9370DB')
root.title("WYKRESY")
root.geometry('400x450')
root.resizable(0,0)

expression=""

def press(item):
    """Funkcja zamienia zmienną na string po kliknięciu """
    global expression
    expression= expression + str(item)
    equation.set(expression)

equation=StringVar()
legend_value = IntVar()


mainlabel = Label(root, text='Równanie:', bg = "#66CDAA").grid(row=3, column=0)
expression_field = Entry(root, textvariable=equation, state="disabled").grid(column=3, row=3)
x_min_label=Label(root, text='x_min:', bg = "#66CDAA").grid(column=1,row=17)
x_min_val=Entry(root,width=13)
x_min_val.grid(column=2, row=17, sticky=W, columnspan=2)
x_max_label=Label(root, text='x_max', bg = "#66CDAA").grid(column=1, row=18)
x_max_val=Entry(root, width=13)
x_max_val.grid(column=2,row=18, sticky=W, columnspan=2)
y_min_label=Label(root, text='y_min:', bg = "#66CDAA").grid(column=1, row=19)
y_min_val=Entry(root, width=13)
y_min_val.grid(column=2, row=19, sticky=W, columnspan=2)
y_max_label=Label(root, text='y_max:', bg = "#66CDAA").grid(column=1, row=20)
y_max_val=Entry(root, width=13)
y_max_val.grid(column=2, row=20, sticky=W, columnspan=2)

y_title=Label(root, text='y_title:', bg = "#66CDAA").grid(column=1, row=21)
y_title_val=Entry(root, width=13)
y_title_val.grid(column=2, row=21)

x_title=Label(root, text='x_title:', bg = "#66CDAA").grid(column=1, row=22)
x_title_val=Entry(root, width=13)
x_title_val.grid(column=2, row=22)

xy_title=Label(root, text='Title:', bg = "#66CDAA").grid(column=1, row=23)
xy_title_val=Entry(root, width=13)
xy_title_val.grid(column=2, row=23)

plot=Button(root, text='Wykres', command=lambda: [plotting()], bg="#9c3a28").grid(row=15, column=3)
clear_button = Button(root, text='Wyczyść', command=lambda: clear(), bg="#9c3a28").grid(row=15, column=2)
legend_button = Checkbutton(root, text='Legenda', variable=legend_value, onvalue=1, offvalue=0, bg = "#66CDAA").grid(column=3, row=22, columnspan=2)

dodawanie=Button(root, text='+', height=1, width=7, command=lambda:press('+'), bg = "#66CDAA").grid(row=6, column=2)
odejmowanie=Button(root, text='-', height=1, width=7, command=lambda:press('-'), bg = "#66CDAA").grid(row=6, column=3)
mnozenie=Button(root, text='*', height=1, width=7, command=lambda:press('*'), bg = "#66CDAA").grid(row=6, column=4)
dzielenie=Button(root, text='/', height=1, width=7, command=lambda:press('/'), bg = "#66CDAA").grid(row=7, column=2)
sinus=Button(root, text='sin', height=1, width=7, command=lambda:press('sin'), bg = "#66CDAA").grid(row=8, column=4)
cosinus=Button(root, text='cos', height=1, width=7, command=lambda:press('cos'), bg = "#66CDAA").grid(row=9, column=2)
logartym=Button(root, text='ln', height=1, width=7, command=lambda:press('ln'), bg = "#66CDAA").grid(row=8, column=2)
exponenta=Button(root, text='e', height=1, width=7, command=lambda:press('e'), bg = "#66CDAA").grid(row=8, column=3)
nawias_lewy=Button(root, text='(', height=1, width=7, command=lambda:press('('), bg = "#66CDAA").grid(row=7, column=3)
nawias_prawy=Button(root, text=')', height=1, width=7, command=lambda:press(')'), bg = "#66CDAA").grid(row=7, column=4)
iks=Button(root, text='x', height=1, width=7, command=lambda:press('x'), bg = "#66CDAA").grid(row=9, column=3)
do_potegi=Button(root, text='^', height=1, width=7, command=lambda:press('^'), bg = "#66CDAA").grid(row=9, column=4)
do_potegi=Button(root, text='\u03C0', height=1, width=7, command=lambda:press('\u03C0'), bg = "#66CDAA").grid(row=10, column=2)

zero=Button(root, text='0', height=1, width=7, command=lambda:press('0'), bg = "#0e6e4d").grid(row=11, column=2)
jeden=Button(root, text='1', height=1, width=7, command=lambda:press('1'), bg = "#0e6e4d").grid(row=11, column=3)
dwa=Button(root, text='2', height=1, width=7, command=lambda:press('2'), bg = "#0e6e4d").grid(row=11, column=4)
trzy=Button(root, text='3', height=1, width=7, command=lambda:press('3'), bg = "#0e6e4d").grid(row=12, column=2)
cztery=Button(root, text='4', height=1, width=7, command=lambda:press('4'), bg = "#0e6e4d").grid(row=12, column=3)
piec=Button(root, text='5', height=1, width=7, command=lambda:press('5'), bg = "#0e6e4d").grid(row=12, column=4)
szesc=Button(root, text='6', height=1, width=7, command=lambda:press('6'), bg = "#0e6e4d").grid(row=13, column=2)
siedem=Button(root, text='7', height=1, width=7, command=lambda:press('7'), bg = "#0e6e4d").grid(row=13, column=3)
osiem=Button(root, text='8', height=1, width=7, command=lambda:press('8'), bg = "#0e6e4d").grid(row=13, column=4)
dziewiec=Button(root, text='9', height=1, width=7, command=lambda:press('9'), bg = "#0e6e4d").grid(row=14, column=2)
srednik=Button(root, text=';', height=1, width=7, command=lambda:press(';'), bg="#9c3a28").grid(row=14, column=3)


symbols_math = {'\u03C0': 'np.pi', 'e': 'np.e', 'ln' : 'np.log', '^' : '**', 'sin' : 'np.sin', 'cos' : 'np.cos', 'ctg' : '1/np.tan', 'tg' : 'np.tan'}



def clear():
    """Funkcja czyści okna Entry"""
    global expression
    expression=""
    equation.set("")
    x_min_val.delete(0, END)
    x_max_val.delete(0, END)
    y_min_val.delete(0, END)
    y_max_val.delete(0, END)
    x_title_val.delete(0,END)
    y_title_val.delete(0,END)
    xy_title_val.delete(0,END)

def plotting():
    """Funkcja próbuje utworzyć wykres, zamienia (ze słownika) klucze wpisane do EntryBox na przypisane im wartości, dzieli je względem średnika (jeśli występuje),
    ustawia zakres funkcji podany przez użytkownika, a następnie tworzy wykres, jeśli nie zadziała pokazuje okno BŁĄD"""
    try:
        global expression
        for key, value in symbols_math.items():
                expression = expression.replace(key, value)
        functions = expression.split(';')
        xmin = int(x_min_val.get())
        xmax = int(x_max_val.get())
        ymin = int(y_min_val.get())
        ymax = int(y_max_val.get())
        plot_frame = Toplevel(root)
        figure1 = plt.figure(figsize=(5,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        plt.xlabel(x_title_val.get())
        plt.ylabel(y_title_val.get())
        plt.title(xy_title_val.get())
        plt.axis([xmin,xmax,ymin,ymax])
        canvas = FigureCanvasTkAgg(figure1, plot_frame)
        canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
        for function in functions:
            xs = np.linspace(xmin, xmax, (xmax-xmin)*10)
            ys = [eval(function) for x in xs]
            ax1.plot(xs,ys, label=f'{function}')
        if legend_value.get() == 1:
            plt.legend()
    except:
        messagebox.showwarning("BŁĄD","TAK NIE MOŻNA")  

root.mainloop()