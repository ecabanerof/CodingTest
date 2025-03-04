def check_parentesis(s):
    """
    Verifica si el string s tiene los paréntesis balanceados.
    Se utilizan una pila (stack) y un diccionario para mapear los paréntesis de cierre a sus correspondientes de apertura.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # Si el carácter es un paréntesis de apertura, se añade a la pila.
        if char in mapping.values():
            stack.append(char)
        # Si es un paréntesis de cierre, se verifica que la pila no esté vacía y que el tope de la pila sea su correspondiente de apertura.
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
        # Otros caracteres se pueden ignorar.
    
    # Al finalizar, la pila debe estar vacía si los paréntesis están balanceados.
    return len(stack) == 0

# Ejemplo de uso:
if __name__ == '__main__':
    ejemplos = [
        "({[]})",
        "((())",
        "[{()}]",
        "([)]",
        "{[()()]}"
    ]
    for exp in ejemplos:
        print(f"{exp} -> {check_parentesis(exp)}")
