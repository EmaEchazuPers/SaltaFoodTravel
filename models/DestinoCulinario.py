class Destino:
    def __init__(self, id_destino,nombre):
        self.id_destino = id_destino
        self.nombre = nombre
        self.ingredientes = []        
        self.precio_min = 0.0
        self.precio_max = 0.0
        self.popularidad = 0.0
        self.disponibilidad = False
        self.id_ubicacion = 0
        self.imagen = ''
    
    def cambiar_nombre(self, nombre):
        self.nombre = str(nombre)

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(str(ingrediente))
    
    def modificar_ingrediente(self, ingrediente, nuevoingrediente):
        if ingrediente in ingredientes:
            self.ingredientes[ingrediente] = nuevoingrediente
    
    def eliminar_ingrediente(self, ingrediente):
        self.ingredientes.remove(ingrediente)
    
    def cambiar_precios(self, minimo, maximo):
        self.precio_min = float(minimo)
        self.precio_max = float(maximo)
    
    def cambiar_popularidad(self, popularidad):
        self.popularidad = float(popularidad)
    
    def cambiar_disponibilidad(self):
        if self.disponibilidad:
            self.disponibilidad = False
        else:
            self.disponibilidad = True

    def cambiar_ubicacion(self, id_ubicacion):
            self.id_ubicacion = int(id_ubicacion)
    
    def cambiar_imagen(self, imagen):
        self.imagen = str(imagen)
