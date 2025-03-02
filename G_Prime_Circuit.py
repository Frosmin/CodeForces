def solve(n):
    # Convertimos n a string para trabajar con sus dígitos
    n_str = str(n)
    
    # Si n ya tiene suma de dígitos par, devolvemos n
    digit_sum = sum(int(digit) for digit in n_str)
    if digit_sum % 2 == 0:
        return n
    
    # Busca el mejor cambio para hacer la suma par
    # Opción 1: Incrementar un dígito para cambiar la paridad
    min_increment = float('inf')
    min_increment_result = None
    
    for i in range(len(n_str)):
        digit = int(n_str[i])
        if digit < 9:
            # Incrementamos este dígito y hacemos los siguientes ceros
            new_digits = list(n_str)
            new_digits[i] = str(digit + 1)
            for j in range(i + 1, len(n_str)):
                new_digits[j] = '0'
            
            new_num = int(''.join(new_digits))
            increment = new_num - n
            
            if increment < min_increment:
                min_increment = increment
                min_increment_result = new_num
    
    # Opción 2: Decrementar un dígito para cambiar la paridad
    min_decrement = float('inf')
    min_decrement_result = None
    
    for i in range(len(n_str)):
        digit = int(n_str[i])
        if i > 0 and digit > 0:  # No podemos decrementar el primer dígito a 0
            # Decrementamos este dígito y hacemos los siguientes 9s
            new_digits = list(n_str)
            new_digits[i] = str(digit - 1)
            for j in range(i + 1, len(n_str)):
                new_digits[j] = '9'
            
            new_num = int(''.join(new_digits))
            decrement = n - new_num
            
            if decrement < min_decrement:
                min_decrement = decrement
                min_decrement_result = new_num
    
    # Elegir la mejor opción
    if min_increment <= min_decrement and min_increment_result is not None:
        return min_increment_result
    elif min_decrement_result is not None:
        return min_decrement_result
    else:
        # Si no podemos decrementar o incrementar, añadimos un dígito
        return int('1' + '0' * len(n_str))

# Lectura y escritura
n = int(input())
result = solve(n)
print(result)