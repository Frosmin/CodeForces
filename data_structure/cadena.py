# Ejemplo: buscar si alguno de los caracteres está en la palabra
chars = set("ABC")
word = "SAMUEL"

# 1) Saber si hay alguna coincidencia
hay = bool(chars & set(word))
print(hay)  # True

# 2) Encontrar la primera posición (índice 0-based), -1 si no existe
first_index = next((i for i, ch in enumerate(word) if ch in chars), -1)
print(first_index)  # 1

# 3) Todas las posiciones donde aparece alguno de los caracteres
positions = [i for i, ch in enumerate(word) if ch in chars]
print(positions)  # [1]

# Si prefieres posiciones 1-based:
positions_1_based = [i+1 for i in positions]
print(positions_1_based)  # [2]