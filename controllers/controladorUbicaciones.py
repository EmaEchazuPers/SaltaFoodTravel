class ControladorUbicaciones:
    def __init__(self,app,Ubicaciones):
        self.app = app
        self.Ubicaciones = Ubicaciones

    def getUbicaciones(self):
        return self.Ubicaciones