class ControladorInicio:
    def __init__(self,app):
        self.app = app
        
    def verDestinos(self):
        self.app.cambiar_frame(self.app.ventana_destinos)