import models.DestinoCulinario
import models.Actividad
import models.Review
import models.RutaVisita
import models.Ubicacion
import models.Usuario

# Creacion ubicaciones

ubi_mercado = models.Ubicacion.Ubicacion('Av. San Martin 780')
ubi_mercado.agregar_coordenada(-24.79304)
ubi_mercado.agregar_coordenada(-65.41337)

ubi_colonial = models.Ubicacion.Ubicacion('Pje. Zorrilla 245')
ubi_colonial.agregar_coordenada(-24.78786)
ubi_colonial.agregar_coordenada(-65.40580)

# Creacion destinos

des_mercado = models.DestinoCulinario.Destino('Mercado Artesanal')
des_mercado.cambiar_cocina('Regional')
des_mercado.agregar_ingrediente('Tomate')
des_mercado.agregar_ingrediente('Aji')
des_mercado.agregar_ingrediente('Choclo')
des_mercado.agregar_ingrediente('Carne')
des_mercado.cambiar_precios(1200,8000)
des_mercado.cambiar_popularidad(3.4)
des_mercado.cambiar_disponibilidad()
des_mercado.cambiar_ubicacion(ubi_mercado.id_ubicacion)
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
des_colonial.cambiar_ubicacion(ubi_colonial.id_ubicacion) 
des_colonial.cambiar_imagen('miimagen.com/2')

# Creacion actividades

act1_mercado = models.Actividad.Actividad('Concurso de empanadas', des_mercado.id_destino)
act1_mercado.cambiar_hora('2023-07-04T10:00:00')
act2_mercado = models.Actividad.Actividad('Concurso de pizzas', des_mercado.id_destino)
act2_mercado.cambiar_hora('2023-07-04T13:00:00')
act1_colonial = models.Actividad.Actividad('Recital folclore', des_colonial.id_destino)
act1_colonial.cambiar_hora('2023-07-04T20:00:00')

# Creacion ruta visitas

ruta1 = models.RutaVisita.Ruta_Visita('Mi ruta')
ruta1.agregar_visita(des_mercado.id_destino)
ruta1.agregar_visita(des_colonial.id_destino)

# Creacion usuario

usuario1 = models.Usuario.Usuario('Juan','Perez')
usuario1.agregar_ruta(ruta1.id_visita)

# Creacion review

review1 = models.Review.Review(des_mercado.id_destino,usuario1.id_usuario)
review1.cambiar_calificacion(4)
review1.cambiar_comentario('Muy buenas pizzas, mucho ruido')
review1.cambiar_animo('Positivo')
review2 = models.Review.Review(des_colonial.id_destino,usuario1.id_usuario)
review2.cambiar_calificacion(2)
review2.cambiar_comentario('Mala atencion, poca variedad')
review2.cambiar_animo('Negativo')

