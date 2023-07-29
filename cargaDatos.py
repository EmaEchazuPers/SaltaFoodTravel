import models.DestinoCulinario
import models.Actividad
import models.Review
import models.RutaVisita
import models.Ubicacion
import models.Usuario

class cargaDatos:
    def __init__(self):
        pass
    
    def devolver_datos(self):
        return False




des_mercado = models.DestinoCulinario.Destino('Mercado Artesanal')
des_mercado.cambiar_cocina('Regional')
des_mercado.agregar_ingrediente('Tomate')
des_mercado.agregar_ingrediente('Aji')
des_mercado.agregar_ingrediente('Choclo')
des_mercado.agregar_ingrediente('Carne')
des_mercado.cambiar_precios(1200,8000)
des_mercado.cambiar_popularidad(3.4)
des_mercado.cambiar_disponibilidad()
des_mercado.cambiar_ubicacion(3) #Aca ingresa id de ubicacion
des_mercado.cambiar_imagen('miimagen.com')


des_colonial = models.DestinoCulinario.Destino('La Colonial')
des_colonial.cambiar_cocina('Popular')
des_colonial.agregar_ingrediente('Tomate')
des_colonial.agregar_ingrediente('Pescado')
des_colonial.agregar_ingrediente('Pastas')
des_colonial.agregar_ingrediente('Carne')
des_colonial.cambiar_precios(2500,12000)
des_colonial.cambiar_popularidad(4.1)
des_colonial.cambiar_disponibilidad()
des_colonial.cambiar_ubicacion(2) #Aca ingresa id de ubicacion
des_colonial.cambiar_imagen('miimagen.com/2')
