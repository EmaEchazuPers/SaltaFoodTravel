class Destino:
    id_destino = 0
    def __init__(self, nombre):
        Destino.id_destino += 1
        self.id_destino = Destino.id_destino
        self.nombre = nombre
        self.tipo_cocina = ''
        self.ingredientes = []        
        self.precio_min = 0.0
        self.precio_max = 0.0
        self.popularidad = 0.0
        self.disponibilidad = False
        self.id_ubicacion = 0
        self.imagen = ''
    
    def cambiar_nombre(self, nombre):
        self.nombre = str(nombre)
    
    def cambiar_cocina(self, tipo_cocina):
        self.tipo_cocina = str(tipo_cocina)

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(str(ingrediente))
    
    def modificar_ingrediente(self, ingrediente, nuevoingrediente):
        if ingrediente in self.ingredientes:
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
