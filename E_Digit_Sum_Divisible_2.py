def solve(n):
    # Convertimos n a string para trabajar con sus dígitos
    n_str = str(n)
    
    # Si n ya tiene suma de dígitos par, devolvemos n
    digit_sum = sum(int(digit) for digit in n_str)
    if digit_sum % 2 == 0:
        return n
    
    # Si la suma es impar, necesitamos encontrar un número cercano con suma par
    
    # Intentamos aumentar un dígito
    for i in range(len(n_str)):
        # Empezamos desde el final para minimizar el cambio
        pos = len(n_str) - 1 - i
        digit = int(n_str[pos])
        
        # Si incrementar este dígito cambia la paridad de la suma
        # (incrementar un dígito añade +1 a la suma, cambiando la paridad)
        if digit < 9:
            new_n = int(n_str[:pos] + str(digit + 1) + '0' * i)
            return new_n
    
    # Si no podemos incrementar, añadimos un 1 al principio y ajustamos
    return int('1' + '0' * len(n_str))

# Lectura y escritura
n = int(input())
result = solve(n)
print(result)