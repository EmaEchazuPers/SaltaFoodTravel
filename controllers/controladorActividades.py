class ControladorActividades:
    def __init__(self,app,actividades):
        self.app = app
        self.actividades = actividades

    def getActividades(self):
        return self.actividades
    
    def seleccionar(self,event):
        indice = self.lista_lugares.curselection()
        destino_seleccionado = 0
        if indice == 0:
            destino_seleccionado = self.destinos
        actividades = self.controlador_Act.getActividades()
        self.lista_lugares.delete(0, tk.END)
        for act in actividades:
            self.lista_actividades.insert(tk.END, act.nombre)