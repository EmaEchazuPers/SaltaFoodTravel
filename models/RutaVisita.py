import json

class Ruta_Visita:
    def __init__(self,id_visita, nombre):
        self.id_visita = id_visita
        self.nombre = str(nombre)
        self.destinos=[]
    
    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**ruta) for ruta in data]

    """
    def set_destinos(self, destinos):
        self.destinos = destinos
    """
