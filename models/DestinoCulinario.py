import json

class Destino:
    def __init__(self, id_destino, nombre):        
        self.id_destino = id_destino
        self.nombre = nombre
        self.tipo_cocina = ''
        self.ingredientes = []        
        self.precio_min = 0.0
        self.precio_max = 0.0
        self.popularidad = 0.0
        self.disponibilidad = False
        self.id_ubicacion = 0
        self.imagen = ''

    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**destino) for destino in data]
    """
    def set_nombre(self, nombre):
        self.nombre = str(nombre)
    
    def set_cocina(self, tipo_cocina):
        self.tipo_cocina = str(tipo_cocina)

    def set_ingredientes(self, ingredientes):
        self.ingredientes = ingredientes
    
    def set_precios(self, minimo, maximo):
        self.precio_min = float(minimo)
        self.precio_max = float(maximo)
    
    def set_popularidad(self, popularidad):
        self.popularidad = float(popularidad)
    
    def set_disponibilidad(self,disponibilidad):
        if disponibilidad:
            self.disponibilidad = True
        else:
            self.disponibilidad = False

    def set_ubicacion(self, id_ubicacion):
            self.id_ubicacion = int(id_ubicacion)
    
    def set_imagen(self, imagen):
        self.imagen = str(imagen)
"""