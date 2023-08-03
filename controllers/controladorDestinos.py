class ControladorDestinos:
    def __init__(self,app,destinoCulinario):
        self.app = app
        self.destinoCulinario = destinoCulinario

    def getDestinos(self):
        return self.destinoCulinario
    
    def volver_inicio(self):
        self.app.cambiar_frame(self.app.ventana_inicio)
    