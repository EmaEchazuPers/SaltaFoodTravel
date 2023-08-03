class ControladorDestinos:
    def __init__(self,app,DestinoCulinario):
        self.app = app
        self.DestinoCulinario = DestinoCulinario

    def getDestinos(self):
        return self.DestinoCulinario