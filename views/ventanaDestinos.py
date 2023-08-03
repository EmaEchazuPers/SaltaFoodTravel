import tkinter as tk
from tkinter.font import Font
import tkintermapview as tkMapa

class VentanaDestinos(tk.Frame):
    def __init__(self, master=None, controlador=None, cont_ubicaciones=None):

        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.cont_ubicaciones = cont_ubicaciones

        #Define titulo de ventana destinos

        lugares_font = Font(size=13)

        self.lugares = tk.Label(self, text='Lista de lugares para visitar', font=lugares_font)
        self.lugares.grid(row=0,column=0, columnspan=9,pady=5)        

        #Define botones

        self.boton_volver = tk.Button( self, text='Volver',command=self.controlador.volver_inicio)
        self.boton_volver.grid(row=1, column=0, rowspan=1, padx=5)
        
        #Define lista de lugares

        lugares_font = Font(size=15)        

        self.lista_lugares = tk.Listbox(self)
        self.lista_lugares.config(width=30,justify='center')
        self.lista_lugares.grid(row=1, column=2, columnspan=2, rowspan=3,padx=5) 

        #Define mapa

        self.mapa = tkMapa.TkinterMapView(self, width=200, height=200, corner_radius=0)
        self.mapa.set_position(-24.789695,-65.411059)
        self.mapa.set_zoom(13)
        self.mapa.grid(row=1, column=5, columnspan=3, rowspan=3,padx=5)   
        mis_coordenadas = self.colocarUbicaciones()
        for mar in mis_coordenadas:
            self.mapa.set_marker(mar[0],mar[1],text='')

        self.actualizar_lista()

    
    def actualizar_lista(self):
        destinos = self.controlador.getDestinos()
        self.lista_lugares.delete(0, tk.END)
        for destino in destinos:
            self.lista_lugares.insert(tk.END, destino.nombre)
    
    def colocarUbicaciones(self):
        ubicaciones = self.cont_ubicaciones.getUbicaciones()
        coordenadas = []
        for ubi in ubicaciones:
            coordenadas.append(ubi.coordenadas)
        return coordenadas
