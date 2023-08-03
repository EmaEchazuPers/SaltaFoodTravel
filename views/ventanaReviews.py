import tkinter as tk
from tkinter.font import Font
import tkintermapview as tkMapa

class VentanaReviews(tk.Frame):
    def __init__(self, master=None, controlador=None, controlador_Rev=None):

        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.controlador_Rev = controlador_Rev
        self.item_seleccionado = 0
        self.destino_elegido = 0

        #Define el titulo
        titulo_font = Font(size=13)

        self.titulo = tk.Label(self, text='Reviews de los usuarios', font=titulo_font)
        self.titulo.grid(row=0,columnspan=8, pady=10, sticky='nsew')

        #Botones

        self.boton_volver = tk.Button( self, text='Volver',command=self.controlador.volver_inicio)
        self.boton_volver.grid(row=1,column=0,pady=10)


        #Define lista de reviews 

        self.lista_reviews = tk.Listbox(self)
        self.lista_reviews.config(width=70, justify='center')
        self.lista_reviews.grid(row=1, column=2, columnspan=15, rowspan=3,padx=5)
        
        self.actualizar_lista()
        

    def actualizar_lista(self):
        reviews = self.controlador_Rev.getReviews()
        destinos = self.controlador.getDestinos()
        self.lista_reviews.delete(0, tk.END)
        for destino in destinos:
            for review in reviews:
                if destino.id_destino == review.id_destino:
                    self.lista_reviews.insert(tk.END, destino.nombre + ': ' + review.comentario + '\n')
