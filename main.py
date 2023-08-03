import tkinter as tk
import views.ventanaInicio as VentanaInicio
import views.ventanaDestinos as VentanaDestinos
import views.ventanaActividades as VentanaActividades
import views.ventanaReviews as VentanaReviews
import models.DestinoCulinario as Mod_Destino
import models.Ubicacion as Mod_Ubicacion
import models.Actividad as Mod_Actividad
import models.Review as Mod_Review
import controllers.controladorDestinos as Cont_Destino
import controllers.controladorInicio as Cont_Inicio
import controllers.controladorUbicaciones as Cont_Ubicacion
import controllers.controladorActividades as Cont_Actividades
import controllers.controladorReviews as Cont_Review


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('SALTA FOOD TRAVEL')
        self.geometry('500x400')
        self.resizable(False,False)
        self.iniciar()
        self.cambiar_frame(self.ventana_inicio)
    

    def iniciar(self):

        destino = Mod_Destino.Destino.carga_json("data\destinos.json")
        ubicaciones = Mod_Ubicacion.Ubicacion.carga_json("data\\ubicaciones.json")
        actividades = Mod_Actividad.Actividad.carga_json("data\\actividades.json")
        reviews = Mod_Review.Review.carga_json("data\\reviews.json")

        controlador_inicio = Cont_Inicio.ControladorInicio(self)
        controlador_destino = Cont_Destino.ControladorDestinos(self, destino)
        controlador_ubicaciones = Cont_Ubicacion.ControladorUbicaciones(self,ubicaciones)
        controlador_actividades = Cont_Actividades.ControladorActividades(self,actividades)
        controlador_reviews = Cont_Review.ControladorReviews(self,reviews)

        self.ventana_inicio = VentanaInicio.VentanaInicio(self,controlador_inicio)
        self.ventana_inicio.configure(background='#EEEEEE')
        self.ventana_destinos = VentanaDestinos.VentanaDestinos(self,controlador_destino,controlador_ubicaciones)
        self.ventana_destinos.configure(background='#EEEEEE')
        self.ventana_actividades = VentanaActividades.VentanaActividades(self,controlador_destino,controlador_actividades)
        self.ventana_actividades.configure(background='#EEEEEE')
        self.ventana_reviews = VentanaReviews.VentanaReviews(self,controlador_destino,controlador_reviews)
        self.ventana_reviews.configure(background='#EEEEEE')

        self.ajustar_frame(self.ventana_inicio)
        self.ajustar_frame(self.ventana_destinos)
        self.ajustar_frame(self.ventana_actividades)
        self.ajustar_frame(self.ventana_reviews)
    
    def ajustar_frame(self, frame_ajuste):
        frame_ajuste.grid(row=0,column=0,sticky='nsew')
        
    
    def cambiar_frame(self, frame_nuevo):
        frame_nuevo.tkraise()


if __name__ == '__main__':
    app = Aplicacion()
    app.mainloop()