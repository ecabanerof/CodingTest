##Enunciado
## 1. Juego de dados
#Lo que se evaluó:
# - Comprensión de la lógica condicional y bucles.
# - Capacidad para manejar casos de borde (por ejemplo, qué hacer cuando el dado muestra 0).
# - Estructuración clara de la función.
# Posibles áreas de mejora:

# Claridad en la lógica: La verificación if pos == i: puede llevar a confusión. 
#       Podrías haber comentado o replanteado la lógica para dejar claro que el avance se hace 
#       solo cuando el índice coincide con la posición actual.
# Casos límite: Asegúrate de que todos los posibles escenarios (por ejemplo, qué ocurre si el 
#       dado en la posición actual no permite avanzar) queden perfectamente documentados y manejados.
# Optimización: Considera cómo simplificar las condiciones para hacer el código más legible sin 
#       sacrificar la funcionalidad.

def jugar_mesa(dados):
    pos = 0  # Posición inicial
    for i in range(len(dados)):
        if pos == i:  # Si estoy en esta posición
            if dados[pos] == 0 and pos != 7:
                return f"No ganaste. Te atascaste en {pos} por un 0."
            if pos + dados[pos] <= 7:
                pos += dados[pos]  # Avanzo lo que dice el dado
            if pos == 7:
                return "¡Ganaste! Llegaste a 7."
    return f"No ganaste. Terminaste en {pos}."

# Caso 1
print("Caso 1:")
print(jugar_mesa([3, 2, 0, 1, 3, 2, 1, 0]))

# Caso 2
print("\nCaso 2:")
print(jugar_mesa([2, 0, 0, 3, 3, 2, 1, 0]))