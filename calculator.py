from tkinter import *
from tkinter import ttk
from ast import literal_eval

WIDTH = 68
HEIGHT = 50

dbotones = [
    {
        'text': 'C',
        'r': 0,
        'c': 1,
    },
    {
        'text': '+/-',
        'r': 0,
        'c': 2,
    },
    {
        'text': '÷',
        'r': 0,
        'c': 3,
    },
    {
        'text': '7',
        'r': 1,
        'c': 0,
    },
    {
        'text': '8',
        'r': 1,
        'c': 1,
    },
    {
        'text': '9',
        'r': 1,
        'c': 2,
    },
    {
        'text': 'x',
        'r': 1,
        'c': 3,
    },
    {
        'text': '4',
        'r': 2,
        'c': 0,
    },
    {
        'text': '5',
        'r': 2,
        'c': 1,
    },
    {
        'text': '6',
        'r': 2,
        'c': 2,
    },
    {
        'text': '-',
        'r': 2,
        'c': 3,
    },
    {
        'text': '1',
        'r': 3,
        'c': 0,
    },
    {
        'text': '2',
        'r': 3,
        'c': 1,
    },
    {
        'text': '3',
        'r': 3,
        'c': 2,
    },
    {
        'text': '+',
        'r': 3,
        'c': 3,
    },
    {
        'text':'0',
        'r':4,
        'c':0,
        'w': 2
    },
    {
        'text': '.',
        'r': 4,
        'c': 2,
    },
    {
        'text': '=',
        'r': 4,
        'c': 3,
    },
]

def retornaCaracter(tecla):
    prfloat('han pulsado', tecla)

class Display(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT)
        self.pack_propagate(0)

        self.label = ttk.Label(self, text="0", anchor=E, background='black', foreground='white', font='Helvetica 36')
        self.label.pack(side=TOP, fill=BOTH, expand=True)

    def refresh(self, texto):
        if not isinstance(texto, str):
            texto = literal_eval(str(texto))

        self.label.config(text=texto)

class CalcButton(ttk.Frame):
    def __init__(self, parent, text, command=None, width=1, height=1):
        ttk.Frame.__init__(self, parent, width=WIDTH*width, height=HEIGHT*height)
        self.pack_propagate(0)
        self.value = text
        self.command = command

        ttk.Button(self, text=text, command=self.send).pack(side=TOP, fill=BOTH, expand=True)

        #ttk.Button(self, text=text, command=lambda : command(text)).pack(side=TOP, fill=BOTH, expand=True)

    def send(self):
        self.command(self.value)


class Keyboard(ttk.Frame):
    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)

        for boton in dbotones:
            w = boton.get('w', 1)
            h = boton.get('h', 1)

            btn = CalcButton(self, boton['text'],width=w, height=h, command=command)
            btn.grid(row=boton['r'], column=boton['c'], columnspan=w, rowspan=h)

class Calculator(ttk.Frame):
    valor1 = None
    valor2 = None
    r = None
    operador = ''
    cadena = ''

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*6)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        self.display = Display(self)
        self.display.pack(side=TOP, fill=BOTH, expand=True)

        self.teclado = Keyboard(self, self.gestiona_calculos)
        self.teclado.pack(side=TOP)

    def formatNumber(self, numero):
        if numero == int(numero):
            return int(numero)
        else:
            return numero

    def gestiona_calculos(self, tecla):

        if tecla.isdigit():
            if not (self.cadena == '' and tecla == '0'):
                self.cadena += tecla
                self.display.refresh(self.cadena)
        elif tecla == '.' and '.' not in self.cadena:
            if self.cadena != '':
                self.cadena += tecla
            else:
                self.cadena = self.cadena + '0' + tecla
            #self.cadena += tecla if cadena != '' else ('0' + tecla)

            self.display.refresh(self.cadena)
        elif tecla in tuple('+-x÷'):
            if self.valor1 == None:
                self.operador = tecla
                self.valor1 = float(self.cadena)
                self.cadena = ''
            else:
                if not self.cadena: 
                    self.operador = tecla
                    return
                self.valor2 = float(self.cadena)
                self.r = self.calculate()
                self.operador = tecla
                self.display.refresh(self.r)
                self.valor1 = self.r

            self.cadena = ''
        elif tecla == '=':
            if not self.cadena: 
                return
            self.valor2 = float(self.cadena)
            self.r = self.calculate()
            self.display.refresh(self.r)
            self.operador = ''
            self.valor1 = self.r
            self.cadena = ''
        elif tecla == 'C':
            self.valor1 = None
            self.valor2 = None
            self.r = None
            self.operador = ''
            self.cadena = ''
            self.display.refresh('0')

    def calculate(self):
        '''
        self.valor1 = 12
        self.valor2 = 32
        self.operador = '+' podría haber - ÷ x
        '''
        if self.operador == '+':
            return self.valor1 + self.valor2
        elif self.operador == '-':
            return self.valor1 - self.valor2
        elif self.operador == 'x':
            return self.valor1 * self.valor2
        elif self.operador == '÷':
            return self.valor1 / self.valor2
        else:
            print("error en operador")
            return 'E'