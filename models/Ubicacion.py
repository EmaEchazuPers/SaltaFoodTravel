class Ubicacion:
    id_ubicacion = 0
    def __init__(self, direccion):
        Ubicacion.id_ubicacion += 1
        self.id_ubicacion = Ubicacion.id_ubicacion
        self.direccion = str(direccion)
        self.coordenadas=[]
    
    def cambiar_direccion(self,direccion):
        self.direccion = str(direccion)
    
    def agregar_coordenada(self, id_coordenada):
        self.coordenadas.append(int(id_coordenada))
    
    def eliminar_coordenada(self, id_coordenada):
        self.coordenadas.remove(id_coordenada)