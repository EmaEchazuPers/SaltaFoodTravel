class Ruta_Visita:
    def __init__(self,id_visita, nombre):
        self.id_visita = id_visita
        self.nombre = str(nombre)
        self.destinos=[]
    
    def cambiar_nombre(self,nombre):
        self.nombre = str(nombre)
    
    def agregar_visita(self, id_destino):
        self.destinos.append(int(id_destino))
    
    def eliminar_ruta(self, id_destino):
        self.destinos.remove(id_destino)