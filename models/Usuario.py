class Usuario:
    def __init__(self,id_usuario,nombre,apellido):
        self.id_usuario = id_usuario
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.historial_rutas = []
      
    def set_ruta(self, historial_rutas):
        self.historial_rutas = historial_rutas
    