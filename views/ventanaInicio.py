import tkinter as tk
from tkinter.font import Font
import tkintermapview as tkMapa

class VentanaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)
        self.master = master
        self.controlador = controlador

        #Define el titulo
        titulo_font = Font(size=20, weight='bold')

        self.titulo = tk.Label(self, text='Bienvenido a SALTA FOOD TRAVEL', font=titulo_font)
        self.titulo.grid(row=0,columnspan=3, pady=10, sticky='n')
        

        descripcion_font = Font(size=10)

        self.descripcion = tk.Label(self,text='Una aplicación diseñana para facilitar la exploración de destinos culinarios.'
        , font=descripcion_font, wraplength=300)
        self.descripcion.grid(row=1, columnspan=3, pady=50, sticky='n')
        

        #Botones

        self.boton_destinos = tk.Button(self, text='Ir a destinos',command=self.controlador.verDestinos)
        self.boton_destinos.grid(row=2,column=0,pady=10)
        
        self.boton_busqueda = tk.Button(self, text='Ver reviews',command=self.controlador.verReviews)
        self.boton_busqueda.grid(row=2,column=1,pady=10)
        
        self.boton_actividades = tk.Button(self, text='Ver actividades', command=self.controlador.verActividades)
        self.boton_actividades.grid(row=2,column=2,pady=10)

