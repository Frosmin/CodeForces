

# def snake(n):
#     primer_digito = int(n[0])  
#     for i in range(1, len(n)):
#         if primer_digito <= int(n[i]):  
#             return False
#     return True

# l,r = (map(str , input().split()))
# ln = int(l)
# rn = int(r)
# res = 0
# for num in range(ln,rn+1):
#     if snake(str(num)):
#         res += 1
# print(res)    


# def es_snake(num):
#     num_str = str(num)
#     primer_digito = int(num_str[0])
    
#     # Verificar todos los dígitos de una vez usando all()
#     return all(primer_digito > int(digito) for digito in num_str[1:])

# # Leer entrada como enteros directamente
# l, r = map(int, input().split())

# # Contar números snake en el rango
# resultado = sum(1 for num in range(l, r+1) if es_snake(num))
# print(resultado)
def es_snake(num):
    """
    Verifica si un número es un número snake.
    Un número snake tiene su primer dígito estrictamente mayor que todos los demás dígitos.
    """
    num_str = str(num)
    primer_digito = int(num_str[0])
    
    # Verificar que el número tenga al menos 2 dígitos
    if len(num_str) < 2:
        return False
    
    # Verificar que el primer dígito sea mayor que todos los demás
    return all(primer_digito > int(digito) for digito in num_str[1:])

def contar_snake_eficiente(l, r):
    """
    Fórmula matemática directa para contar números snake en un rango [l, r]
    """
    def contar_hasta(n):
        if n < 10:
            return 0
        
        n_str = str(n)
        n_len = len(n_str)
        resultado = 0
        
        # Contar todos los números snake con menos dígitos
        for longitud in range(2, n_len):
            for d in range(1, 10):
                # Para cada dígito inicial d, hay d^(longitud-1) números snake
                resultado += d ** (longitud - 1)
        
        # Contar números snake con la misma longitud
        primer_digito = int(n_str[0])
        
        # Números que empiezan con dígito menor que el primer dígito de n
        for d in range(1, primer_digito):
            resultado += d ** (n_len - 1)
        
        # Números que empiezan con el mismo dígito que n
        prefijo = n_str[0]
        for i in range(1, n_len):
            actual_digit = int(n_str[i])
            
            # Contamos números que tienen dígitos menores en esta posición
            for d in range(0, min(actual_digit, primer_digito)):
                # Solo si el dígito es menor que el primer dígito
                if d < primer_digito:
                    # Calculamos cuántos números snake pueden formarse con este prefijo
                    resultado += primer_digito ** (n_len - i - 1)
            
            # Si encontramos un dígito mayor o igual al primer dígito, ya no podemos
            # formar más números snake con este prefijo
            if actual_digit >= primer_digito:
                break
            
            # Actualizamos el prefijo para la siguiente iteración
            prefijo += n_str[i]
        
        # Verificar si n mismo es un número snake
        if es_snake(n):
            resultado += 1
        
        return resultado
    
    return contar_hasta(r) - contar_hasta(l - 1)

# Leer entrada
l, r = map(int, input().split())

# Determinar qué enfoque usar
if r - l <= 10**6:
    # Para rangos pequeños, usar el enfoque directo
    resultado = 0
    for num in range(max(10, l), r+1):
        if es_snake(num):
            resultado += 1
    print(resultado)
else:
    # Para rangos grandes, usar el enfoque matemático
    print(contar_snake_eficiente(max(10, l), r))