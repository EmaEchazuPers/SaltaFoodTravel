class Ruta_Visita:
    id_visita = 0
    def __init__(self,nombre):
        Ruta_Visita.id_visita += 1
        self.id_visita = Ruta_Visita.id_visita
        self.nombre = str(nombre)
        self.destinos=[]
    
    def cambiar_nombre(self,nombre):
        self.nombre = str(nombre)
    
    def agregar_visita(self, id_destino):
        self.destinos.append(int(id_destino))
    
    def eliminar_ruta(self, id_destino):
        self.destinos.remove(id_destino)