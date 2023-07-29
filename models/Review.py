class Review:
    id_review = 0
    def __init__(self, id_destino, id_usuario):
        Review.id_review += 1
        self.id_review = Review.id_review
        self.id_destino = int(id_destino)
        self.id_usuario = int(id_usuario)
        self.calificacion = 0
        self.comentario = ''
        self.animo = ''
    
    def cambiar_calificacion(self,calificacion):
        if calificacion >= 1 & calificacion <= 5:
            self.calificacion = int(calificacion)
        else:
            print('Calificacion no valida')

    def cambiar_comentario(self, comentario):
        self.comentario = str(comentario)

    def cambiar_animo(self, animo):
        self.animo = str(animo)
