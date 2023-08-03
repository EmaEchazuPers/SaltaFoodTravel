import tkinter as tk
from tkinter.font import Font
import tkintermapview as tkMapa

class VentanaActividades(tk.Frame):
    def __init__(self, master=None, controlador=None, controlador_Act=None):

        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.controlador_Act = controlador_Act
        self.item_seleccionado = 0
        self.destino_elegido = 0

        #Define el titulo
        titulo_font = Font(size=13)

        self.titulo = tk.Label(self, text='Actividades realizadas en los destinos', font=titulo_font)
        self.titulo.grid(row=0,columnspan=3, pady=10, sticky='n')

        descripcion_font = Font(size=10)

        #Define lista de lugares    

        self.lista_lugares = tk.Listbox(self)
        self.lista_lugares.config(width=30, justify='center')
        self.lista_lugares.grid(row=1, column=0, columnspan=2, rowspan=3,padx=5)
        
        #Define lista de actividades

        self.lista_actividades = tk.Listbox(self)
        self.lista_actividades.config(width=30, justify='center')
        #self.lista_actividades.bind('<<ListboxSelect>>',seleccionar)
        self.lista_actividades.grid(row=1, column=1, columnspan=2, rowspan=3,padx=5)

        #Botones

        self.boton_volver = tk.Button( self, text='Volver',command=self.controlador.volver_inicio)
        self.boton_volver.grid(row=2,column=0,pady=10)

        self.boton_seleccionar = tk.Button( self, text='Seleccionar',command=self.item_seleccionado)
        self.boton_seleccionar.grid(row=2,column=0,pady=10)

        self.actualizar_lista()
        self.destino_elegido = self.actualizar_actividades(self.item_seleccionado)

    def actualizar_lista(self):
        destinos = self.controlador.getDestinos()
        self.lista_lugares.delete(0, tk.END)
        for destino in destinos:
            self.lista_lugares.insert(tk.END, destino.nombre)
    
    def item_seleccionado():
        for item in self.lista_lugares.curselection():
            self.item_seleccionado = self.lista_lugares.get(item)
    
    def actualizar_actividades(self, item):
        destinos = self.controlador.getDestinos()
        destino_elegido = 0
        for destino in destinos:
            if destino.nombre == item:
                destino_elegido = destino.id_destino
        return destino_elegido



    