## Definición de tipos
# Creación de una tupla con nombre para las coordenadas
from collections import namedtuple
from math import radians, sin, cos, asin, sqrt
Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def a_radianes(coordenadas):
    '''Convierte unas coordenadas en grados a radianes

    @param coordenadas: Coordenadas que se quieren convertir a radianes
    @type coordenadas: Coordenadas(float, float)
    @return: Las coordenadas convertidas a radianes
    @rtype: Coordenadas(float, float)
    
    Ayuda:
    Usa la función radians para convertir a radianes. Por ejemplo,
    latitud_radianes = radians(latitud)
    '''
    pass
    latitud_radianes = radians(coordenadas.latitud)
    longitud_radianes = radians(coordenadas.longitud)
    return Coordenadas(latitud_radianes, longitud_radianes)
       

def distancia_harvesine(coordenadas1, coordenadas2):
    '''Devuelve la distancia de harvesine entre dos coordenadas

    @param coordenadas1: Coordenadas del primer punto
    @type coordenadas1: Coordenadas(float, float)
    @param coordenadas2: Coordenadas del segundo punto
    @type coordenadas2: Coordenadas(float, float)
    @return: La distancia harvesine entre las dos coordenadas dadas como parámetro
    @rtype: float
    '''
    pass
    
    R = 6371.0
    lat1, lon1 = coordenadas1.latitud, coordenadas1.longitud
    lat2, lon2 = coordenadas2.latitud, coordenadas2.longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))

    distancia = R * c
    return distancia

def redondear(coordenadas):
    '''Devuelve unas coordenadas cuya latitud y longitud son 
    el redondeo de la latitud y la longitud de las coordenadas originales

    @param coordenadas: Coordenadas que se quieren convertir a radianes
    @type coordenadas: Coordenadas(float, float)
    @return: Las coordenadas redondeadas
    @rtype: Coordenadas(float, float)

    Ayuda:
    Usa la función round para redondear. Por ejemplo,
    latitud_redondeada = round(latitud)
    '''
    pass

    latitud_redondeada = round(coordenadas.latitud)
    longitud_redondeada = round(coordenadas.longitud)
    return Coordenadas(latitud_redondeada, longitud_redondeada)