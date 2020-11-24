from tkinter import *
from tkinter import ttk

import calculator

def imprimeuno():
    print(1)


class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")


        self.display = calculator.Display(self)
        self.display.pack(side=TOP, fill=BOTH, expand=True)

        self.teclado = calculator.Keyboard_con_diccionario(self)
        self.teclado.pack(side=TOP)


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()