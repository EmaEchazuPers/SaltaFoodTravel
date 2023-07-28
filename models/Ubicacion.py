class Ubicacion:
    def __init__(self,id_ubicacion,direccion):
        self.id_ubicacion = int(id_ubicacion)
        self.direccion = str(direccion)
        self.coordenadas=[]
    
    def cambiar_direccion(self,direccion):
        self.direccion = str(direccion)
    
    def agregar_coordenada(self, id_coordenada):
        self.coordenadas.append(int(id_coordenada))
    
    def eliminarr_coordenada(self, id_coordenada):
        self.coordenadas.remove(id_coordenada)