import json

class Destino:
    def __init__(self, id_destino, nombre, tipo_cocina, ingredientes, precio_min, precio_max, popularidad, disponibilidad, id_ubicacion,imagen):        
        self.id_destino = id_destino
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_min = precio_min
        self.precio_max = precio_max
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

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