class Usuario:
    id_usuario = 0
    def __init__(self,nombre,apellido):
        Usuario.id_usuario += 1
        self.id_usuario = Usuario.id_usuario
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