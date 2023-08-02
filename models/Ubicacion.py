import json

class Ubicacion:
    def __init__(self,id_ubicacion, direccion):
        self.id_ubicacion = id_ubicacion
        self.direccion = str(direccion)
        self.coordenadas=[]

    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**ubicacion) for ubicacion in data]

    """
    def set_direccion(self,direccion):
        self.direccion = str(direccion)
    
    def set_coordenadas(self,coordenadas):
        self.coordenadas = coordenadas
    """