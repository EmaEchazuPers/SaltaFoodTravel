import tkinter as tk
import views.ventanaInicio as VentanaInicio
import models.DestinoCulinario as Mod_Destino
import controllers.controladorDestinos as Cont_Destino


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('SALTA FOOD TRAVEL')
        self.geometry('700x500')
        self.resizable(False,False)
        self.iniciar()
        self.cambiar_frame(self.ventana_inicio)
    

    def iniciar(self):

        destino = Mod_Destino.Destino.carga_json('data\destinos.json')

        controlador_destino = Cont_Destino.ControladorDestinos(self, destino)

        self.ventana_inicio = VentanaInicio.VentanaInicio(self,controlador_destino)

        self.ajustar_frame(self.ventana_inicio)
    
    def ajustar_frame(self, frame_ajuste):
        frame_ajuste.grid(row=0,column=0,sticky='nsew')
    
    def cambiar_frame(self, frame_nuevo):
        frame_nuevo.tkraise()


if __name__ == '__main__':
    app = Aplicacion()
    app.mainloop()