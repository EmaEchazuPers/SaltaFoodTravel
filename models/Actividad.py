class Actividad:
    def __init__(self, id_actividad, nombre, id_destino):
        self.id_actividad = id_actividad
        self.nombre = str(nombre)
        self.id_destino = int(id_destino)
        self.hora_inicio = ''
    
    def set_nombre(self,nombre):
        self.nombre = str(nombre)
    
    def set_hora(self, hora_inicio):
        self.hora_inicio = str(hora_inicio)