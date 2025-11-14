

import sys
from collections import defaultdict

# Función para leer una línea de enteros
def read_ints():
    return map(int, sys.stdin.readline().split())

def solve():
    n, a = read_ints()
    v = list(read_ints())
    
    # events almacenará los cambios en la puntuación en coordenadas específicas
    # events[x] = +k significa que la puntuación aumenta en k en b=x
    # events[x] = -k significa que la puntuación disminuye en k en b=x
    events = defaultdict(int)
    
    score_at_zero = 0
    
    for vi in v:
        if vi == a:
            # Bob nunca gana si vi == a (Alice gana por empate)
            continue
            
        # El otro punto de empate además de 'a' es b = 2*vi - a
        b_tie = 2 * vi - a
        
        # El intervalo abierto (L, R) donde Bob gana
        L = min(a, b_tie)
        R = max(a, b_tie)
        
        # El intervalo cerrado de enteros [start_b, end_b] donde Bob gana
        start_b = L + 1
        end_b = R - 1
        
        if start_b <= end_b:
            # Un intervalo ganador comienza en start_b
            events[start_b] += 1
            # El intervalo termina *después* de end_b,
            # así que restamos 1 en (end_b + 1)
            events[end_b + 1] -= 1
            
            # Comprobamos si b=0 está en este intervalo ganador
            if start_b <= 0 <= end_b:
                score_at_zero += 1

    # Inicializamos con el resultado para b=0
    max_score = score_at_zero
    best_b = 0
    current_score = score_at_zero
    
    # Ordenamos las coordenadas de los eventos para el barrido de línea
    # Solo nos interesan las coordenadas > 0, ya que b=0 ya está calculado
    sorted_coords = sorted([coord for coord in events if coord > 0])
    
    for coord in sorted_coords:
        # Aplicamos el cambio en la puntuación en esta coordenada
        current_score += events[coord]
        
        # Si la puntuación actual es mejor que la máxima encontrada,
        # actualizamos nuestro mejor 'b' y la puntuación máxima.
        if current_score > max_score:
            max_score = current_score
            best_b = coord
            
    print(best_b)

# Leer el número de casos de prueba
try:
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
except EOFError:
    pass
except Exception as e:
    # Manejo de errores en caso de que la entrada no sea la esperada
    # print(f"Error: {e}", file=sys.stderr)
    pass