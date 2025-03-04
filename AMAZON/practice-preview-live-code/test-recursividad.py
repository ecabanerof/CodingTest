def potencia(x, n):
    """
    Calcula x elevado a la n utilizando recursividad.
    Usa el método de exponentiation by squaring para optimizar la complejidad.
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        half = potencia(x, n // 2)
        return half * half
    else:
        return x * potencia(x, n - 1)

# Ejemplo de uso:
if __name__ == '__main__':
    base = 2
    exponente = 10
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} =", resultado)