class Actividad:
    id_actividad = 0
    def __init__(self, nombre, id_destino):
        Actividad.id_actividad += 1
        self.id_actividad = Actividad.id_actividad
        self.nombre = str(nombre)
        self.id_destino = int(id_destino)
        self.hora_inicio = ''
    
    def cambiar_nombre(self,nombre):
        self.nombre = str(nombre)
    
    def cambiar_hora(self, hora_inicio):
        self.hora_inicio = str(hora_inicio)