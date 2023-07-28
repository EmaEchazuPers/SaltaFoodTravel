class Usuario:
    def __init__(self,id_usuario,nombre,apellido):
        self.id_usuario = id_usuario
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.historial_rutas = []
    
    def cambiar_nombre(self,nombre):
        self.nombre = str(nombre)

    def cambiar_apellido(self, apellido):
        self.apellido = str(apellido)
    
    def agregar_ruta(self, id_ruta):
        self.historial_rutas.append(int(id_ruta))
    
    def eliminar_ruta(self, id_ruta):
        self.historial_rutas.remove(id_ruta)