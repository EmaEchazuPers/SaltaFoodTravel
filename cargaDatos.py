import json 
import models.DestinoCulinario as Mod_Destino
import models.Ubicacion as Mod_Ubicacion
import models.Actividad as Mod_Actividad
import models.Review as Mod_Review
import models.RutaVisita as Mod_Ruta
import models.Usuario as Mod_Usuario

lista_destinos = []
lista_ubicaciones = []
lista_actividades = []
lista_reviews = []
lista_rutas = []
lista_usuarios = []

#Funcion apertura de archivos JSON

def apertura_json(dir_json):
    with open(dir_json,'r') as f:
        dicc = json.load(f)
    return dicc

#Carga de destinos

dicc_destinos = apertura_json('data\destinos.json')

for destino in dicc_destinos.values():
    nuevoDestino = Mod_Destino.Destino(destino["id_destino"],destino["nombre"])
    nuevoDestino.set_cocina(destino["tipo_cocina"])
    nuevoDestino.set_disponibilidad(destino["disponibilidad"])
    nuevoDestino.set_imagen(destino["imagen"])
    nuevoDestino.set_ingredientes(destino["ingredientes"])
    nuevoDestino.set_popularidad(destino["popularidad"])
    nuevoDestino.set_precios(destino["precio_min"],destino["precio_max"])
    nuevoDestino.set_ubicacion(destino["id_ubicacion"])
    lista_destinos.append(nuevoDestino)

#Carga de ubicaciones

dicc_ubicaciones = apertura_json('data\\ubicaciones.json')

for ubicacion in dicc_ubicaciones.values():
    nuevaUbicacion = Mod_Ubicacion.Ubicacion(ubicacion["id_ubicacion"],ubicacion["direccion"])
    nuevaUbicacion.set_coordenadas(ubicacion["coordenadas"])
    lista_ubicaciones.append(nuevaUbicacion)

#Carga de actividades

dicc_actividades = apertura_json('data\\actividades.json')

for actividad in dicc_actividades.values():
    nuevaActividad = Mod_Actividad.Actividad(actividad["id_actividad"],actividad["nombre"],actividad["id_destino"])
    nuevaActividad.set_hora(actividad["hora_inicio"])
    lista_actividades.append(nuevaActividad)

#Carga de reviews

dicc_reviews = apertura_json('data\\reviews.json')

for review in dicc_reviews.values():
    nuevaReview = Mod_Review.Review(review["id_review"],review["id_destino"],review["id_usuario"])
    nuevaReview.set_comentario(review["comentario"])
    nuevaReview.set_calificacion(review["calificacion"])
    nuevaReview.set_animo(review["animo"])
    lista_reviews.append(nuevaReview)

#Carga de rutas visitas

dicc_rutas = apertura_json('data\\rutasvisitas.json')

for ruta in dicc_rutas.values():
    nuevaRuta = Mod_Ruta.Ruta_Visita(ruta["id_visita"],ruta["nombre"])
    nuevaRuta.set_destinos(ruta["destinos"])
    lista_rutas.append(nuevaRuta)

#Carga de usuarios

dicc_usuarios = apertura_json('data\\usuarios.json')

for usuario in dicc_usuarios.values():
    nuevoUsuario = Mod_Usuario.Usuario(usuario["id_usuario"],usuario["nombre"],usuario["apellido"])
    nuevoUsuario.set_ruta(usuario["historial_rutas"])
    lista_usuarios.append(nuevoUsuario)

#Return de lista con objetos

def devolver_lista_destinos():
    return lista_destinos

def devolver_lista_ubicaciones():
    return lista_ubicaciones

def devolver_lista_actividades():
    return lista_actividades

def devolver_lista_reviews():
    return lista_reviews

def devolver_lista_rutas():
    return lista_rutas

def devolver_lista_usuarios():
    return lista_usuarios
