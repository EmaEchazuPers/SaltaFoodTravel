import json

class Actividad:
    def __init__(self, id_actividad, nombre, id_destino):
        self.id_actividad = id_actividad
        self.nombre = str(nombre)
        self.id_destino = int(id_destino)
        self.hora_inicio = ''
    
    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**actividad) for actividad in data]
