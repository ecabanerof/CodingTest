

from itertools import permutations

def tsp_bruteforce(cost):
    # Número de ciudades, basado en el tamaño de la matriz de costos.
    n = len(cost)
    # Creamos una lista de ciudades: [0, 1, 2, ..., n-1]
    cities = list(range(n))
    # Inicializamos el costo mínimo con un valor muy alto.
    min_cost = float('inf')
    # Aquí se almacenará la mejor ruta encontrada.
    best_path = None

    # Generamos todas las permutaciones de las ciudades EXCLUYENDO la ciudad 0.
    # La ciudad 0 se fija como punto de partida y llegada.
    for perm in permutations(cities[1:]):
        # Construimos la ruta completa: comenzamos en la ciudad 0,
        # visitamos las ciudades en el orden dado por la permutación, y volvemos a la ciudad 0.
        path = [0] + list(perm) + [0]

        # Calculamos el costo total de la ruta.
        total = 0
        # Recorremos la ruta sumando el costo de ir de cada ciudad a la siguiente.
        for i in range(len(path) - 1):
            total += cost[path[i]][path[i+1]]

        # Si el costo total de esta ruta es menor que el costo mínimo actual,
        # actualizamos el costo mínimo y guardamos esta ruta.
        if total < min_cost:
            min_cost = total
            best_path = path

    # Devolvemos la mejor ruta encontrada y su costo total.
    return best_path, min_cost

# Ejemplo de uso:
if __name__ == '__main__':
    # Definimos una matriz de costos de ejemplo.
    cost_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    # Ejecutamos la función para encontrar la ruta óptima y el costo mínimo.
    best_route, best_cost = tsp_bruteforce(cost_matrix)
    
    print("Ruta óptima:", best_route)
    print("Costo mínimo:", best_cost)