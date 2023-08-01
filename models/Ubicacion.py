class Ubicacion:
    def __init__(self,id_ubicacion, direccion):
        self.id_ubicacion = id_ubicacion
        self.direccion = str(direccion)
        self.coordenadas=[]
    
    def cambiar_direccion(self,direccion):
        self.direccion = str(direccion)
    
    def agregar_coordenadas(self,coordenadas):
        self.coordenadas = coordenadas

    def modificar_coordenada(self, coordenada, nuevacoordenada):
        if coordenada in self.coordenadas:
            self.coordenadas[coordenada] = nuevacoordenada
    
    def eliminar_coordenada(self, coordenada):
        self.coordenadas.remove(coordenada)