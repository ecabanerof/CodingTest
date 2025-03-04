
import itertools

def tsp_brute_force(distance_matrix):
    """
    Resuelve TSP usando fuerza bruta generando todas las permutaciones.
    Args:
        distance_matrix (list[list[int]]): Matriz de distancias entre ciudades.
    Returns:
        int: Costo mínimo de la ruta.
    """
    n = len(distance_matrix)
    min_cost = float('inf')
    for perm in itertools.permutations(range(1, n)):
        cost = distance_matrix[0][perm[0]]  # Desde la ciudad inicial
        for i in range(len(perm) - 1):
            cost += distance_matrix[perm[i]][perm[i + 1]]
        cost += distance_matrix[perm[-1]][0]  # Regreso al inicio
        min_cost = min(min_cost, cost)
    return min_cost

def tsp_nearest_neighbor(distance_matrix):
    """
    Resuelve TSP usando el algoritmo del vecino más cercano (heurística).
    Args:
        distance_matrix (list[list[int]]): Matriz de distancias entre ciudades.
    Returns:
        tuple: (ruta, costo).
    """
    n = len(distance_matrix)
    visited = [False] * n
    tour = [0]  # Empezamos en la ciudad 0
    visited[0] = True
    current = 0
    
    for _ in range(n - 1):
        next_city = min(
            (city for city in range(n) if not visited[city]),
            key=lambda city: distance_matrix[current][city]
        )
        tour.append(next_city)
        visited[next_city] = True
        current = next_city
    
    tour.append(0)  # Regresar al inicio
    cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(n))
    return tour, cost

if __name__ == "__main__":
    # Caso de prueba 1: Ejemplo con 4 ciudades
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    assert tsp_brute_force(distance_matrix) == 80, "Fuerza bruta falló"
    tour, cost = tsp_nearest_neighbor(distance_matrix)
    print(f"Fuerza bruta: Costo = {tsp_brute_force(distance_matrix)}")  # Esperado: 80
    print(f"Vecino más cercano: Tour = {tour}, Costo = {cost}")      # Ejemplo: [0, 1, 3, 2, 0], 80

    # Caso de prueba 2: Matriz más pequeña
    small_matrix = [
        [0, 5, 10],
        [5, 0, 8],
        [10, 8, 0]
    ]
    assert tsp_brute_force(small_matrix) == 23, "Fuerza bruta falló en caso pequeño"
    tour, cost = tsp_nearest_neighbor(small_matrix)
    print(f"Fuerza bruta (pequeño): Costo = {tsp_brute_force(small_matrix)}")  # Esperado: 23
    print(f"Vecino más cercano (pequeño): Tour = {tour}, Costo = {cost}")
