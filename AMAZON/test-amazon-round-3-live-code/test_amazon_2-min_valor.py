#Ejercicio 2: Camino de Mínimo Valor en una Matriz con Límites
#Enunciado
# Dada la siguiente matriz:
# [ [3, 5, 2, 1],
#  [4, 2, 1, 6],
#  [5, 3, 0, 1],
#  [2, 5, 4, 3] ]
# Se requiere encontrar el camino que permita recorrer la matriz desde la esquina superior izquierda 
# (valor 3) hasta la esquina inferior derecha (valor 3), de modo que se minimice la suma total de 
# los valores de las celdas por las que se transita.

#Condiciones:

# Solo se puede mover a celdas adyacentes (arriba, abajo, izquierda, derecha).
# Los movimientos deben respetar los límites de la matriz (no se puede salir de la misma).
# El objetivo es obtener la suma mínima del camino y, opcionalmente, conocer el recorrido seguido.
'''
function caminoMinimo(matriz):
    filas = número de filas de matriz
    columnas = número de columnas de matriz

    // Inicializamos una matriz "dist" para guardar la suma mínima para llegar a cada celda
    dist = matriz de tamaño [filas][columnas] inicializada con infinito
    dist[0][0] = matriz[0][0]  // La suma para empezar es el valor en la celda inicial

    // Usamos una cola de prioridad para gestionar los nodos a explorar (costo, (fila, columna))
    PQ = nueva ColaDePrioridad()
    PQ.insertar((dist[0][0], (0, 0)))

    // Movimientos posibles: abajo, arriba, derecha, izquierda
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while PQ no esté vacía:
        (costo_actual, (fila, col)) = PQ.extraer_min()  // Extrae el nodo con menor costo

        // Si hemos llegado a la esquina inferior derecha, retornamos el costo
        if fila == filas - 1 y col == columnas - 1:
            return costo_actual

        // Explorar cada vecino
        for (df, dc) in movimientos:
            nuevaFila = fila + df
            nuevaCol = col + dc

            // Comprobar que el vecino esté dentro de los límites
            if nuevaFila está entre 0 y filas-1 y nuevaCol está entre 0 y columnas-1:
                nuevo_costo = costo_actual + matriz[nuevaFila][nuevaCol]
                if nuevo_costo < dist[nuevaFila][nuevaCol]:
                    dist[nuevaFila][nuevaCol] = nuevo_costo
                    PQ.insertar((nuevo_costo, (nuevaFila, nuevaCol)))

    return "No se encontró un camino válido"
'''
# Implementación en Python
import heapq

def camino_minimo(matriz):
    # Verificar que la matriz no esté vacía y tenga al menos una fila y una columna
    if not matriz or not matriz[0]:
        return None

    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Inicializar la matriz de distancias con infinito
    dist = [[float('inf')] * columnas for _ in range(filas)]
    dist[0][0] = matriz[0][0]  # La suma inicial es el valor en (0,0)
    
    # Cola de prioridad: (costo acumulado, fila, columna)
    pq = [(matriz[0][0], 0, 0)]
    
    # Movimientos posibles: abajo, arriba, derecha, izquierda
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while pq:
        costo_actual, fila, col = heapq.heappop(pq)
        
        # Si llegamos a la esquina inferior derecha, retornamos el costo acumulado
        if fila == filas - 1 and col == columnas - 1:
            return costo_actual
        
        # Si el costo actual es mayor que el almacenado, se omite
        if costo_actual > dist[fila][col]:
            continue
        
        # Explorar celdas adyacentes
        for df, dc in movimientos:
            nuevaFila = fila + df
            nuevaCol = col + dc
            
            # Verificar límites de la matriz
            if 0 <= nuevaFila < filas and 0 <= nuevaCol < columnas:
                nuevo_costo = costo_actual + matriz[nuevaFila][nuevaCol]
                if nuevo_costo < dist[nuevaFila][nuevaCol]:
                    dist[nuevaFila][nuevaCol] = nuevo_costo
                    heapq.heappush(pq, (nuevo_costo, nuevaFila, nuevaCol))
                    
    return None  # En caso de que no exista un camino

# Función para ejecutar tests
def run_tests():
    # Test 1: Matriz proporcionada
    matriz1 = [
        [3, 5, 2, 1],
        [4, 2, 1, 6],
        [5, 3, 0, 1],
        [2, 5, 4, 3]
    ]
    # Se espera que el camino mínimo sea 14, basado en la ruta:
    # (0,0)=3 -> (1,0)=4 -> (1,1)=2 -> (1,2)=1 -> (2,2)=0 -> (2,3)=1 -> (3,3)=3
    esperado1 = 14
    resultado1 = camino_minimo(matriz1)
    print("Test 1:")
    print("Esperado:", esperado1)
    print("Obtenido:", resultado1)
    print("Test 1", "PASÓ" if resultado1 == esperado1 else "FALLÓ")
    print("-" * 40)
    
    # Test 2: Matriz de 1x1
    matriz2 = [[7]]
    # El único camino es la celda misma, por lo que se espera 7.
    esperado2 = 7
    resultado2 = camino_minimo(matriz2)
    print("Test 2:")
    print("Esperado:", esperado2)
    print("Obtenido:", resultado2)
    print("Test 2", "PASÓ" if resultado2 == esperado2 else "FALLÓ")
    print("-" * 40)
    
    # Test 3: Matriz vacía
    matriz3 = []
    esperado3 = None
    resultado3 = camino_minimo(matriz3)
    print("Test 3:")
    print("Esperado:", esperado3)
    print("Obtenido:", resultado3)
    print("Test 3", "PASÓ" if resultado3 == esperado3 else "FALLÓ")
    print("-" * 40)

if __name__ == "__main__":
    run_tests()

