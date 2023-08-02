class Ubicacion:
    def __init__(self,id_ubicacion, direccion):
        self.id_ubicacion = id_ubicacion
        self.direccion = str(direccion)
        self.coordenadas=[]
    
    def set_direccion(self,direccion):
        self.direccion = str(direccion)
    
    def set_coordenadas(self,coordenadas):
        self.coordenadas = coordenadas