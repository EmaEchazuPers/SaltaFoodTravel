import tkinter as tk
from tkinter.font import Font

class VentanaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)
        self.master = master
        self.controlador = controlador

        #Define el titulo
        titulo_font = Font(size=20, weight='bold')

        self.titulo = tk.Label(self, text='Bienvenido a SALTA FOOD TRAVEL', font=titulo_font)
        self.titulo.grid(row=0,column=0,pady=5)

        #Define lista de lugares

        lugares_font = Font(size=10)

        self.lugares = tk.Label(self, text='LUGARES PARA VISITAR', font=lugares_font,wraplength=150)
        self.lugares.grid(row=1,column=0, pady=8)

        self.lista_lugares = tk.Listbox(self)
        self.lista_lugares.config(width=50)
        #self.lista_lugares.pack()
        self.lista_lugares.grid(row=2,column=0)
        self.actualizar_lista()

        #Define botones

        self.boton_buscar = tk.Button( self, text='Buscar')
        self.boton_buscar.grid(row=1,column=1,pady=6,padx=10)
    
    def actualizar_lista(self):
        destinos = self.controlador.getDestinos()
        self.lista_lugares.delete(0, tk.END)
        for destino in destinos:
            self.lista_lugares.insert(tk.END, destino.nombre)
