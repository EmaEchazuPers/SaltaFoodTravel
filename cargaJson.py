import json 
import models.DestinoCulinario as Mod_Destino
import models.Ubicacion as Mod_Ubicacion

lista_destinos = []

with open('data\destinos.json','r') as f:
    dicc_destinos = json.load(f)

with open("data\\ubicaciones.json","r") as u:
    dicc_ubicaciones = json.load(u)


for destino in dicc_destinos.values():
    destinoAux = Mod_Destino.Destino(destino["nombre"])
    destinoAux.cambiar_cocina(destino["tipo_cocina"])
    destinoAux.cambiar_ingredientes(destino["ingredientes"])
    destinoAux.cambiar_precios(destino["precio_min"],destino["precio_max"])
    destinoAux.cambiar_popularidad(destino["popularidad"])
    destinoAux.cambiar_disponibilidad(destino["disponibilidad"])
    destinoAux.cambiar_ubicacion(destino["id_ubicacion"])
    destinoAux.cambiar_imagen(destino["imagen"])
    lista_destinos.append(destinoAux)

for a in lista_destinos:
    print(a.nombre)
    print(a.disponibilidad)
    print(a.imagen)
    print(a.popularidad)
    

