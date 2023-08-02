import json

class Usuario:
    def __init__(self,id_usuario,nombre,apellido):
        self.id_usuario = id_usuario
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.historial_rutas = []
    
    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**usuario) for usuario in data]

    """
    def set_ruta(self, historial_rutas):
        self.historial_rutas = historial_rutas
    """
    