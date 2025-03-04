# Ejercicio 3: Construcción de una API en Pseudocódigo para Gestión de Ficheros
# Enunciado
# Objetivo:
# Diseñar una API en pseudocódigo que integre varias funciones para interactuar con el sistema de ficheros. 
# La API debe incluir las siguientes funcionalidades:

#  - Calcular el tamaño de un fichero dado su ruta.
#  - Obtener la ruta absoluta de un fichero a partir de su nombre.
#  - Listar todos los ficheros de un directorio que tengan una extensión específica (por ejemplo, .csv).
# La idea es que la API se comporte como una función principal que, según la acción solicitada, 
# invoque a la función correspondiente.

#Pseudocódigo

// Función para calcular el tamaño de un fichero
function calcularTamañoFichero(ruta):
    // Aquí se implementa la lógica para obtener el tamaño
    tamaño = ...  // Código que calcula el tamaño del fichero en bytes
    return tamaño

// Función para obtener la ruta absoluta de un fichero dado su nombre
function obtenerRutaFichero(nombreFichero):
    // Buscar en el sistema la ruta absoluta que corresponda al nombre del fichero
    ruta = ...  // Código que realiza la búsqueda
    return ruta

// Función para listar ficheros en un directorio filtrando por extensión
function listarFicherosPorExtension(directorio, extension):
    listaFicheros = []  // Inicializar lista vacía
    ficheros = obtenerListaDeFicheros(directorio)  // Función que lista todos los ficheros en el directorio
    
    for fichero in ficheros:
        if fichero termina con extension:
            listaFicheros.append(fichero)
    
    return listaFicheros

// Función principal de la API que integra los métodos anteriores
function API_GestionFicheros(accion, parametros):
    if accion == "obtener_tamaño":
        ruta = parametros["ruta"]
        return calcularTamañoFichero(ruta)
    else if accion == "obtener_ruta":
        nombre = parametros["nombre"]
        return obtenerRutaFichero(nombre)
    else if accion == "listar_por_extension":
        directorio = parametros["directorio"]
        extension = parametros["extension"]
        return listarFicherosPorExtension(directorio, extension)
    else:
        return "Acción no soportada"

// Ejemplo de uso de la API
imprimir(API_GestionFicheros("listar_por_extension", {"directorio": "/mi/directorio", "extension": ".csv"}))
