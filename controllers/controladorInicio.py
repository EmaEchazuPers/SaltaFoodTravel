class ControladorInicio:
    def __init__(self,app):
        self.app = app
        
    def verDestinos(self):
        self.app.cambiar_frame(self.app.ventana_destinos)
    
    def verActividades(self):
        self.app.cambiar_frame(self.app.ventana_actividades)
    
    def verReviews(self):
        self.app.cambiar_frame(self.app.ventana_reviews)