import json

class Review:
    def __init__(self, id_review, id_destino, id_usuario):
        self.id_review = id_review
        self.id_destino = int(id_destino)
        self.id_usuario = int(id_usuario)
        self.calificacion = 0
        self.comentario = ''
        self.animo = ''
    
    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**review) for review in data]
