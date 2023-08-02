class Ruta_Visita:
    def __init__(self,id_visita, nombre):
        self.id_visita = id_visita
        self.nombre = str(nombre)
        self.destinos=[]
       
    def set_destinos(self, destinos):
        self.destinos = destinos
